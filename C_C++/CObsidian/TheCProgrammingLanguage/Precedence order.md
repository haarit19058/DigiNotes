In C programming, operators have different precedence levels, which determine the order in which they are evaluated in an expression. Operators with higher precedence are evaluated before operators with lower precedence. If operators have the same precedence, their associativity determines the order of evaluation (left-to-right or right-to-left).

Here's a list of operators in C programming, sorted by precedence (from highest to lowest):

1. **Postfix Operators**: `() [] -> . ++ --`
2. **Unary Operators**: `+ - ! ~ ++ -- * & (type) sizeof`
3. **Multiplicative Operators**: `* / %`
4. **Additive Operators**: `+ -`
5. **Shift Operators**: `<< >>`
6. **Relational Operators**: `< <= > >=`
7. **Equality Operators**: `== !=`
8. **Bitwise AND Operator**: `&`
9. **Bitwise XOR Operator**: `^`
10. **Bitwise OR Operator**: `|`
11. **Logical AND Operator**: `&&`
12. **Logical OR Operator**: `||`
13. **Conditional Operator**: `? :`
14. **Assignment Operators**: `= += -= *= /= %= &= ^= |= <<= >>=`
15. **Comma Operator**: `,`

Keep in mind that parentheses (`()`) can be used to override the default precedence and enforce the evaluation order you desire.

Additionally, within a specific category of operators, such as unary operators or binary operators, the precedence and associativity of individual operators are as follows:

- **Unary Operators** (from right to left):
  - `sizeof`
  - `++ --`
  - `+ - ! ~`
  - `* &`

- **Binary Operators** (left-to-right):
  - `* / %`
  - `+ -`
  - `<< >>`
  - `< <= > >=`
  - `== !=`
  - `&`
  - `^`
  - `|`
  - `&&`
  - `||`
  - `? :`
  - `= += -= *= /= %= &= ^= |= <<= >>=`

Understanding operator precedence and associativity is crucial for writing correct and efficient C code. It helps you predict how expressions will be evaluated and can prevent errors or unexpected behavior in your programs.