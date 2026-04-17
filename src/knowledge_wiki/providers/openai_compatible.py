from __future__ import annotations

import json
import mimetypes
import uuid
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from ..models import GenerationResult
from .base import LLMProvider, ProviderError, build_usage


class OpenAICompatibleProvider(LLMProvider):
    name = "openai_compatible"
    supports_file_inputs = True

    def __init__(
        self,
        *,
        api_key: str | None,
        model: str,
        base_url: str,
        timeout: int = 60,
    ) -> None:
        self.api_key = api_key
        self.model = model
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def generate(self, prompt: str, *, system_prompt: str | None = None) -> GenerationResult:
        if not self.api_key:
            raise ProviderError("OpenAI-compatible provider requires an API key.")
        payload: dict[str, object] = {
            "model": self.model,
            "input": [
                {
                    "role": "user",
                    "content": [{"type": "input_text", "text": prompt}],
                }
            ],
        }
        if system_prompt:
            payload["instructions"] = system_prompt

        request = Request(
            f"{self.base_url}/responses",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        parsed = self._perform_json_request(request)
        return GenerationResult(
            text=_extract_response_text(parsed),
            raw_response=parsed,
            usage=_openai_usage(parsed, provider=self.name, model=self.model),
        )

    def generate_with_files(
        self,
        prompt: str,
        *,
        files: list[Path],
        system_prompt: str | None = None,
    ) -> GenerationResult:
        if not self.api_key:
            raise ProviderError("OpenAI-compatible provider requires an API key.")
        if not files:
            raise ProviderError("At least one file is required for file-input generation.")

        uploaded_file_ids: list[str] = []
        try:
            for path in files:
                uploaded_file_ids.append(self._upload_file(path))
            return self._create_response_with_files(
                prompt, file_ids=uploaded_file_ids, system_prompt=system_prompt
            )
        finally:
            for file_id in uploaded_file_ids:
                self._delete_file(file_id)

    def _create_response_with_files(
        self,
        prompt: str,
        *,
        file_ids: list[str],
        system_prompt: str | None,
    ) -> GenerationResult:
        content: list[dict[str, str]] = []
        if prompt.strip():
            content.append({"type": "input_text", "text": prompt})
        for file_id in file_ids:
            content.append({"type": "input_file", "file_id": file_id})

        payload: dict[str, object] = {
            "model": self.model,
            "input": [{"role": "user", "content": content}],
        }
        if system_prompt:
            payload["instructions"] = system_prompt

        request = Request(
            f"{self.base_url}/responses",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        parsed = self._perform_json_request(request)
        return GenerationResult(
            text=_extract_response_text(parsed),
            raw_response=parsed,
            usage=_openai_usage(parsed, provider=self.name, model=self.model),
        )

    def _upload_file(self, path: Path) -> str:
        boundary = f"----OpenAIBoundary{uuid.uuid4().hex}"
        mime_type = _guess_mime_type(path)
        body = _build_multipart_body(
            boundary=boundary,
            purpose="user_data",
            path=path,
            mime_type=mime_type,
        )
        request = Request(
            f"{self.base_url}/files",
            data=body,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": f"multipart/form-data; boundary={boundary}",
                "Content-Length": str(len(body)),
            },
            method="POST",
        )
        parsed = self._perform_json_request(request)
        file_id = parsed.get("id")
        if not isinstance(file_id, str) or not file_id:
            raise ProviderError("Upload did not return a file ID.")
        return file_id

    def _delete_file(self, file_id: str) -> None:
        request = Request(
            f"{self.base_url}/files/{file_id}",
            headers={"Authorization": f"Bearer {self.api_key}"},
            method="DELETE",
        )
        try:
            with urlopen(request, timeout=self.timeout):
                return
        except Exception:
            return

    def _perform_json_request(self, request: Request) -> dict:
        try:
            with urlopen(request, timeout=self.timeout) as response:
                body = response.read().decode("utf-8")
        except HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="ignore")
            raise ProviderError(f"Provider request failed with HTTP {exc.code}: {detail}") from exc
        except URLError as exc:
            raise ProviderError(f"Provider request failed: {exc.reason}") from exc
        return json.loads(body)


def _build_multipart_body(
    *,
    boundary: str,
    purpose: str,
    path: Path,
    mime_type: str,
) -> bytes:
    boundary_bytes = boundary.encode("utf-8")
    chunks: list[bytes] = []

    def add_field(name: str, value: str) -> None:
        chunks.extend(
            [
                b"--" + boundary_bytes + b"\r\n",
                f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode(),
                value.encode("utf-8"),
                b"\r\n",
            ]
        )

    add_field("purpose", purpose)
    chunks.extend(
        [
            b"--" + boundary_bytes + b"\r\n",
            (
                f'Content-Disposition: form-data; name="file"; filename="{path.name}"\r\n'
                f"Content-Type: {mime_type}\r\n\r\n"
            ).encode(),
            path.read_bytes(),
            b"\r\n",
            b"--" + boundary_bytes + b"--\r\n",
        ]
    )
    return b"".join(chunks)


def _extract_response_text(parsed: dict) -> str:
    texts: list[str] = []
    for item in parsed.get("output", []):
        if not isinstance(item, dict):
            continue
        if item.get("type") == "message":
            for content in item.get("content", []):
                if not isinstance(content, dict):
                    continue
                content_type = content.get("type")
                if content_type in {"output_text", "text"} and isinstance(content.get("text"), str):
                    texts.append(content["text"])
        elif item.get("type") in {"output_text", "text"} and isinstance(item.get("text"), str):
            texts.append(item["text"])
    if not texts and isinstance(parsed.get("output_text"), str):
        texts.append(parsed["output_text"])
    return "\n\n".join(text.strip() for text in texts if text.strip()).strip()


def _guess_mime_type(path: Path) -> str:
    overrides = {
        ".md": "text/markdown",
        ".rst": "text/plain",
        ".ipynb": "application/json",
        ".ts": "text/plain",
        ".tsx": "text/plain",
        ".js": "text/plain",
        ".py": "text/x-python",
        ".java": "text/x-java-source",
        ".c": "text/x-c",
        ".cpp": "text/x-c++",
        ".h": "text/x-c",
        ".hpp": "text/x-c++",
        ".go": "text/plain",
        ".rs": "text/plain",
        ".sql": "text/plain",
        ".scala": "text/plain",
        ".toml": "text/plain",
        ".yaml": "text/yaml",
        ".yml": "text/yaml",
    }
    return (
        overrides.get(path.suffix.lower())
        or mimetypes.guess_type(path.name)[0]
        or "application/octet-stream"
    )


def _openai_usage(parsed: dict, *, provider: str, model: str):
    usage = parsed.get("usage")
    if not isinstance(usage, dict):
        return None
    input_tokens = usage.get("input_tokens", usage.get("prompt_tokens"))
    output_tokens = usage.get("output_tokens", usage.get("completion_tokens"))
    total_tokens = usage.get("total_tokens")
    metadata: dict[str, object] = {}
    for key in ("input_tokens_details", "output_tokens_details"):
        if key in usage:
            metadata[key] = usage[key]
    return build_usage(
        provider=provider,
        model=model,
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        total_tokens=total_tokens,
        metadata=metadata,
    )
