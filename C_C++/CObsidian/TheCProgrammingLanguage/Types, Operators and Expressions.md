

- the first character must be a letter. The underscore  _  counts as a letter; it is sometimes useful for improving the readability of long variable names. 
- An integer constant like 1234 is an int. A long constant is written with a terminal l (ell) or L, as in 123456789L; an integer constant too big to fit into an int will also be taken as a long. Unsigned constants are written with a terminal u or U, and the suffix ul or UL indicates unsigned long.
- A constant expression is an expression that involves only constants. Such expressions may be evaluated at during compilation rather than run-time, and accordingly may be used in any place that a constant can occur, as in ```
```c
#define MAXLINE 1000 
char line[MAXLINE+1];
```


### String

- "hello, " "world" is equivalent to "hello, world" 
	This is useful for splitting up long strings across several source lines. Technically, a string constant is an array of characters. The internal representation of a string has a null character '\\0' at the end, so the physical storage required is one more than the number of characters written between the quotes. This representation means that there is no limit to how long a string can be, but programs must scan a string completely to determine its length. The standard library function strlen(s) returns the length of its character string argument s, excluding the terminal '\\0'. Here is our version:

```c
/* strlen: return length of s */
int strlen(char s[]) { 
	int i; while (s[i] != '\0') ++i;
	return i;
}
```

- Be careful to distinguish between a character constant and a string that contains a single character: 'x' is not the same as "x". The former is an integer, used to produce the numeric value of the letter x in the machine's character set. The latter is an array of characters that contains one character (the letter x) and a '\\0'.


### Enum
- There is one other kind of constant, the enumeration constant. An enumeration is a list of constant integer values,
- If not all values are specified, unspecified values continue the progression from the last specified value, as the second of these examples:
- Works like \#define that is it defines the value of constants but maybe inside of a function only.

```c
enum escapes { BELL = '\a', BACKSPACE = '\b', TAB = '\t', NEWLINE = '\n', VTAB = '\v', RETURN = '\r' }; 
enum months { JAN = 1, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC }; /* FEB = 2, MAR = 3, etc. */
```


### const
- The qualifier const can be applied to the declaration of any variable to specify that its value will not be changed.

### relational and logical operators
- The precedence of && is higher than that of ||, and both are lower than relational and equality operators, so expressions like
- i < lim-1 && (c=getchar()) != '\n' && c != EOF 
- need no extra parentheses. But since the precedence of != is higher than assignment, parentheses are needed in


### Type Conversions

function to convert string to integer
```c
 /* atoi:  convert s to integer */ 
   int atoi(char s[]) 
   { 
       int i, n; 
       n = 0; 
       for (i = 0; s[i] >= '0' && s[i] <= '9'; ++i) 
           n = 10 * n + (s[i] - '0'); 
       return n; 
   } 
```

Function to convert all uppercase to lowercase
```c
/* lower:  convert c to lower case; ASCII only */ 
   int lower(int c) 
   { 
       if (c >= 'A' && c <= 'Z') 
           return c + 'a' - 'A'; 
       else 
      }
```


type conversions depends on the architecture
- There is one subtle point about the conversion of characters to integers. The language does not specify whether variables of type char are signed or unsigned quantities. When a char is converted to an int, can it ever produce a negative integer? The answer varies from machine to machine, reflecting differences in architecture. On some machines a char whose leftmost bit is 1 will be converted to a negative integer (sign extension). On others, a char is promoted to an int by adding zeros at the left end, and thus is always positive.


Implicit conversions

If either operand is long double, convert the other to long double. 
- Otherwise, if either operand is double, convert the other to double. 
- Otherwise, if either operand is float, convert the other to float. 
- Otherwise, convert char and short to int. 
- Then, if either operand is long, convert the other to long.

- *Conversions take place across assignments; the value of the right side is converted to the type of the left, which is the type of the result.*


- Notice that floats in an expression are not automatically converted to double; this is a change from the original definition. In general, mathematical functions like those in will use double precision. The main reason for using float is to save storage in large arrays, or, less often, to save time on machines where double-precision arithmetic is particularly expensive.


- Conversion rules are more complicated when unsigned operands are involved. The problem is that comparisons between signed and unsigned values are machine-dependent, because they depend on the sizes of the various integer types. For example, suppose that int is 16 bits and long is 32 bits. Then -1L < 1U, because 1U, which is an unsigned int, is promoted to a signed long. But -1L > 1UL because -1L is promoted to unsigned long and thus appears to be a large positive number.
- Conversions take place across assignments; the value of the right side is converted to the type of the left, which is the type of the result. A character is converted to an integer, either by sign extension or not, as described above. Longer integers are converted to shorter ones or to chars by dropping the excess high-order bits. Thus in \# int i; char c; i = c; c = i;  \#  the value of c is unchanged. This is true whether or not sign extension is involved. Reversing the order of assignments might lose information, however.

- Since an argument of a function call is an expression, type conversion also takes place when arguments are passed to functions. In the absence of a function prototype, char and short become int, and float becomes double. This is why we have declared function arguments to be int and double even when the function is called with char and float.

#### How to explicitly convert
And it will convert according to the  rules of conversion
```c
(type name) expression

```



- The standard library includes a portable implementation of a pseudo-random number generator and a function for initializing the seed; the former illustrates a cast: 
-
```c
 unsigned long int next = 1; 
   /* rand:  return pseudo-random integer on 0..32767 */ 
   int rand(void) 
   { 
   } 
       next = next * 1103515245 + 12345; 
       return (unsigned int)(next/65536) % 32768; 
   /* srand:  set seed for rand() */ 
   void srand(unsigned int seed) 
   { 
       next = seed; 
   }
```


## Bitwise operators

- The bitwise AND operator & is often used to mask off some set of bits, for example n = n & 0177; sets to zero all but the low-order 7 bits of n.
- x = x | SET_ON; sets to one in x the bits that are set to one in SET_ON.
- The shift operators << and >> perform left and right shifts of their left operand by the number of bit positions given by the right operand, which must be non-negative. Thus x << 2 shifts the value of x by two positions, filling vacated bits with zero;

Basically it is highlighting the working of and or xor like how they interact with the  bits.  So there are chances that these logic may be useful in solving some of the question.



& bitwise AND 
| bitwise inclusive OR 
^ bitwise exclusive OR 
<<   left shift 
\>\> right shift 
\~ one's complement (unary)






## Conditional Expressions

- expr1 ? expr2 : expr3 --> shorthand of if else
- z = (a > b) ? a : b;   example. this is the max() function in python
- 