# C   :-)

First Program
```c
 #include <stdio.h> 
   main() 
   { 
     printf("hello, world\n"); 
     return 0;
   } 
```

- To run the program use the ccompiler to compile. Use gcc filename.c. It will generate a.out and then run a.out. 
- to get output as exe write gcc filename -o newname.exe
- Normally you are at liberty to give functions whatever names you like, but main ' is special - your program begins executing at the beginning of main. This means that every program must have a main somewhere. main will usually call other functions to help perform its job, some that you wrote, and others from libraries that are provided for you.


```c
# Types of variables

char   character - a single byte 
short    short integer 
long   long integer 
double   double-precision floating point 
```

- The size of these objects is also machine-dependent.

- There are a couple of problems with the temperature conversion program. The simpler one is that the output isn't very pretty because the numbers are not right-justified. That's easy to fix; if we augment each %d in the printf statement with a width, the numbers printed will be right-justified in their fields. For instance, we might say  
	**printf("%3d %6d\\n", fahr, celsius)**; 
	to print the first number of each line in a field three digits wide, and the second in a field six digits wide, like this:  
 
     0     -17 
    20      -6 
    40       4 
    60      15 
    80      26 
	100      37


```c
 #include <stdio.h> 
   /* print Fahrenheit-Celsius table 
       for fahr = 0, 20, ..., 300; floating-point version */ 
   int main() 
   { 
     float fahr, celsius; 
     float lower, upper, step; 
     lower = 0;      /* lower limit of temperatuire scale */ 
     upper = 300;    /* upper limit */ 
     step = 20;      /* step size */ 
     fahr = lower; 
     while (fahr <= upper) { 
         celsius = (5.0/9.0) * (fahr-32.0); 
         printf("%3.0f %6.1f\n", fahr, celsius); 
         fahr = fahr + step; 
     } 
     return 0;
    }
```


- This is much the same as before, except that fahr and celsius are declared to be float and the formula for conversion is written in a more natural way. We were unable to use 5/9 in the previous version because integer division would truncate it to zero. A decimal point in a constant indicates that it is floating point, however, so 5.0/9.0 is not truncated because it is the ratio of two floating-point values.


- If an arithmetic operator has integer operands, an integer operation is performed. If an arithmetic operator has one floating-point operand and one integer operand, however, the integer will be converted to floating point before the operation is done. If we had written (fahr-32), the 32 would be automatically converted to floating point.



# For and while loops

# Symbolic constants
```c
#define Maxline 300
```

# Character Input and Output

```c
int c;
c = getchar();
putchar(c);
```


- What appears to be a character on the keyboard or screen is of course, like everything else, stored internally just as a bit pattern. The type char is specifically meant for storing such character data, but any integer type can be used. We used int for a subtle but important reason. The problem is distinguishing the end of input from valid data. The solution is that getchar returns a distinctive value when there is no more input, a value that cannot be confused with any real character. This value is called EOF, for \`\`end of file''. We must declare c to be a type big enough to hold any value that getchar returns. We can't use char since c must be big enough to hold EOF in addition to any possible char. Therefore we use int.
## Counting characters, words, number of lines , tabs etc. using c

- use stdio.h header only. That is use only getchar and putchar.

- Character Counting
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

- Words counting 
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

- Line counting
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

## Arrays in C

## Functions

## Arguments call by value
- One aspect of C functions may be unfamiliar to programmers who are used to some other languages, particulary Fortran. In C, all function arguments are passed by value. This means that the called function is given the values of its arguments in temporary variables rather than the originals. This leads to some different properties than are seen with call by reference'' languages like Fortran or with var parameters in Pascal, in which the called routine has access to the original argument, not a local copy.
## Character Arrays or strings

- difference in using '' and ""
- strings always ends with \\0  to determine the end of string we can use this property to perform lot many tasks.
- 

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

## External Variables and Scopes

- The \`extern\` keyword in C is used to declare a variable or function that is defined in another source file or in the same file but outside of the current scope. Essentially, it tells the compiler that the variable or function exists elsewhere and is not defined in the current scope, and it instructs the compiler not to allocate storage for that variable.

Here's how `extern` works for variables:

1. **Declaration**: When you want to use a variable that is defined in another file or scope, you declare it with the `extern` keyword. This informs the compiler about the existence and type of the variable without allocating storage for it.

    ```c
    extern int globalVariable;
    ```

2. **Definition**: In a separate file or in the same file but outside of any function, you define the variable without the `extern` keyword. This actually allocates storage for the variable.

    ```c
    int globalVariable; // Definition, not extern
    ```

By separating declaration and definition, you can access the variable from multiple files without causing multiple definitions, which would lead to linker errors.

Here's an example demonstrating the use of `extern`:

File 1 (file1.c):
```c
#include <stdio.h>

extern int globalVariable; // Declaration

void function1() {
    printf("The value of globalVariable from function1: %d\n", globalVariable);
}
```

File 2 (file2.c):
```c
#include <stdio.h>

int globalVariable = 10; // Definition

extern void function1(); // Declaration of function from file1.c

int main() {
    function1();
    printf("The value of globalVariable from main: %d\n", globalVariable);
    return 0;
}
```

In this example:

- `globalVariable` is declared with `extern` in file1.c but defined in file2.c.
- `function1` is declared with `extern` in file2.c so that it can be used in main.c.

This setup allows sharing of the `globalVariable` and `function1` across files without causing linker errors.




