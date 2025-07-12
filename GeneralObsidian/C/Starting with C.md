
\# Pending Excercise from 1-16 Continue it if free


First Program
```c++
\#include <stdio.h> 

int main()

{

    printf("hello, world\n");

    return 0;

}
```


%% compile it with the command --> cc hello.c
it compiles the c file and makes an executable file named hello.out
type hello.out in terminal to run the file %%expired


gcc helloworld.c will create  a file named a.exe
gcc -o hello helloworld.c      a file named helloworld.exe


### .out file is an older version of executable file. Nowadays most commaon is exe file

%#include tells the compiler to include information about the standard input/output library. 

printf is a library function that prints output, in this case the string of characters between the quotes. It won't create a new line by itself.

\\n is escape code 



## Note :Error I am getting.

Error I am getting.

passing argument 1 of 'printf' makes pointer from integer without a cast 
Here

```c
printf(c);
```

you pass the character instead of a format string as the first argument to `printf()`. It should be

```c
printf("%c", c);
```

or alternatively

```c
putchar(c);
```


## Note 2: There are  a lot many things to see for printf()
### from book
- Width and precision may be omitted from a specification: %6f says that the number is to be at least six characters wide; %.2f specifies two characters after the decimal point, but the width is not constrained; and %f merely says to print the number as floating point.
- %d print as decimal integer
- %6d %f print as decimal integer, at least 6 characters wide print as floating point
- %6f %.2f print as floating point, at least 6 characters wide print as floating point, 2 characters after decimal point 
- %6.2f print as floating point, at least 6 wide and 2 after decimal point

- 










[See Here](https://www.geeksforgeeks.org/printf-in-c/)  Geeks for Geeks.

Specifier-memorize
Width- see
Precision- upto what digits
Length- length in memory

Example1 

```c 
// C program to print a variable
#include <stdio.h>
int main()
{
	int num1 = 99;
	int num2 = 1;
	printf("The sum of %d and %d is %d\n", num1, num2,
		num1 + num2);
	return 0;
}


//OutPut
//The sum of 99 and 1 is 100
```

Example 2
```c
// C program to illustrate the use of printf with width
// specifier
#include <stdio.h>
int main()
{
	// number to be printed
	int num = 123456;
	// printing the num with 10 width and getting the
	// printed characters in char_printed
	printf("Printing num with width 10: ");
	int chars_printed = printf("%10d", num);
	printf("\nNumber of characters printed: %d",
		chars_printed);

	// specifying with using other method
	printf("\nPrinting num with width 3: ");
	chars_printed = printf("%*d", 3, num);
	printf("\nNumber of characters printed: %d",
		chars_printed);

	return 0;
}

//OutPut
//Printing num with width 10:     123456
//Number of characters printed: 10
//Printing num with width 3: 123456
//Number of characters printed: 6
```

Example 3
```c
// C program to illustrate the use of precision
// sub-specifier
#include <stdio.h>

int main()
{
	int num = 2451;
	float dec = 12.45126;
	char* str = "GeeksforGeeks";

	// precision for integral data
	printf("For integers: %.10d\n", num);
	// precision for numbers with decimal points
	printf("For floats: %.2f\n", dec);
	// for strings
	printf("For strings: %.5s", str);

	return 0;
}

//Output
//For integers: 0000002451
//For floats: 12.45
//For strings: Geeks

```


Example 4
```c
// C program to illustrate the length modifier
#include <stdio.h>

int main()
{
	long var = 3000000000;
	// printing var using %d
	printf("Using %%d: %d", var);
	// printing var using %ld
	printf("\nUsing %%ld: %ld", var);

	return 0;
}


//Output
//Using %d: -1294967296
//Using %ld: 3000000000
```









































Comments Multiline /**/ and single line //


Program for Temperature..................................................................................................................................................................................................................................................................
###### see code
```c
  

#include <stdio.h>

   /* print Fahrenheit-Celsius table

       for fahr = 0, 20, ..., 300 */

   main()

   {

     int fahr, celsius;

     int lower, upper, step;

     lower = 0;      /* lower limit of temperature scale */

     upper = 300;    /* upper limit */

     step = 20;      /* step size */

     fahr = lower;

     while (fahr <= upper) {

         celsius = 5 * (fahr-32) / 9;

         printf("%d\t%d\n", fahr, celsius);

         fahr = fahr + step;

     }

   }
```


Baki to sab normal wala hi hai.




char  13 character - a single byte
short   short integer
long long   integer
double  double-precision floating point



While and for loops



## Temperature conversion

```c
#include <stdio.h>

/* print Fahrenheit-Celsius table

    for fahr = 0, 20, ..., 300; floating-point version */

int main()

{

    float fahr, celsius;

    float lower, upper, step;

    lower = 0;      /* lower limit of temperatuire scale */

    upper = 300;    /* upper limit */

    step = 20;      /* step size */

    fahr = lower;

    while (fahr <= upper) {

        celsius = (5.0/9.0) * (fahr-32.0);

        printf("%3.0f %6.1f\n", fahr, celsius);

        fahr = fahr + step;

    }

}
```

- The printf conversion specification %3.0f says that a floating-point number (here fahr) is to be printed at least three characters wide, with no decimal point and no fraction digits. %6.1f describes another number (celsius) that is to be printed at least six characters wide, with 1 digit after the decimal point.
- 



# Notes

Write code in a very good manner like maintain indents, make it readable , use variables that are self explanatory and use blanks around operators to make them good looking.

We recommend writing only one statement per line, and using blanks around operators to clarify grouping. The position of braces is less important, although people hold passionate beliefs.

If an arithmetic operator has integer operands, an integer operation is performed. If an arithmetic operator has one floating-point operand and one integer operand, however, the integer will be converted to floating point before the operation is done.



# More of it 
## The for statement

syntax
```c
for (fahr = 0; fahr <= 300; fahr = fahr + 20) {
printf("%3d %6.1f\n", fahr, (5.0/9.0)*(fahr-32));
}
```


## Symbolic constants

\#define name replacement list Thereafter, any occurrence of name (not in quotes and not part of another name) will be replaced by the corresponding replacement text. The name has the same form as a variable name: a sequence of letters and digits that begins with a letter. The replacement text can be any sequence of characters; it is not limited to numbers.

```c
#include <stdio.h>

   #define LOWER  0     /* lower limit of table */

   #define UPPER  300   /* upper limit */

   #define STEP   20    /* step size */

   /* print Fahrenheit-Celsius table */

   main()

   {

       int fahr;

       for (fahr = LOWER; fahr <= UPPER; fahr = fahr + STEP)

           printf("%3d %6.1f\n", fahr, (5.0/9.0)*(fahr-32));

   }
```

Notice that there is no semicolon at the end of a \#define line.







## Character input and output

- Text input or output, regardless of where it originates or where it goes to, is dealt with as streams of characters. A text stream is a sequence of characters divided into lines; each line consists of zero or more characters followed by a newline character.
- The standard library provides several functions for reading or writing one character at a time, of which getchar and putchar are the simplest. Each time it is called, getchar reads the next input character from a text stream and returns that as its value. That is, after

```c
c=getchar()
putchar(c)
```


```c
#include <stdio.h>

   /* copy input to output; 1st version  */

   int main()
   {  
       int c;
       c = getchar();
       while (c != EOF) {
           putchar(c);
           c = getchar();
       }
}
```

- with reference to above code.
- We used int for a subtle but important reason. The problem is distinguishing the end of input from valid data. The solution is that getchar returns a distinctive value when there is no more input, a value that cannot be confused with any real character. This value is called EOF, for "end of file''. We must declare c to be a type big enough to hold any value that getchar returns. We can't use char since c must be big enough to hold EOF in addition to any possible char. Therefore we use int.
- EOF is an integer defined in , but the specific numeric value doesn't matter as long as it is not the same as any char value.

another method
```c
 #include <stdio.h> 
   /* copy input to output; 2nd version  */ 
   main() 
   { 
       int c; 
       while ((c = getchar()) != EOF) 
           putchar(c);
   }
```

- The parentheses around the assignment, within the condition are necessary. The precedence of != is higher than that of =, which means that in the absence of parentheses the relational test != would be done before the assignment =. So the statement c = getchar() != EOF is equivalent to           c = (getchar() != EOF) . This has the undesired effect of setting c to 0 or 1, depending on whether or not the call of getchar returned end of file.
-
program to print value of eof.

```c
#include <stdio.h>

  

int main() {

    int eofValue = EOF;

    printf("The value of EOF is: %d\n", eofValue);

    return 0;

}
```






## Character Counting

```c
#include <stdio.h> 
   /* count characters in input; 1st version */ 
   main() 
   { 
       long nc; 
       nc = 0; 
       while (getchar() != EOF) 
           ++nc; 
       printf("%ld\n", nc); 
	}
```




## Line Counting

```c
#include <stdio.h> 
   /* count lines in input */ 
   main() 
   { 
       int c, nl; 
       nl = 0; 
       while ((c = getchar()) != EOF) 
           if (c == '\n') 
               ++nl; 
       printf("%d\n", nl); 

   }
```


## Printing single space

```c
#include <stdio.h>

int main() {
    int c;
    int lastCharWasSpace = 0; // Flag to track if the last character was a space

    printf("Enter some text (press Ctrl+D to end input):\n");

    while ((c = getchar()) != EOF) {
        if (c == ' ') {
            if (!lastCharWasSpace) {
                putchar(c); // Print only one space for consecutive spaces
                lastCharWasSpace = 1;
            }
        } else {
            putchar(c); // Print non-space characters as they are
            lastCharWasSpace = 0;
        }
    }

    return 0;
}


```


## replacing tabs and backspace

```c
#include <stdio.h>

int main() {
    int c;

    printf("Enter some text (press Ctrl+D to end input):\n");

    while ((c = getchar()) != EOF) {
        if (c == '\t') {
            printf("\\t");
        } else if (c == '\b') {
            printf("\\b");
        } else if (c == '\\') {
            printf("\\\\");
        } else {
            putchar(c);
        }
    }

    return 0;
}

```
## Counting words
```c
#include <stdio.h> 
   #define IN   1  /* inside a word */ 
   #define OUT  0  /* outside a word */ 
   /* count lines, words, and characters in input */ 
   main() 
   { 
       int c, nl, nw, nc, state; 
       state = OUT; 
       nl = nw = nc = 0; 
       while ((c = getchar()) != EOF) { 
           ++nc; 
           if (c == '\n') 
               ++nl; 
           if (c == ' ' || c == '\n' || c = '\t') 
               state = OUT; 
           else if (state == OUT) { 
               state = IN; 
               ++nw; 
           } 
       } 
       printf("%d %d %d\n", nl, nw, nc); 
}
```


## Single vs Double quote

Yes, in C programming, single quotes (`'`) and double quotes (`"`) are used to represent different types of literals.

1. **Single Quotes (`'`):**
   - Single quotes are used to represent individual characters in C.
   - For example: `'a'`, `'1'`, `'\n'` (newline character), etc.

2. **Double Quotes (`"`)**
   - Double quotes are used to represent strings in C.
   - For example: `"Hello"`, `"123"`, `"C programming"`, etc



- we cannot compare string with a character maybe so check it out

Here are some examples to illustrate the difference:

```c
#include <stdio.h>

int main() {
    // Single quotes for characters
    char charVariable = 'A';
    printf("Character: %c\n", charVariable);

    // Double quotes for strings
    char stringVariable[] = "Hello, World!";
    printf("String: %s\n", stringVariable);

    return 0;
}
```

In this example, `'A'` is a character literal, and `"Hello, World!"` is a string literal. The key distinction is that single quotes are used for individual characters, while double quotes are used for strings (sequences of characters).

### small note on bitwise or and and

- There is a corresponding operator && for AND; its precedence is just higher than ||. Expressions connected by && or || are evaluated left to right, and it is guaranteed that evaluation will stop as soon as the truth or falsehood is known.


## Arrays

```c
 #include <stdio.h> 
   /* count digits, white space, others */ 
   main() 
   { 
       int c, i, nwhite, nother; 
       int ndigit[10]; 
       nwhite = nother = 0; 
       for (i = 0; i < 10; ++i) 
           ndigit[i] = 0; 
       while ((c = getchar()) != EOF) 
           if (c >= '0' && c <= '9') 
               ++ndigit[c-'0']; 
           else if (c == ' ' || c == '\n' || c == '\t') 
               ++nwhite; 
           else 
               ++nother; 
       printf("digits ="); 
       for (i = 0; i < 10; ++i) 
           printf(" %d", ndigit[i]); 
       printf(", white space = %d, other = %d\n", 
           nwhite, nother);
}
```


- By definition, chars are just small integers **(*Ascii to be precise*)**, so char variables and constants are identical to ints in arithmetic expressions. This is natural and convenient; for example c-'0' is an integer expression with a value between 0 and 9 corresponding to the character '0' to '9' stored in c, and thus a valid subscript for the array ndigit.


## histograms 
code 1
exercise 1-13

```c
#include <stdio.h>

#define MAX_WORD_LENGTH 20

int main() {
    int c;
    int wordLengths[MAX_WORD_LENGTH + 1]; // Array to store word lengths
    int currentWordLength = 0;

    // Initialize the array to zero
    for (int i = 0; i <= MAX_WORD_LENGTH; i++) {
        wordLengths[i] = 0;
    }

    printf("Enter some text (press Ctrl+D to end input):\n");

    // Count word lengths
    while ((c = getchar()) != EOF) {
        if (c == ' ' || c == '\n' || c == '\t') {
            if (currentWordLength > 0 && currentWordLength <= MAX_WORD_LENGTH) {
                wordLengths[currentWordLength]++;
            }
            currentWordLength = 0; // Reset word length for the next word
        } else {
            currentWordLength++;
        }
    }

    // Print vertical histogram
    printf("\nVertical Histogram of Word Lengths:\n");

    for (int i = MAX_WORD_LENGTH; i > 0; i--) {
        printf("%2d |", i);
        for (int j = 1; j <= MAX_WORD_LENGTH; j++) {
            if (wordLengths[j] >= i) {
                printf(" * ");
            } else {
                printf("   ");
            }
        }
        printf("\n");
    }

    // Print the bottom axis
    printf("    +");
    for (int i = 1; i <= MAX_WORD_LENGTH; i++) {
        printf("---");
    }
    printf("\n     ");
    for (int i = 1; i <= MAX_WORD_LENGTH; i++) {
        printf("%2d ", i);
    }
    printf("\n");

    return 0;
}

```


exercise 1-14

```c
#include <stdio.h>

#define ASCII_SIZE 128 // Assuming ASCII character set

int main() {
    int c;
    int charFrequencies[ASCII_SIZE] = {0};

    printf("Enter some text (press Ctrl+D to end input):\n");

    // Count character frequencies
    while ((c = getchar()) != EOF) {
        if (c >= 0 && c < ASCII_SIZE) {
            charFrequencies[c]++;
        }
    }

    // Print histogram
    printf("\nCharacter Frequency Histogram:\n");

    for (int i = 0; i < ASCII_SIZE; i++) {
        if (charFrequencies[i] > 0) {
            printf("%3c |", i);
            for (int j = 0; j < charFrequencies[i]; j++) {
                printf("*");
            }
            printf("\n");
        }
    }

    return 0;
}

```





## Functions

example of  function.

```c
   #include <stdio.h> 
   int power(int m, int n); 
    /* test power function */ 
    main() 
    {
        int i; 
        for (i = 0; i < 10; ++i) 
            printf("%d %d %d\n", i, power(2,i), power(-3,i)); 
        return 0; 
    /* power:  raise base to n-th power; n >= 0 */ 
    int power(int base, int n) 
    { 
        int i,  p; 
        p = 1; 
        for (i = 1; i <= n; ++i) 
            p = p * base; 
        return p; 
    }
}
```



# Note: Calling by value and calling by reference




## Characters in array

Another example to understand better.
In C you literally have to define everything like copy because we cannot assign value of an array to another directly like we used to do in python.
- getline puts the character '\0' (the null character, whose value is zero) at the end of the array it is creating, to mark the end of the string of characters. This conversion is also used by the C language: when a string constant like  "hello\\n"   appears in a C program, it is stored as an array of characters containing the characters in the string and terminated with a '\0' to mark the end.  

## Scope in c

- An external variable must be defined, exactly once, outside of any function; this sets aside storage for it. The variable must also be declared in each function that wants to access it; this states the type of the variable. The declaration may be an explicit extern statement or may be implicit from context.


```c
#include <stdio.h> 
#define MAXLINE 1000   /* maximum input line length */ 
int getline(char line[], int maxline); 
void copy(char to[], char from[]); 
/* print the longest input line */ 
main() 
{ 
int len;            /* current line length */ 
int max;            /* maximum length seen so far */ 
char line[MAXLINE];    /* current input line */ 
char longest[MAXLINE]; /* longest line saved here */ 
max = 0; 
while ((len = getline(line, MAXLINE)) > 0) 
   if (len > max) { 
	   max = len; 
	   copy(longest, line); 
   } 
if (max > 0)  /* there was a line */ 
   printf("%s", longest); 
return 0; 
}
/* getline:  read a line into s, return length  */ 
int getline(char s[],int lim) 
{ 
	int c, i; 
	for (i=0; i < lim-1 && (c=getchar())!=EOF && c!='\n'; ++i) 
	   s[i] = c; 
	if (c == '\n') { 
	   s[i] = c; 
	   ++i; 
	} 
	s[i] = '\0'; 
	return i; 
}
/* copy:  copy 'from' into 'to'; assume to is big enough */ 
void copy(char to[], char from[]) 
{ 
   int i; 
   i = 0; 
   while ((to[i] = from[i]) != '\0') 
	   ++i; 
} 
```



## Definition vs declaration

- You should note that we are using the words definition and declaration carefully when we refer to external variables in this section. Definition refers to the place where the variable is  created or assigned storage; declaration refers to places where the nature of the variable is stated but no storage is allocated.



## This is how appending in c works

```python
#include <stdio.h>  
#include <stdlib.h>  
  
int main() {  
  
int size = 10;  
int myArray[size];  
int newArray[size+1];  
int newElement = 5;  
  
memcpy(newArray, myArray, size * sizeof(int));  
newArray[size] = newElement;  
  
// Print the new array  
for (int i = 0; i < size+1; i++) {  
printf("%d ", newArray[i]);  
}  
  
return 0;  
}
```


