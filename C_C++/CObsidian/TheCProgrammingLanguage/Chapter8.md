# The UNIX system

Very good chapter to start with linux dev. First I will complete the codes of chpters 1-7 and then will do chapter 8 thoroughly.


## File Descriptor

## Low Level I/O - Read and Write

### Chatgpt Explains

In the `read()` and `write()` functions used in Unix-like operating systems, including Linux and macOS, file descriptors are used to identify open files or other I/O resources. 

- The file descriptor `0` refers to the standard input (stdin). This is typically the keyboard.
- The file descriptor `1` refers to the standard output (stdout). This is typically the screen or terminal.

So, when `read(0, buf, BUFSIZ)` is called, it reads input from the standard input (keyboard) into the `buf` array. Similarly, `write(1, buf, n)` writes data from the `buf` array to the standard output (screen or terminal).

These file descriptors are predefined by the operating system and are available for use in any program.


This code is a simple C program that acts as a copy utility, reading input from the standard input (usually the keyboard) and writing it to the standard output (usually the screen). Let's break down the code:

```c
#include "syscalls.h"
```
This line includes a header file named "syscalls.h". This file likely contains declarations or definitions for system calls used in the program, such as `read()` and `write()`. 

```c
main()  /* copy input to output */ 
```
This is the main function of the program. However, it is missing a return type declaration (`int`, `void`, etc.), which is considered bad practice. By default, in C, if a function definition lacks a return type, it's assumed to return an `int`.

```c
{ 
    char buf[BUFSIZ]; 
    int n; 
```
Here, two variables are declared:
- `buf`: This is an array of characters (a string) with a size of `BUFSIZ`. `BUFSIZ` is a constant that represents the size of the buffer. It's typically defined in the standard library, usually as a large value that's suitable for most I/O operations.
- `n`: This is an integer variable used to store the number of characters read from the input.

```c
while ((n = read(0, buf, BUFSIZ)) > 0) 
```
This is a `while` loop that continuously reads input from the standard input (file descriptor `0`) using the `read()` system call. It reads up to `BUFSIZ` characters into the `buf` array. The `read()` function returns the number of characters read, or -1 if an error occurs. The loop continues as long as `read()` returns a positive value (indicating successful reading).

```c
write(1, buf, n); 
```
Within the loop, the program writes the contents of `buf` to the standard output (file descriptor `1`) using the `write()` system call. It writes `n` characters from the `buf` array.

```c
return 0; 
```
Finally, the `main()` function returns 0 to indicate successful completion of the program.

In summary, this program continuously reads input from the user and writes it back to the output until there is no more input, essentially acting as a simple copy utility. However, it's worth noting that this program lacks error handling, making it vulnerable to potential issues during I/O operations.


```c
  #include "syscalls.h" 
   main()  /* copy input to output */ 
   { 
       char buf[BUFSIZ]; 
       int n; 
       while ((n = read(0, buf, BUFSIZ)) > 0) 
           write(1, buf, n); 
       return 0; 
   } 
```

## Open, Creat, Close and Unlink

## Random Access - Lseek

## Example - An Example of Fopen and Getc

## Example - Listing Directories

## Example -  A storage Allocator

