---
page_id: "y1s1-cs1101s-lecture-11"
title: "Lecture 11: Metalinguistic Abstraction"
page_type: "concept"
page_kind: "topic"
module_id: "y1s1-cs1101s"
parent_page_id: "y1s1-cs1101s-hub"
batch_id: "y1s1-cs1101s-20260412t081115z"
status: "canonical"
summary: "Lecture 11: Metalinguistic Abstraction consolidates the numbered lecture materials for this module. Lecture L11, \"Metalinguistic Abstraction,\" was presented by Boyd Anderson on October 26, 2022, for CS1101S: Programmi..."
aliases:
tags:
  - "course"
  - "cs1101s"
  - "topic"
  - "y1s1"
related:
source_refs:
  - "cs1101s-lecture-lecture-l11-view-pdf#section-1"
  - "cs1101s-lecture-lecture-l11-view-pdf#section-2"
  - "cs1101s-lecture-lecture-l11-view-pdf#section-3"
topics:
  - "evaluator"
  - "function"
  - "environment"
  - "source"
  - "functions"
  - "language"
  - "week"
  - "expressions"
  - "lecture"
  - "metalinguistic"
source_count: 1
lecture_number: 11
last_compiled_at: "2026-04-12T08:44:47+00:00"
---
# Lecture 11: Metalinguistic Abstraction

Lecture 11: Metalinguistic Abstraction

Metalinguistic abstraction is a core concept in computer science, emphasizing that a programming language's evaluator is, at its heart, a program itself [source:cs1101s-lecture-lecture-l11-view-pdf#section-1]. This lecture, presented by Boyd Anderson on October 26, 2022, for CS1101S: Programming Methodology, delves into understanding the environment model by programming an evaluator for a simplified version of Source [source:cs1101s-lecture-lecture-l11-view-pdf#section-1, cs1101s-lecture-lecture-l11-view-pdf#section-3].

---

### Course Overview and Logistics

CS1101S is structured into four main units:
*   **Unit 1: Functions** (Textbook Chapter 1) - Focuses on functional abstraction, static program reading, the substitution model, and applications like Runes and curves [source:cs1101s-lecture-lecture-l11-view-pdf#section-2].
*   **Unit 2: Data** (Textbook Chapter 2) - Covers data structures such as pairs, lists, and trees; includes searching and sorting in these structures, with applications in sound processing [source:cs1101s-lecture-lecture-l11-view-pdf#section-2].
*   **Unit 3: State** (Parts of Textbook Chapter 3) - Introduces stateful abstractions, arrays, loops, searching, sorting, and reading programs using the [[lecture-08: Environment Model|environment model]] [source:cs1101s-lecture-lecture-l11-view-pdf#section-3]]. Applications include robots and video processing [source:cs1101s-lecture-lecture-l11-view-pdf#section-3].
*   **Unit 4: Beyond** (Parts of Textbook Chapters 3 and 4) - Explores streams and the concept of metalinguistic abstraction, specifically understanding the environment model through programming it [source:cs1101s-lecture-lecture-l11-view-pdf#section-3].

**Assessment and Future Lectures**:
*   Lecture L11, "Metalinguistic Abstraction," is delivered in Week 11 [source:cs1101s-lecture-lecture-l11-view-pdf#section-1, cs1101s-lecture-lecture-l11-view-pdf#section-5].
*   Reading Assessment 2 is also scheduled for Week 11, replacing B11 [source:cs1101s-lecture-lecture-l11-view-pdf#section-6].
*   Week 12 will feature L12A (Logic Programming), L12B (Concurrent Programming), L12C (Register Machines), and L12D (Explicit-Control Evaluator), along with a brief B12 on "Power of Simplicity; Tips and Tricks" [source:cs1101s-lecture-lecture-l11-view-pdf#section-7, cs1101s-lecture-lecture-l11-view-pdf#section-8].
*   Week 13 includes a Practical Assessment (replacing L13) and a Final Brief (B13) [source:cs1101s-lecture-lecture-l11-view-pdf#section-9].
*   All material up to and including Lecture L11 is assessed. Lectures L12A, L12B, L12C, and L12D are *not* assessed [source:cs1101s-lecture-lecture-l11-view-pdf#section-10].

**CP3108: A project module on “Source Academy”**:
*   This is a 2/4 MC project module for Sem 2 AY2022/23 [source:cs1101s-lecture-lecture-l11-view-pdf#section-11].
*   Application period: Friday Week 11 to Friday Week 13 (11/11/2022 to 9/1/2023 for "Avenger recruitment") [source:cs1101s-lecture-lecture-l11-view-pdf#section-12, cs1101s-lecture-lecture-l11-view-pdf#section-16].
*   Interviews: 14/11–2/12/2022 for CP3108, and throughout Sem 2 for Avenger recruitment [source:cs1101s-lecture-lecture-l11-view-pdf#section-13, cs1101s-lecture-lecture-l11-view-pdf#section-17].
*   Scope: Topics listed in the application form, with further announcements to follow [source:cs1101s-lecture-lecture-l11-view-pdf#section-14].
*   Selection: First round before end of Sem 2; waiting list [source:cs1101s-lecture-lecture-l11-view-pdf#section-18].

### On Metacircular Evaluators

**Why a Metacircular Evaluator?**
Programming is fundamentally about communicating computational processes [source:cs1101s-lecture-lecture-l11-view-pdf#section-22]. By now, we are proficient in using Source to express these processes [source:cs1101s-lecture-lecture-l11-view-pdf#section-24]. The [[lecture-08: Environment Model|environment model]] describes a computational process (with frames and environments) that unfolds whenever any program runs [source:cs1101s-lecture-lecture-l11-view-pdf#section-26]. The goal of this lecture is to use Source itself to better understand the environment model [source:cs1101s-lecture-lecture-l11-view-pdf#section-27].

**Importance of Metalinguistic Abstraction**
The most fundamental idea in programming is that "the evaluator, which determines the meaning of statements and expressions in a programming language, is just another program" [source:cs1101s-lecture-lecture-l11-view-pdf#section-29].
Examples illustrating this idea include:
*   The symbolic evaluator/differentiator from [[lecture-06: Sorting and Symbolic Processing|Lecture L6]] [source:cs1101s-lecture-lecture-l11-view-pdf#section-30].
*   Source Academy, where your programs run [source:cs1101s-lecture-lecture-l11-view-pdf#section-31].
*   Firmware uploaded to EV3 LEGO Mindstorms computers [source:cs1101s-lecture-lecture-l11-view-pdf#section-32].
*   The environment visualizer [source:cs1101s-lecture-lecture-l11-view-pdf#section-33].

Gerald Jay Sussman, in a CS1101S Guest Lecture (2020/21, 25:35), famously called the "Eval/Apply Interpreter" "the most beautiful program ever written" [source:cs1101s-lecture-lecture-l11-view-pdf#section-34]. Its beauty lies in conveying deep insights in just a few lines, similar to Maxwell's Equations in electromagnetism [source:cs1101s-lecture-lecture-l11-view-pdf#section-35]. This concept is central to SICP (Structure and Interpretation of Computer Programs), where "Eval/Apply" is prominently featured on the cover [source:cs1101s-lecture-lecture-l11-view-pdf#section-38].

A Metacircular Evaluator (MCE) functions as a language processor. When `factorial` is run in Source Academy, it executes through multiple layers of Source and x86-64. An MCE for `factorial` would similarly involve layers of `factorial`, Source, and x86-64, but the interpreter for Source is itself written in Source [source:cs1101s-lecture-lecture-l11-view-pdf#section-39].

**Task and Objective**:
The task is to write an evaluator in Source that can execute programs also written in Source [source:cs1101s-lecture-lecture-l11-view-pdf#section-41]. While there's no practical use for such a metacircular evaluator (as you need a working Source implementation to run it), the objective is to gain new insights into the language and a deeper understanding of the environment model by building it [source:cs1101s-lecture-lecture-l11-view-pdf#section-43, cs1101s-lecture-lecture-l11-view-pdf#section-46].

**First step for evaluator: Parsing**
The process of transforming a source string into an executable form involves several stages [source:cs1101s-lecture-lecture-l11-view-pdf#section-47]:
1.  **Lexical Analysis (Create Tokens)**: Input characters are split into meaningful symbols called *tokens*, defined using regular expressions. For example, `"8 + 34;"` is tokenized into `8`, `+`, `34`, `;` [source:cs1101s-lecture-lecture-l11-view-pdf#section-49, cs1101s-lecture-lecture-l11-view-pdf#section-50].
2.  **Syntactic Analysis (Create Tree)**: This stage, known as parsing, checks that the tokens form allowable components and produces a symbolic representation of the program, known as a *syntax tree* [source:cs1101s-lecture-lecture-l11-view-pdf#section-52, cs1101s-lecture-lecture-l11-view-pdf#section-53].
    *   Source provides `parse(string)` to generate a syntax tree as a Source list [source:cs1101s-lecture-lecture-l11-view-pdf#section-55].
    *   For example, `parse("8 + 34;")` results in `list("binary_operator_combination", "+", list("literal", 8), list("literal", 34))` [source:cs1101s-lecture-lecture-l11-view-pdf#section-55].
3.  **Compiler, Interpreter or Translator**: The syntax tree is then processed to produce an output [source:cs1101s-lecture-lecture-l11-view-pdf#section-47].

**Scope of L11**:
This lecture focuses on building an evaluator for a simplified subset of Source §1 without the `return` statement. This involves a sequence of evaluators describing the structure and interpretation of this simplified language, starting with a "Calculator language" [source:cs1101s-lecture-lecture-l11-view-pdf#section-56].
It *does not* include: `return`, pairs, assignment, loops, or lazy evaluation [source:cs1101s-lecture-lecture-l11-view-pdf#section-57].
**Reading**: SICP JS 4.1: L11 [source:cs1101s-lecture-lecture-l11-view-pdf#section-58].

### Calculator Language

The calculator language is defined using Backus-Naur Form (BNF) [source:cs1101s-lecture-lecture-l11-view-pdf#section-59].

**Syntax in BNF**:
*   `stmt ::= expr ;` (expression statement)
*   `expr ::= expr bin-op expr` (binary operator combination)
    *   `| number` (number expression)
    *   `| ( expr )` (parenthesized expression)
*   `bin-op ::= + | - | * | /` (binary operator) [source:cs1101s-lecture-lecture-l11-view-pdf#section-60].

**Parsing the calculator language**:
For a program like `1.4 + 2.3 / 70.4;`, parsing produces a syntax tree.
Example: `parse("1.4 + 2.3 / 70.4;")` returns:
```
list("binary_operator_combination",
     "+",
     list("literal", 1.4),
     list("binary_operator_combination", "/",
          list("literal", 2.3),
          list("literal", 70.4)))
```
[source:cs1101s-lecture-lecture-l11-view-pdf#section-62]

**Syntax Predicates and Selectors for Literals**:
*   `is_literal(comp)`: Checks if a component is a literal (e.g., `list("literal", 38)`). It uses `is_tagged_list(comp, "literal")` [source:cs1101s-lecture-lecture-l11-view-pdf#section-63].
*   `literal_value(comp)`: Extracts the value from a literal component (e.g., `38` from `list("literal", 38)`). It uses `head(tail(comp))` [source:cs1101s-lecture-lecture-l11-view-pdf#section-63].

**Syntax Predicates and Selectors for Operator Combinations**:
For `parse("... 2.3 + 70.4 ...")` it results in `list("binary_operator_combination", "+", list("literal", 2.3), list("literal", 70.4))` [source:cs1101s-lecture-lecture-l11-view-pdf#section-64].
*   `is_operator_combination(comp)`: Checks if a component is a binary operator combination. Uses `is_tagged_list(comp, "binary_operator_combination")` [source:cs1101s-lecture-lecture-l11-view-pdf#section-65].
*   `op_comb_symbol(comp)`: Selects the operator symbol (e.g., `"+"`) using `list_ref(comp, 1)` [source:cs1101s-lecture-lecture-l11-view-pdf#section-65].
*   `op_first_operand(comp)`: Selects the first operand using `list_ref(comp, 2)` [source:cs1101s-lecture-lecture-l11-view-pdf#section-65].
*   `op_second_operand(comp)`: Selects the second operand using `list_ref(comp, 3)` [source:cs1101s-lecture-lecture-l11-view-pdf#section-65].

**Evaluating the calculator language**:
The `evaluate` function handles literals and operator combinations [source:cs1101s-lecture-lecture-l11-view-pdf#section-66]:
```javascript
function evaluate(expr) {
    return is_literal(expr)
           ? literal_value(expr)
           : is_operator_combination(expr)
           ? apply(op_comb_operator_symbol(expr),
                   list_of_values(
                       list(op_comb_first_operand(expr),
                            op_comb_second_operand(expr))))
           : error(expr, "Unknown expression:");
}
```
*   `list_of_values(exprs)`: Evaluates a list of expressions by mapping `evaluate` over them [source:cs1101s-lecture-lecture-l11-view-pdf#section-67].
    ```javascript
    function list_of_values(exprs) {
        return map(evaluate, exprs);
    }
    ```
*   `apply(operator, operands)`: Performs the arithmetic operation based on the operator symbol [source:cs1101s-lecture-lecture-l11-view-pdf#section-68].
    ```javascript
    function apply(operator, operands) {
        const first_op = head(operands);
        const second_op = head(tail(operands));
        return operator === "+"
               ? first_op + second_op
               : operator === "-"
               ? first_op - second_op
               : operator === "*"
               ? first_op * second_op
               : operator === "/"
               ? first_op / second_op
               : error();
    }
    ```

### Adding Booleans, Conditionals, and Sequences

**Syntax in BNF**:
The language is extended to include boolean literals, conditional expressions, and statement sequences [source:cs1101s-lecture-lecture-l11-view-pdf#section-69].
*   `stmt ::= ... | stmt1 ... stmtn` (statement sequence)
*   `expr ::= ... | true | false` (boolean literals)
    *   `| expr1 ? expr2 : expr3` (conditional expression) [source:cs1101s-lecture-lecture-l11-view-pdf#section-70].

**Evaluating the language (updated `evaluate` function)**:
The `evaluate` function is extended to handle conditionals and sequences [source:cs1101s-lecture-lecture-l11-view-pdf#section-71]:
```javascript
function evaluate(comp) {
    return ... // handling literals, operator comb
           : is_conditional(comp)
           ? eval_conditional(comp)
           : is_sequence(comp)
           ? eval_sequence(sequence_statements(comp))
           : error(comp, "Unknown component:");
}
```

**Parsing Conditionals**:
Example: `parse("true ? 42 : 17;")` returns:
```
list("conditional_expression",
     list("literal", true),
     list("literal", 42),
     list("literal", 17))
```
[source:cs1101s-lecture-lecture-l11-view-pdf#section-72]
*   **Syntax predicate**: `is_conditional`
*   **Selectors**: `cond_expr_pred`, `cond_expr_cons`, `cond_expr_alt` [source:cs1101s-lecture-lecture-l11-view-pdf#section-73].

**Evaluating Conditionals**:
```javascript
function eval_conditional(comp) {
    return is_truthy(evaluate(cond_expr_pred(comp)))
           ? evaluate(cond_expr_cons(comp))
           : evaluate(cond_expr_alt(comp));
}

const is_truthy = x => is_boolean(x) ? x : error();
```
[source:cs1101s-lecture-lecture-l11-view-pdf#section-74, cs1101s-lecture-lecture-l11-view-pdf#section-75]
This approach explains conditionals in the interpreted language using conditional expressions in the interpreting language, which can be seen as either a "cop-out" or a "stroke of genius" [source:cs1101s-lecture-lecture-l11-view-pdf#section-76, cs1101s-lecture-lecture-l11-view-pdf#section-77].

**Parsing Sequences**:
Example: `parse("1; 2; 3;")` returns:
```
list("sequence",
     list(list("literal", 1),
          list("literal", 2),
          list("literal", 3)))
```
[source:cs1101s-lecture-lecture-l11-view-pdf#section-78]
*   **Syntax predicate**: `is_sequence`
*   **Selectors**: `sequence_statements`, `first_statement`, `rest_statements`
*   **Additional predicates**: `is_empty_sequence`, `is_last_statement` [source:cs1101s-lecture-lecture-l11-view-pdf#section-79].

**Evaluating Sequences**:
The `eval_sequence` function processes a list of statements iteratively [source:cs1101s-lecture-lecture-l11-view-pdf#section-80].
```javascript
function eval_sequence(stmts) {
    if (is_empty_sequence(stmts)) {
        return undefined;
    } else if (is_last_statement(stmts)) {
        return evaluate(first_statement(stmts));
    } else {
        const ignore = evaluate(first_statement(stmts)); // evaluate and discard result
        return eval_sequence(rest_statements(stmts));
    }
}
```
[source:cs1101s-lecture-lecture-l11-view-pdf#section-80]
Similar to conditionals, sequences in the interpreted language are explained using sequences in the interpreting language [source:cs1101s-lecture-lecture-l11-view-pdf#section-81].

### Adding Blocks and Declarations

**Syntax in BNF**:
Extensions for blocks and constant declarations [source:cs1101s-lecture-lecture-l11-view-pdf#section-82].
*   `stmt ::= ... | { stmt }` (block)
    *   `| const name = expr ;` (constant declaration)
*   `expr ::= ... | name` (name expression) [source:cs1101s-lecture-lecture-l11-view-pdf#section-83].

**Evaluating the language (updated `evaluate` function)**:
The `evaluate` function is further extended to handle names, blocks, and declarations [source:cs1101s-lecture-lecture-l11-view-pdf#section-84].
```javascript
function evaluate(comp, env) { // env parameter added
    return ... // handling literals, operator comb, conditionals, sequences
           : is_name(comp)
           ? lookup_symbol_value(symbol_of_name(comp), env)
           : is_block(comp)
           ? eval_block(comp, env)
           : is_declaration(comp)
           ? eval_declaration(comp, env)
           : error(comp, "Unknown component:");
}
```

**Frames and Environments**:
*   An **environment** is a sequence of **frames** [source:cs1101s-lecture-lecture-l11-view-pdf#section-85].
*   A **frame** is a data structure that maps symbols (names) to values. It's represented as a pair of lists: one for names, one for values [source:cs1101s-lecture-lecture-l11-view-pdf#section-85].
    ```javascript
    function make_frame(names, values) {
        return pair(names, values);
    }
    const frame_names = head;
    const frame_values = tail;
    ```
*   `extend_environment(ns, vs, e)`: Creates a new environment by adding a new frame (binding names `ns` to values `vs`) to an existing environment `e` [source:cs1101s-lecture-lecture-l11-view-pdf#section-85].
    ```javascript
    function extend_environment(ns, vs, e) {
        return pair(make_frame(ns, vs), e);
    }
    ```
*   `the_empty_environment`: Represented as `null` [source:cs1101s-lecture-lecture-l11-view-pdf#section-85].
*   `the_global_environment`: Initially `the_empty_environment`, then extended with primitive functions [source:cs1101s-lecture-lecture-l11-view-pdf#section-85].

**Evaluating Blocks**:
When a block is evaluated, a new environment is created for its local declarations [source:cs1101s-lecture-lecture-l11-view-pdf#section-86].
```javascript
function eval_block(component, env) {
    const body = block_body(component); // The sequence of statements in the block
    const locals = scan_out_declarations(body); // Names declared within the block
    const unassigneds = list_of_unassigned(locals); // Placeholder values for local variables
    return evaluate(body,
                    extend_environment(locals,
                                       unassigneds,
                                       env));
}
```
*   `list_of_unassigned(symbols)`: Creates a list of placeholder values (e.g., `"*unassigned*"`) for new local variables [source:cs1101s-lecture-lecture-l11-view-pdf#section-87].
*   `scan_out_declarations(comp)`: Recursively scans a component (like a sequence of statements) to extract the symbols declared within it [source:cs1101s-lecture-lecture-l11-view-pdf#section-88].

**Evaluating Declarations**:
`eval_declaration` assigns a value to a declared symbol within the current frame [source:cs1101s-lecture-lecture-l11-view-pdf#section-89].
```javascript
function eval_declaration(comp, env) {
    assign_symbol_value(
        declaration_symbol(comp),
        evaluate(declaration_value_expression(comp),
                 env),
        env);
    return undefined; // Declarations don't return a value
}
```

**Assigning a Name to a Value**:
`assign_symbol_value(symbol, val, env)`: Searches for the symbol in the environment and updates its value in the first frame where it's found [source:cs1101s-lecture-lecture-l11-view-pdf#section-90].
```javascript
function assign_symbol_value(symbol, val, env) {
    function scan_write(symbols, vals) {
        return symbol === head(symbols)
               ? set_head(vals, val) // Update value in the list
               : scan_write(tail(symbols), tail(vals));
    }
    const frame = first_frame(env); // Get the first frame
    return scan_write(frame_symbols(frame),
                      frame_values(frame));
}
```
This function mutates the `vals` list within the frame using `set_head`.

**Environment Functions**:
*   `first_frame(env)`: Returns the first frame of an environment (`head(env)`) [source:cs1101s-lecture-lecture-l11-view-pdf#section-91].
*   `enclosing_environment(env)`: Returns the rest of the environment (the parent environment) (`tail(env)`) [source:cs1101s-lecture-lecture-l11-view-pdf#section-91].
*   `is_empty_environment(env)`: Checks if an environment is empty (`is_null(env)`) [source:cs1101s-lecture-lecture-l11-view-pdf#section-91].

**Looking up a Symbol**:
`lookup_symbol_value(name, env)`: Searches for a symbol's value through the frames in the environment [source:cs1101s-lecture-lecture-l11-view-pdf#section-92].
```javascript
function lookup_symbol_value(name, env) {
    function env_loop(env) {
        function scan_read(names, vals) { /* ... finds value associated with name in current frame */ }
        if (is_empty_environment(env)) {
            error(name, "Unbound name:");
        } else {
            const frame = first_frame(env);
            const value = scan_read(frame_names(frame), frame_values(frame));
            if (value === "*unassigned*") {
                error(name, "Used before declared:");
            } else {
                return value;
            }
        }
    }
    return env_loop(env);
}
```
[source:cs1101s-lecture-lecture-l11-view-pdf#section-92]

### Adding Compound Functions (but no return)

**Syntax in BNF**:
Extensions for function declarations, lambda expressions, and function applications [source:cs1101s-lecture-lecture-l11-view-pdf#section-93].
*   `stmt ::= ... | function name ( params ) block` (function declaration)
*   `expr ::= ... | expr( expr1 , ... , exprn)` (function application)
    *   `| params => block` (lambda expression) [source:cs1101s-lecture-lecture-l11-view-pdf#section-94].

**Evaluating Compound Functions (updated `evaluate` function)**:
The `evaluate` function is extended to handle lambda expressions, function declarations, and function applications [source:cs1101s-lecture-lecture-l11-view-pdf#section-95].
```javascript
function evaluate(comp, env) {
    return ... // existing cases
           : is_lambda_expression(comp)
           ? make_function(lambda_parameter_symbols(comp),
                           lambda_body(comp), env)
           : is_function_declaration(comp)
           ? evaluate(function_decl_to_constant_decl(comp),
                      env)
           : is_application(comp)
           ? apply(evaluate(function_expression(comp), env),
                   list_of_values(arg_expressions(comp), env))
           : error(comp, "Unknown component:");
}
```

**Function Objects**:
A compound function object is represented as a list containing its parameters, body, and the environment in which it was created (the *enclosing environment*) [source:cs1101s-lecture-lecture-l11-view-pdf#section-96].
```javascript
function make_function(parameters, body, env) {
    return list("compound_function", parameters, body, env);
}
```
There are also predicates like `is_compound_function`, `function_parameters`, `function_body`, and `function_environment` to interact with these objects.

**Transformation of Function Declaration**:
A function declaration is transformed into a constant declaration where the value assigned is a lambda expression [source:cs1101s-lecture-lecture-l11-view-pdf#section-97].
```javascript
// function fact(n) { n === 1 ? 1 : n * fact(n - 1); }
// becomes
// const fact = n => { n===1 ? 1 : n * fact(n - 1); };

function function_decl_to_constant_decl(comp) {
    return make_constant_declaration(
        function_declaration_name(comp),
        make_lambda_expression(
            function_declaration_parameters(comp),
            function_declaration_body(comp)));
}
```

**Function Application**:
The `apply` function is updated to handle both primitive and compound functions [source:cs1101s-lecture-lecture-l11-view-pdf#section-98].
```javascript
function apply(fun, args) {
    return is_primitive_function(fun)
           ? apply_primitive_function(fun, args)
           : is_compound_function(fun)
           ? evaluate(function_body(fun), // Evaluate the function body
                      extend_environment( // In a new environment
                          function_parameters(fun),
                          args,
                          function_environment(fun))) // Extended from the function's environment
           : error(fun, "Unknown function type:");
}
```

**Primitive Functions**:
Primitive functions are pre-defined functions (like `math_sin` or arithmetic operators) provided by the underlying language [source:cs1101s-lecture-lecture-l11-view-pdf#section-99, cs1101s-lecture-lecture-l11-view-pdf#section-100]. They are stored as a list of pairs (name, implementation) in the global environment [source:cs1101s-lecture-lecture-l11-view-pdf#section-101].
```javascript
const primitive_functions =
    list(pair("math_sin", math_sin),
         // ...
         pair("+", (x, y) => x + y),
         pair("-", (x, y) => x - y),
         // ...
    );

function setup_environment() {
    // ... adds primitive_functions to a new frame ...
}
const the_global_environment = setup_environment();
```

**Applying Primitive Functions**:
`apply_primitive_function(fun, arglist)` executes the underlying JavaScript implementation of the primitive function [source:cs1101s-lecture-lecture-l11-view-pdf#section-102].
```javascript
function apply_primitive_function(fun, arglist) {
    return apply_in_underlying_javascript(
               primitive_implementation(fun),
               arglist);
}
```

### Summary

The metacircular evaluator is a powerful tool for communicating the computational process known as the [[lecture-08: Environment Model|environment model]] [source:cs1101s-lecture-lecture-l11-view-pdf#section-104].
*   It clarifies frames and environments as data types [source:cs1101s-lecture-lecture-l11-view-pdf#section-105].
*   Environments are demystified as simply lists of pairs [source:cs1101s-lecture-lecture-l11-view-pdf#section-106].
*   Function objects are demystified as lists themselves [source:cs1101s-lecture-lecture-l11-view-pdf#section-107].
*   The entire process operates as an `evaluate—apply` loop [source:cs1101s-lecture-lecture-l11-view-pdf#section-108].
