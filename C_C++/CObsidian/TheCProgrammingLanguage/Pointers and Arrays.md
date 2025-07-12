

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


## Adress Arithmetic

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

## Character pointers and functions


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


