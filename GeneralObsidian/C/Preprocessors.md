
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