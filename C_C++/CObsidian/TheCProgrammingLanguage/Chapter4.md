#  Functions and Program structures


common syntax of the functions

- By default it is adduemd that the funciton will return the int type unless mentioned explicitly
- Using functions with external variables 


## See all the exercise questions by yourself they are very good

## Static Variables

In C, a `static` variable is a type of variable that retains its value across function calls and has a lifespan equal to the duration of the program. There are two main contexts where `static` variables can be used: within functions and outside functions.

1. **Static Variables within Functions**:
   When a variable is declared as `static` within a function, it retains its value between function calls. This means that the variable is initialized only once, and its value persists across subsequent calls to the function. Here's an example:

   ```c
   #include <stdio.h>

   void counter() {
       static int count = 0; // Static variable
       count++;
       printf("Count: %d\n", count);
   }

   int main() {
       counter(); // Output: Count: 1
       counter(); // Output: Count: 2
       counter(); // Output: Count: 3
       return 0;
   }
   ```

   In this example, the `count` variable is declared as `static` within the `counter` function. Each time `counter` is called, the value of `count` persists and is incremented.

2. **Static Variables outside Functions**:
   When a variable is declared as `static` outside of any function, it becomes a global variable with file scope. This means that the variable is accessible only within the file where it is declared. Here's an example:

   ```c
   #include <stdio.h>

   static int global_var = 10; // Static variable with file scope

   void function() {
       printf("Global variable: %d\n", global_var);
   }

   int main() {
       function(); // Output: Global variable: 10
       return 0;
   }
   ```

   In this example, `global_var` is declared as a `static` variable outside of any function. It can be accessed by any function defined within the same source file, but it is not accessible from other files.

Static variables are initialized to zero by default if not explicitly initialized. They are allocated in the data segment of the program's memory and retain their value throughout the program's execution.

## Register Variables

In C, `register` is a keyword used to suggest to the compiler that a particular variable should be stored in a CPU register for faster access. However, it's important to note that the use of `register` is merely a hint to the compiler, and the compiler may or may not honor this request.

Historically, when C was first developed, compilers often lacked sophisticated optimization techniques, and programmers could use the `register` keyword to suggest to the compiler that certain variables should be placed in CPU registers for faster access, especially for frequently accessed variables within loops or critical sections of code.

Here's an example of using the `register` keyword:

```c
#include <stdio.h>

int main() {
    register int i; // Declare a register variable
    
    for (i = 0; i < 10; i++) {
        printf("%d\n", i);
    }
    
    return 0;
}
```

In this example, `i` is declared as a register variable. The intention here is to hint to the compiler that `i` should be stored in a CPU register for faster access within the loop.

However, modern compilers are highly optimized and often make better decisions about register allocation than programmers. In many cases, the use of the `register` keyword has become obsolete, and compilers may ignore it altogether. In fact, some compilers might emit a warning if you try to use `register` since it's often considered redundant. 

So, while `register` was once a useful optimization hint, its usefulness has diminished over time due to advances in compiler optimization techniques.








## Initialization
 - In the absence of explicit initialization, external and static variables are guaranteed to be initialized to zero; automatic and register variables have undefined (i.e., garbage) initial values.


## Recursion

# The C Preprocessor





# Notes from chatgpt
 Preprocessors in C are tools that manipulate the source code before it is compiled. They are directives that provide instructions to the compiler to perform certain tasks such as including header files, defining constants, and conditionally compiling code. Preprocessors begin with a `#` symbol and are processed before the actual compilation of the code.

Here are some commonly used preprocessor directives in C:

1. `#include`: Includes the contents of another file in the source code.
2. `#define`: Defines a macro or a symbolic constant.
3. `#ifdef`, `#ifndef`, `#endif`: Conditional compilation directives.
4. `#if`, `#elif`, `#else`: Conditional compilation based on expressions.
5. `#pragma`: Provides additional instructions to the compiler.

The workflow of compiling a C program typically involves several steps:

1. **Preprocessing**: The preprocessor scans the source code, processes preprocessor directives, and generates an intermediate code known as the preprocessed code.

2. **Compilation**: The preprocessed code is passed to the compiler, which translates it into assembly language or machine code. This involves lexical analysis, parsing, semantic analysis, and optimization.

3. **Assembly**: The assembly code generated by the compiler is converted into object code by the assembler. Object code is a binary representation of the program's instructions.

4. **Linking**: If the program consists of multiple source files or external libraries, the linker combines the object code generated from each source file and resolves references to external symbols. This produces an executable file or a library.

5. **Execution**: The executable file is loaded into memory and executed by the operating system or runtime environment.

During the preprocessing stage, the preprocessor performs the following tasks:

- Removes comments from the source code.
- Expands macros defined using `#define`.
- Includes contents of header files specified using `#include`.
- Handles conditional compilation directives such as `#ifdef`, `#if`, etc.
- Performs other text manipulations specified by preprocessor directives.

Once preprocessing is complete, the compiler takes the preprocessed code and performs the actual compilation, generating assembly code or machine code depending on the target architecture and compiler settings.



# It is not necessary to spend much time learning the preprocessors right now 
# So learn it whenever necessary or you have time



# How c works
Pre processing>Compilation>Assembly>Linking

## Preprocessing
- removal of comments
- Expansion of Macros
- Expansion of include files

## Compilation
- Assembly level instructions generated

## Assembly
- .o or .exe file generated but printf are not resolved and the code are converted to machine code.
- machine code is binary
## Linking
- Resolves all the function calls
- Links the function implementations


# C preprocessor

- Comes before actual compilation
- Not a part of compiler
- All preprocessing have \# on the start

- 

## Preprocessor commands examples
- \#define
- \#include
- \#undef
- \#ifdef
- \#if
- \#ifndef
- \#if
- \#else
- \#elif






### File inclusion
- C provides certain language facilities by means of a preprocessor, which is conceptionally a separate first step in compilation.
- \#include "filename" or \#include \<filename\>
- If the filename is quoted, searching for the file typically begins where the source program was found; if it is not found there, or if the name is enclosed in < and >, searching follows an implementation-defined rule to find the file. 
### Macro substitution

- A definition has the form \#define name replacement text It calls for a macro substitution of the simplest kind - subsequent occurrences of the token name will be replaced by the replacement text.
- \#define PI 3.14159

- All occurences of PI in the code will be replaced by 3.14159
- \#define max(A, B) ((A) > (B) ? (A) : (B))                                                  Although it looks like a function call, a use of max expands into in-line code. Each occurrence of a formal parameter (here A or B) will be replaced by the corresponding actual argument. Thus the line x = max(p+q, r+s); will be replaced by the line x = ((p+q) > (r+s) ? (p+q) : (r+s)); So long as the arguments are treated consistently, this macro will serve for any data type; there is ==no need for different kinds of max for different data types==, as there would be with functions.
- The preprocessor operator ## provides a way to concatenate actual arguments during macro expansion. If a parameter in the replacement text is adjacent to a ##, the parameter is replaced by the actual argument, the ## and surrounding white space are removed, and the result is re scanned. For example, the macro paste concatenates its two arguments


### Conditional Inclusion

-  For example, to make sure that the contents of a file hdr.h are included only once, the contents of the file are surrounded with a conditional like this:  
	   \#if !defined(HDR) 
	   \#define HDR 
	   /* contents of hdr.h go here */ 
	   \#endif 
	
- 