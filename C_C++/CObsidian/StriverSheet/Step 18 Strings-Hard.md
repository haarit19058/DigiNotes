# Minimum number of bracket reversals needed to make an expression balanced

Approach:

- We can keep track of the balance of parentheses using two variables: open and close.

- Traverse through the string, and for each character:

- If it's an opening parenthesis '(', increment the open count.

- If it's a closing parenthesis ')':

- If there are open parentheses available (open > 0), decrement the open count.

- Otherwise, increment the close count.

- The total number of moves required to make the string valid would be equal to open + close.

```cpp
int minAddToMakeValid(string s) {
    int open = 0, close = 0;
    for(char c : s) {
        if(c == '(') {
            open++;
        } else {
            if(open > 0) {
                open--; // balance it with an open parenthesis
            } else {
                close++;
            }
        }
    }
    return open + close; // total moves required
}
```

# Count and Say
