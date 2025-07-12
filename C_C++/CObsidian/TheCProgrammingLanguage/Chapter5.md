Pointers and Arrays




# Pointers
- A pointer is a variable that contains the address of a variable. Pointers are much used in C, partly because they are sometimes the only way to express a computation, and partly because they usually lead to more compact and efficient code than can be obtained in other ways.
- One common situation is that any byte can be a char, a pair of one-byte cells can be treated as a short integer, and four adjacent bytes form a long. A pointer is a group of cells (often two or four) that can hold an address.
- The unary operator & gives the address of an object,
	- p = &c;
- The & operator only applies to objects in memory: variables and array elements. It cannot be applied to expressions, constants, or register variables.
- The unary operator * is the indirection or dereferencing operator; when applied to a pointer, it accesses the object the pointer points to. Suppose that x and y are integers and ip is a pointer to int.

```c
int x = 1, y = 2, z[10]; 
int *ip;          /* ip is a pointer to int */ 
ip = &x;          /* ip now points to x */ 
y = *ip;          /* y is now 1 */ 
*ip = 0;          /* x is now 0 */ 
ip = &z[0];       /* ip now points to z[0] */ 
```

- pointer is to be declared

- You should also note the implication that a pointer is constrained to point to a particular kind of object: every pointer points to a specific data type.
- we should realize that all the variables are essentially pointers so we can also use pointers to do changes in the variable value.
- 

### Note: pointer to void is used to hold any type of pointer but cannot be dereferenced itself.


## Pointers in function arguments

```c
void swap(int x, int y)  /* WRONG */ 
   { 
       int temp; 
       temp = x; 
       x = y; 
       y = temp; 
   } 
/*It is done by value and the below is done by reference*/


 void swap(int *px, int *py)  /* interchange *px and *py */ 
   { 
       int temp; 
       temp = *px; 
       *px = *py; 
       *py = temp; 
   } 
   
```





## Pointers and Array

- Arrays are itself pointers but the only difference is that pointers are variables that means that we can change the value of pointers but not the arrays
- How to manipulate the arrays using the pointer.

```c
/* strlen:  return length of string s */ 
   int strlen(char *s) 
   { 
       int n; 
       for (n = 0; *s != '\0', s++) 
           n++; 
       return n; 
   } 
```

- It is possible to pass part of an array to a function, by passing a pointer to the beginning of the subarray. For example, if a is an array, f(&a\[2]) and f(a+2) both pass to the function f the address of the subarray that starts at a\[2]. Within f, the parameter declaration can read
- Rather more surprising, at first sight, is the fact that a reference to a[i] can also be written as \*(a+i). In evaluating a\[i], C converts it to (a+i) immediately; the two forms are equivalent. Applying the operator & to both parts of this equivalence, it follows that &a\[i] and a+i are also identical: a+i is the address of the i-th element beyond a. As the other side of this coin, if pa is a pointer, expressions might use it with a subscript; pa\[i] is identical to \*(pa+i). In short, an array-and-index expression is equivalent to one written as a pointer and offset.



- As formal parameters in a function definition, char s[]; and char \*s; are equivalent; we prefer the latter because it says more explicitly that the variable is a pointer.


## Address Arithmetic

- we can perform p++ and p+=i can be performed on the pointer variable but it cannot be done on arrays.


- The first, alloc(n), returns a pointer to n consecutive character positions, which can be used by the caller of alloc for storing characters. The second, afree(p), releases the storage thus acquired so it can be re used later. The routines are \`\`rudimentary'' because the calls to afree must be made in the opposite order to the calls made on alloc. That is, the storage managed by alloc and afree is a stack, or last-in, first-out. The standard library provides analogous functions called malloc and free that have no such restrictions; in Section 8.7 implemented.


```c
   #define ALLOCSIZE 10000 /* size of available space */ 
   static char allocbuf[ALLOCSIZE]; /* storage for alloc */ 
   static char *allocp = allocbuf;  /* next free position */ 
   char *alloc(int n)    /* return pointer to n characters */ 
   { 
       if (allocbuf + ALLOCSIZE - allocp >= n) {  /* it fits */ 
           allocp += n; 
           return allocp - n; /* old p */ 
       } else      /* not enough room */ 
           return 0; 
   } 
   void afree(char *p)  /* free storage pointed to by p */ 
   { 
       if (p >= allocbuf && p < allocbuf + ALLOCSIZE) 
           allocp = p; 
   } 
```

- we have already observed that a pointer and an integer may be added or subtracted.
- Pointer subtraction is also valid: if p and q point to elements of the same array, and p
- pointer is basically a hexadecimal number that points to memory.
- Pointers are vey essential and necessary so explore them whenever you have time.
- pointers can be compared as well


- ++\*ip and (\*ip)++ The parentheses are necessary in this last example; without them, the expression would increment ip instead of what it points to, because unary operators like * and ++ associate right to left.



## Character pointers and functions


- If pmessage is declared as char \*pmessage; then the statement pmessage = "now is the time"; assigns to pmessage a pointer to the character array. This is not a string copy; only pointers are involved. C does not provide any operators for processing an entire string of characters as a unit. There is an important difference between these definitions: 94 char amessage[] = "now is the time"; /* an array \*/ char *pmessage = "now is the time"; /* a pointer \*/ amessage is an array, just big enough to hold the sequence of characters and '\0' that initializes it. Individual characters within the array may be changed but amessage will always refer to the same storage. On the other hand, pmessage is a pointer, initialized to point to a string constant; the pointer may subsequently be modified to point elsewhere, but the result is undefined if you try to modify the string contents.

-  It would be nice just to say s=t but this copies the pointer, not the 
characters. To copy the characters, we need a loop. The array version first:  
```c
/* strcpy:  copy t to s; array subscript version */ 
   void strcpy(char *s, char *t) 
   { 
       int i; 
       i = 0; 
       while ((s[i] = t[i]) != '\0') 
           i++; 
   } 
```

For contrast, here is a version of strcpy with pointers:  

```c
/* strcpy:  copy t to s; pointer version */ 
   void strcpy(char *s, char *t) 
   { 
       int i; 
       i = 0; 
       while ((*s = *t) != '\0') { 
           s++; 
           t++; 
       } 
   } 
```


- `char *name[]` and `char name[]` are both declarations involving character arrays, but they represent different things:

1. **`char *name[]`**:
   - This declares an array of pointers to characters.
   - Each element of the array `name` is a pointer to a character (string).
   - It's often used to represent an array of strings or a list of strings.
   - Memory is allocated for the array of pointers, but memory for the strings themselves may need to be allocated separately.

   Example:
   ```c
   char *names[] = {"John", "Alice", "Bob"};
   ```
   In this example, `names` is an array of pointers to strings. Each element of `names` points to the first character of a string literal.

2. **`char name[]`**:
   - This declares a character array or a string.
   - It's used to represent a single string of characters.
   - Memory is allocated for the string itself, and it's usually initialized with a specific string literal or characters.

   Example:
   ```c
   char name[] = "Hello";
   ```
   In this example, `name` is a character array initialized with the string "Hello". The size of the array is automatically determined based on the length of the string literal.

In summary, `char *name[]` represents an array of strings, where each element is a pointer to a string, while `char name[]` represents a single string of characters.


## Pointer Arrays and pointers to pointers

- The sorting process has three steps: read all the lines of input sort them print them in order

- The output routine only has to print the lines in the order in which they appear in the array of pointers.  

```c
   #include <stdio.h> 
   #include <string.h> 
   #define MAXLINES 5000     /* max #lines to be sorted */ 
   char *lineptr[MAXLINES];  /* pointers to text lines */ 
   int readlines(char *lineptr[], int nlines); 
   void writelines(char *lineptr[], int nlines); 
   void qsort(char *lineptr[], int left, int right); 
   /* sort input lines */ 
   main() 
   { 
   } 
       int nlines;     /* number of input lines read */ 
       if ((nlines = readlines(lineptr, MAXLINES)) >= 0) { 
           qsort(lineptr, 0, nlines-1); 
           writelines(lineptr, nlines); 
           return 0; 
       } else { 
           printf("error: input too big to sort\n"); 
           return 1; 
       } 
   #define MAXLEN 1000  /* max length of any input line */ 
   int getline(char *, int); 
   char *alloc(int); 
   /* readlines:  read input lines */ 
   int readlines(char *lineptr[], int maxlines) 
   { 
       int len, nlines; 
       char *p, line[MAXLEN]; 
       nlines = 0; 
       while ((len = getline(line, MAXLEN)) > 0) 
           if (nlines >= maxlines || p = alloc(len) == NULL) 
               return -1; 
           else { 
98 
               line[len-1] = '\0';  /* delete newline */ 
               strcpy(p, line); 
               lineptr[nlines++] = p; 
           } 
       return nlines; 
   } 
   /* writelines:  write output lines */ 
   void writelines(char *lineptr[], int nlines) 
   { 
       int i; 
       for (i = 0; i < nlines; i++) 
           printf("%s\n", lineptr[i]); 
   }
   
```


## Multidimensional Arrays

- If a two-dimensional array is to be passed to a function, the parameter declaration in the function must include the number of columns; the number of rows is irrelevant, since what is passed is, as before, a pointer to an array of rows, where each row is an array of 13 ints. In this particular case, it is a pointer to objects that are arrays of 13 ints. Thus if the array daytab is to be passed to a function f, the declaration of f would be: f(int daytab\[2]\[13]) { ... } It could also be f(int daytab\[]\[13]) { ... } since the number of rows is irrelevant, or it could be f(int (\*daytab)\[13]) { ... }
- pointers plays their role here as well think like 2d arrays are indirectly array  of two pointers pointing to two different arrays.


## Pointers vs Multidimensional Arrays

## Pointers to functions
- Use to know more

```c
#include <stdio.h> 
   #include <string.h> 
   #define MAXLINES 5000     /* max #lines to be sorted */ 
   char *lineptr[MAXLINES];  /* pointers to text lines */ 
   int readlines(char *lineptr[], int nlines); 
   void writelines(char *lineptr[], int nlines); 
   void qsort(void *lineptr[], int left, int right, 
              int (*comp)(void *, void *)); 
   int numcmp(char *, char *); 
   /* sort input lines */ 
   main(int argc, char *argv[]) 
   { 
       int nlines;        /* number of input lines read */ 
       int numeric = 0;   /* 1 if numeric sort */ 
       if (argc > 1 && strcmp(argv[1], "-n") == 0) 
           numeric = 1; 
       if ((nlines = readlines(lineptr, MAXLINES)) >= 0) { 
           qsort((void**) lineptr, 0, nlines-1, 
             (int (*)(void*,void*))(numeric ? numcmp : strcmp)); 
           writelines(lineptr, nlines); 
107 
           return 0; 
       } else { 
           printf("input too big to sort\n"); 
           return 1; 
       } 
   }
```


- In the call to qsort, strcmp and numcmp are addresses of functions. Since they are known to be functions, the & is not necessary, in the same way that it is not needed before an array name.

## Complicated Declarations

- The syntax is an attempt to make the declaration and the use agree; it works well for simple cases, but it can be confusing for the harder ones, because declarations cannot be read left to right, and because parentheses are over-used. The difference between int \*f(); \* f: function returning pointer to int \*/ and int (\*pf)(); /\* pf: pointer to function returning int \*/ 109 illustrates the problem: * is a prefix operator and it has lower precedence than (), so parentheses are necessary to force the proper association.

```c
char **argv 
    argv:  pointer to char 
int (*daytab)[13] 
    daytab:  pointer to array[13] of int 
int *daytab[13] 
    daytab:  array[13] of pointer to int 
void *comp() 
    comp: function returning pointer to void 
void (*comp)() 
    comp: pointer to function returning void 
char (*(*x())[])() 
    x: function returning pointer to array[] of 
    pointer to function returning char 
char (*(*x[3])())[5] 
    x: array[3] of pointer to function returning 
    pointer to array[5] of char 
```



# Commandline Arguments

- When main is called, it is called with two arguments. The first (conventionally called argc, for argument count) is the number of command-line arguments the program was invoked with; the second (argv, for argument vector) is a pointer to an array of character strings that contain the arguments, one per string. We customarily use multiple levels of pointers to manipulate these character strings.
- When main is called, it is called with two arguments. The first (conventionally called argc, for argument count) is the number of command-line arguments the program was invoked with; the second (argv, for argument vector) is a pointer to an array of character strings that contain the arguments, one per string. We customarily use multiple levels of pointers to manipulate these character strings.
- ***See it thoroughly after learning all the concepts.***
- Very important for developing commandline softs





# What i would like to say is pointers is in itself a very big topic and i think that the whole chapters is essential so do not miss any part. That's why i am not including any further notes on pointers



# How to make the code take arguments in the commandline.
```c
 #include <stdio.h> 
   /* echo command-line arguments; 1st version */ 
   main(int argc, char *argv[]) 
   { 
       int i; 
       for (i = 1; i < argc; i++) 
           printf("%s%s", argv[i], (i < argc-1) ? " " : ""); 
       printf("\n"); 
       return 0; 
   } 
```







# Pointers

- Every byte in the computer have a address and it starts from 0.
- integers occupy 4 byte of memory
- character 2 byte
- float takes two bytes

- Every byte have 8 bits i.e. 8 zeors or ones and alll the variables are stored in 0/1 form.

Pinters are variables that store address of another variable.


int \*p --> to declare a pointer
p=&a --> to get address of a in p
we can also get the address of pointers.

print(\*p)--> prints the value at p pointer
\*p means value at address p.

int**  or \*\*p
This is a pointer to a adress of another pointer

int \*\*\*\*\* pointer to pointer to.........


# Pointers and 2-D arrays 

- very complicated concept so try practicing it
- how to give 2d and 3d arrays into arguments.
- second and third brackets should provide how many elements are there.
- 



