# Input Output

## File Handling using C


|Functions|Description|
|---|---|
|[fopen()](https://www.geeksforgeeks.org/c-fopen-function-with-examples/)|It is used to create a file or to open a file.|
|fclose()|It is used to close a file.|
|[fgets()](https://www.geeksforgeeks.org/fgets-gets-c-language/)|It is used to read a file.|
|[fprintf()](https://www.geeksforgeeks.org/fprintf-in-c/)|It is used to write blocks of data into a file.|
|[fscanf()](https://www.geeksforgeeks.org/scanf-and-fscanf-in-c/)|It is used to read blocks of data from a file.|
|[getc()](https://www.geeksforgeeks.org/difference-getchar-getch-getc-getche/)|It is used to read a single character to a file.|
|[putc()](https://www.geeksforgeeks.org/c-library-function-putc/)|It is used to write a single character to a file.|
|[fseek()](https://www.geeksforgeeks.org/fseek-in-c-with-example/)|It is used to set the position of a file pointer to a mentioned location.|
|[ftell()](https://www.geeksforgeeks.org/ftell-c-example/)|It is used to return the current position of a file pointer.|
|[rewind()](https://www.geeksforgeeks.org/g-fact-82/)|It is used to set the file pointer to the beginning of a file.|
|putw()|It is used to write an integer to a file.|
|getw()|It is used to read an integer from a file.|



## Standard Input and Output
Pipe | and > < operators in terminal can be used along with the c program

prog | otherprog   it means output of prog is fed into input of otherprog

prog > file  it means output of prog is written into file

prog < file it means input of prog is taken from file

## Formatted Output

printf("")

The format string contains two types of objects: ordinary characters, which are copied to the output stream, and conversion specifications, each of which causes conversion and printing of the next successive argument to printf. Each conversion specification begins with a % and ends with a conversion character. Between the % and the conversion character there may be, in order:  

-  A minus sign, which specifies left adjustment of the converted argument.  
-  A number that specifies the minimum field width. The converted argument will be printed in a field at least this wide. If necessary it will be padded on the left (or right, if left adjustment is called for) to make up the field width.  
-  A period, which separates the field width from the precision.  
-  A number, the precision, that specifies the maximum number of characters to be printed from a string, or the number of digits after the decimal point of a floating-point value, or the minimum number of digits for an integer.  
-  An h if the integer is to be printed as a short, or l (letter ell) if as a long.  

## Variable Length Argument List

- This section contains an implementation of a minimal version of printf, to show how to write a function that processes a variable-length argument list in a portable way.

These properties form the basis of our simplified printf:  
```c
#include <stdarg.h> 
   /* minprintf: minimal printf with variable argument list */ 
   void minprintf(char *fmt, ...) 
   { 
       va_list ap; /* points to each unnamed arg in turn */ 
       char *p, *sval; 
       int ival; 
       double dval; 
       va_start(ap, fmt); /* make ap point to 1st unnamed arg */ 
       for (p = fmt; *p; p++) { 
           if (*p != '%') { 
               putchar(*p); 
               continue; 
           } 
           switch (*++p) { 
           case 'd': 
               ival = va_arg(ap, int); 
               printf("%d", ival); 
               break; 
           case 'f': 
               dval = va_arg(ap, double); 
               printf("%f", dval); 
               break; 
           case 's': 
               for (sval = va_arg(ap, char *); *sval; sval++) 
                   putchar(*sval); 
               break; 
           default: 
               putchar(*p); 
               break; 
           } 
       } 
       va_end(ap); /* clean up when done */ 
   }
```


### How to handle unnamed args in c

In C, you don't have a built-in mechanism like Python's `*args` for handling a variable number of arguments. However, you can achieve similar functionality using variadic functions and the `<stdarg.h>` header.

Here's a basic example of how you can define a function in C to accept a variable number of arguments:

```c
#include <stdio.h>
#include <stdarg.h>

void my_function(int count, ...) {
    va_list args;
    int i;

    va_start(args, count); // Initialize the va_list

    for (i = 0; i < count; i++) {
        // Access each argument using va_arg macro
        int arg = va_arg(args, int);
        printf("%d ", arg);
    }

    va_end(args); // Clean up the va_list
}

int main() {
    my_function(4, 1, 2, 3, 4);
    return 0;
}
```

In this example:

- `my_function` takes an integer `count` followed by a variable number of arguments.
- Inside the function, `va_list` is declared to hold the variable number of arguments.
- `va_start` initializes the `va_list` to point to the first argument after `count`.
- `va_arg` retrieves each argument one by one, and its type is specified as the second argument.
- The loop iterates `count` times, printing each argument.
- Finally, `va_end` is used to clean up the `va_list`.

Remember, with this approach, you need some way of knowing how many arguments were passed (hence the first argument `count`). If you don't know the number of arguments beforehand, you may need to pass some sentinel value or use some other mechanism to determine the end of the arguments.

## Formatted Input
scanf()

The format string usually contains conversion specifications, which are used to control conversion of input. The format string may contain:
- Blanks or tabs, which are not ignored. 
- Ordinary characters (not %), which are expected to match the next non-white space character of the input stream.
- Conversion specifications, consisting of the character %, an optional assignment suppression character \*, an optional number specifying a maximum field width, an optional h, l or L indicating the width of the target, and a conversion character.


## File Access 

When a C program is started, the operating system environment is responsible for opening three files and providing pointers for them. These files are the standard input, the standard output, and the standard error; the corresponding file pointers are called stdin, stdout, and stderr, and are declared in <stdio.h>. Normally stdin is connected to the keyboard and stdout and stderr are connected to the screen, but stdin and stdout may be redirected to files or pipes as described in Section 7.1.


This pointer, called the file pointer, points to a structure that contains information about the file, such as the location of a buffer, the current character position in the buffer, whether the file is being read or written, and whether errors or end of file have occurred. Users don't need to know the details, because the definitions obtained from include a structure declaration called FILE. The only declaration needed for a file pointer is exemplified by

```c
FILE *fp; 
FILE *fopen(char *name, char *mode);
```

Notice that FILE is a type name, like int, not a structure tag; it is defined with a typedef.


For formatted input or output of files, the functions fscanf and fprintf may be used. These are identical to scanf and printf, except that the first argument is a file pointer that specifies the file to be read or written; the format string is the second argument.  
```c
   int fscanf(FILE *fp, char *format, ...) 
   int fprintf(FILE *fp, char *format, ...)
```



```c
 #include <stdio.h> 
   /* cat:  concatenate files, version 1 */ 
   main(int argc, char *argv[]) 
   { 
       FILE *fp; 
       void filecopy(FILE *, FILE *) 
       if (argc == 1) /* no args; copy standard input */ 
           filecopy(stdin, stdout); 
       else 
          while(--argc > 0) 
              if ((fp = fopen(*++argv, "r")) == NULL) { 
                  printf("cat: can't open %s\n, *argv); 
                  return 1; 
              } else { 
                 filecopy(fp, stdout); 
                 fclose(fp); 
              } 
          return 0; 
   } 
    /* filecopy:  copy file ifp to file ofp */ 
    void filecopy(FILE *ifp, FILE *ofp) 
    { 
        int c; 
        while ((c = getc(ifp)) != EOF) 
            putc(c, ofp); 
    } 
```



```c
int fclose(FILE *fp) 
```
is the inverse of fopen, it breaks the connection between the file pointer and the external name that was established by fopen, freeing the file pointer for another file.





## Error handling

Let us revise cat to write its error messages on the standard error.  
```c
#include <stdio.h> 
   /* cat:  concatenate files, version 2 */ 
   main(int argc, char *argv[]) 
   { 
       FILE *fp; 
       void filecopy(FILE *, FILE *); 
       char *prog = argv[0];  /* program name for errors */ 
       if (argc == 1 ) /* no args; copy standard input */ 
           filecopy(stdin, stdout); 
       else 
           while (--argc > 0) 
               if ((fp = fopen(*++argv, "r")) == NULL) { 
                   fprintf(stderr, "%s: can't open %s\n", 
                           prog, *argv); 
                   exit(1); 
               } else { 
                   filecopy(fp, stdout); 
                   fclose(fp); 
               } 
       if (ferror(stdout)) { 
           fprintf(stderr, "%s: error writing stdout\n", prog); 
           exit(2); 
       } 
       exit(0); 
   } 
```

### exit() in c 
In C programming, the `exit()` function is used to terminate a program abruptly. It is defined in the `<stdlib.h>` header file. The `exit()` function takes an integer argument, which is known as the exit status. This exit status is typically used to indicate whether the program terminated successfully or encountered an error.

Here's the basic syntax of the `exit()` function:

```c
#include <stdlib.h>

void exit(int status);
```

- `status`: An integer value representing the exit status of the program. A status of 0 usually indicates successful termination, while non-zero values typically indicate some error condition.

When you call `exit()` within your program, it immediately terminates the program and returns control to the operating system, along with the specified exit status. All open files are closed, and any functions registered with `atexit()` or `on_exit()` are executed before termination.

Here's a simple example demonstrating the usage of `exit()`:

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    printf("Before exit\n");
    exit(0); // Terminate the program with exit status 0 (success)
    printf("After exit\n"); // This line will not be executed
    return 0;
}
```

In this example, the program terminates after the `exit(0)` call, and "Before exit" is printed to the console. The line "After exit" is never printed because the program terminates before reaching that point.






The function ferror returns non-zero if an error occurred on the stream fp. int ferror(FILE \*fp) Although output errors are rare, they do occur (for example, if a disk fills up), so a production program should check this as well. The function feof(FILE \*) is analogous to ferror; it returns non-zero if end of file has occurred on the specified file. int feof(FILE \*fp) We have generally not worried about exit status in our small illustrative programs, but any serious program should take care to return sensible, useful status values.
## Line Input and Output

**(*standard library provides a lot many functions. Try to expxlore them and write them on your own.*)**

The standard library provides an input and output routine fgets that is similar to the getline function. 



# Miscellaneous

## String Operations
We have already mentioned the string functions strlen, strcpy, strcat, and strcmp, found in <string.h>. In the following, s and t are char \*'s, and c and n are ints.  

- strcat(s,t)         concatenate t to end of s 
- strncat(s,t,n)    concatenate n characters of t to end of s 
- strcmp(s,t)       return negative, zero, or positive for s < t, s == t, s > t 
- strncmp(s,t,n)  same as strcmp but only in first n characters 
- strcpy(s,t)        copy t to s 
- strlen(s)           copy at most n characters of t to s 
- strncpy(s,t,n)   return length of s 
- strchr(s,c)        return pointer to first c in s, or NULL if not present 
- strrchr(s,c)       return pointer to last c in s, or NULL if not present 

## Character Class Testing and Conversions

Several functions from perform character tests and conversions. In the following, c is an int that can be represented as an unsigned char or EOF. The function returns int.

- isalpha(c)             non-zero if c is alphabetic, 0 if not 
- isupper(c)            non-zero if c is upper case, 0 if not 
- islower(c)             non-zero if c is lower case, 0 if not 
- isdigit(c)               non-zero if c is digit, 0 if not 
- isalnum(c)            non-zero if isalpha(c) or isdigit(c), 0 if not 
- isspace(c)             non-zero if c is blank, tab, newline, return, formfeed,                                         vertical tab 
- toupper(c)            return c converted to upper case 
- tolower(c)            return c converted to lower case 

## Ungetc

- The standard library provides a rather restricted version of the function ungetch that we wrote in Chapter 4 ; it is called ungetc. int ungetc(int c, FILE \*fp) pushes the character c back onto file fp, and returns either c, or EOF for an error. Only one character of pushback is guaranteed per file. ungetc may be used with any of the input functions like scanf, getc, or getchar.


## Command Execution
The function system(char \*s) executes the command contained in the character string s, then resumes execution of the current program. The contents of s depend strongly on the local operating system. As a trivial example, on UNIX systems, the statement system("date"); causes the program date to be run; it prints the date and time of day on the standard output. system returns a system-dependent integer status from the command executed. In the UNIX system, the status return is the value returned by exit.

## Storage Management



### Calloc

In C, `calloc()` is a function used to dynamically allocate memory for an array of elements. It stands for "contiguous allocation". It's similar to `malloc()`, but it initializes the allocated memory block to zero. 

The syntax for `calloc()` is:

```c
void *calloc(size_t num_elements, size_t element_size);
```

- `num_elements`: Number of elements to allocate memory for.
- `element_size`: Size of each element in bytes.

`calloc()` returns a pointer to the beginning of the allocated memory block. If the memory allocation fails, it returns NULL.

Here's an example of how you might use `calloc()`:

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr;
    int num_elements = 5;
    
    // Allocate memory for an array of 5 integers
    arr = (int *)calloc(num_elements, sizeof(int));

    if (arr == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    // Use the allocated memory
    for (int i = 0; i < num_elements; i++) {
        printf("arr[%d] = %d\n", i, arr[i]);
    }

    // Free the allocated memory when done
    free(arr);

    return 0;
}
```

In this example, `calloc()` allocates memory for an array of 5 integers, initializes it to zero, and then we can use it as needed. Finally, we free the allocated memory using `free()` to avoid memory leaks.








Certainly! Here are concise summaries for your notes:

### Using `malloc` in C

- **Dynamic Allocation:** `malloc` is used for dynamic memory allocation in C.
  
- **Dynamic Size:** Allows you to allocate memory based on a size that is determined at runtime.

- **Pointer Return:** Returns a pointer to the allocated memory, typically used for representing arrays.

- **Lifetime Control:** Memory persists until explicitly freed with `free`.

- **Responsibility:** Requires manual memory management; you must free the allocated memory when done.

### Alternatives without `malloc`

1. **Static Array:**
   - Limited by a fixed size determined at compile-time.
   - Example:
     ```c
     int* createArray() {
         static int newArray[] = {1, 2, 3, 4, 5};
         return newArray;
     }
     ```

2. **Passing Array as Parameter:**
   - Requires the caller to pre-allocate memory.
   - Example:
     ```c
     void fillArray(int* arr, int size) {
         // fill arr with values
     }
     int main() {
         int myArray[5];
         fillArray(myArray, 5);
         // Now myArray is filled with values
         return 0;
     }
     ```

Note: Dynamic memory allocation with `malloc` is preferred for flexibility in array size and when the size is not known at compile-time. Always free the allocated memory using `free` to prevent memory leaks.








Certainly! Here are some common use cases for `malloc()` and `free()`:

### 1. Dynamic Allocation of Single Variable:

```c
int *ptr;
ptr = (int *)malloc(sizeof(int));
if (ptr != NULL) {
    *ptr = 10;
}
// Use ptr...
free(ptr);
```

### 2. Dynamic Allocation of Arrays:

```c
int *arr;
int size = 10;
arr = (int *)malloc(size * sizeof(int));
if (arr != NULL) {
    // Initialize array elements...
}
// Use arr...
free(arr);
```

### 3. Dynamic Allocation of 2D Arrays:

```c
int **matrix;
int rows = 5, cols = 3;
matrix = (int **)malloc(rows * sizeof(int *));
if (matrix != NULL) {
    for (int i = 0; i < rows; i++) {
        matrix[i] = (int *)malloc(cols * sizeof(int));
        // Initialize each row...
    }
}
// Use matrix...
// Free memory for each row
for (int i = 0; i < rows; i++) {
    free(matrix[i]);
}
free(matrix);
```

### 4. Dynamic Allocation of Structs:

```c
typedef struct {
    int x;
    int y;
} Point;

Point *p;
p = (Point *)malloc(sizeof(Point));
if (p != NULL) {
    p->x = 10;
    p->y = 20;
}
// Use p...
free(p);
```

### 5. Returning Dynamically Allocated Memory from a Function:

```c
int *createArray(int size) {
    int *arr = (int *)malloc(size * sizeof(int));
    // Initialize arr...
    return arr;
}

void destroyArray(int *arr) {
    free(arr);
}

int main() {
    int *arr = createArray(10);
    // Use arr...
    destroyArray(arr);
    return 0;
}
```

### 6. Error Handling for `malloc()` Failures:

```c
int *ptr;
ptr = (int *)malloc(sizeof(int));
if (ptr == NULL) {
    printf("Memory allocation failed\n");
    exit(1);
}
// Continue with program...
```

Remember to always check the return value of `malloc()` to ensure that memory allocation was successful, and to free dynamically allocated memory using `free()` when it's no longer needed to prevent memory leaks.








## Mathematical Functions

There are more than twenty mathematical functions declared in <math.h>; here are some of the more frequently used. Each takes one or two double arguments and returns a double.  

- sin(x)                       sine of x, x in radians 
- cos(x)                      cosine of x, x in radians 
- exp(x)                      exponential function ex 
- atan2(y,x)                arctangent of y/x, in radians 
- log(x)                      natural (base e) logarithm of x (x>0) 
- log10(x)                  common (base 10) logarithm of x (x>0) 
- pow(x,y)                  x$^y$ 
- sqrt(x)                     square root of x (x>0) 
- fabs(x)                    absolute value of x 


## Random Number Generation


The function rand() computes a sequence of pseudo-random integers in the range zero to RAND_MAX, which is defined in <stdlib.h>. One way to produce random floating-point numbers greater than or equal to zero but less than one is  
   \#define frand() ((double) rand() / (RAND_MAX+1.0)) 

(If your library already provides a function for floating-point random numbers, it is likely to have better statistical properties than this one.)  The function srand(unsigned) sets the seed for rand. The portable implementation of rand 
and srand suggested by the standard appears in Section 2.7





