In competitive programming, you often need to perform input and output operations quickly. Here are some commonly used functions from `stdio.h` in C for competitive programming:

1. **printf:**
   - Purpose: Print formatted output to the standard output (usually the console).
   - Example: `printf("Hello, %s!\n", "World");`

2. **scanf:**
   - Purpose: Read formatted input from the standard input (usually the keyboard).
   - Example: `scanf("%d", &num);`

3. **fprintf:**
   - Purpose: Write formatted output to a file.
   - Example: `fprintf(file_pointer, "This is a formatted output\n");`

4. **fscanf:**
   - Purpose: Read formatted input from a file.
   - Example: `fscanf(file_pointer, "%d", &num);`

5. **getchar:**
   - Purpose: Read a character from the standard input.
   - Example: `char c = getchar();`

6. **putchar:**
   - Purpose: Write a character to the standard output.
   - Example: `putchar('A');`

7. **puts:**
   - Purpose: Write a string to the standard output, followed by a newline character.
   - Example: `puts("Hello, World!");`

8. **gets:**
   - Purpose: Read a line from the standard input.
   - Example: `char buffer[100]; gets(buffer);`

9. **fgets:**
   - Purpose: Read a line from a file or standard input.
   - Example: `fgets(buffer, sizeof(buffer), stdin);`

10. **fclose:**
    - Purpose: Close a file.
    - Example: `fclose(file_pointer);`

11. **feof:**
    - Purpose: Check for the end-of-file indicator.
    - Example: `while (!feof(file_pointer)) { /* process file */ }`

These are just a subset of functions available in `stdio.h`. Depending on the specific needs of your program, you may use additional functions. Keep in mind that in competitive programming, efficiency and simplicity are crucial, so choose functions wisely based on the problem requirements.











# standard lib

Listing all the functions in the C Standard Library would be quite extensive, as there are many functions available for various purposes. However, I can provide you with a categorized overview of some commonly used functions in the C Standard Library. Note that this is not an exhaustive list, but it covers a broad range of functionalities:

### Input/Output (stdio.h):
- `printf`
- `scanf`
- `sprintf`
- `sscanf`
- `fprintf`
- `fscanf`
- `getchar`
- `putchar`
- `puts`
- `fgets`
- `fputs`
- `fgetc`
- `fputc`
- `fclose`
- `feof`

### String Handling (string.h):
- `strlen`
- `strcpy`
- `strncpy`
- `strcat`
- `strncat`
- `strcmp`
- `strncmp`
- `strchr`
- `strrchr`
- `strstr`
- `strtok`
- `memcpy`
- `memcmp`
- `memset`

### Dynamic Memory Management (stdlib.h):
- `malloc`
- `calloc`
- `realloc`
- `free`
- `atoi`
- `atol`
- `atof`
- `rand`
- `srand`
- `exit`
- `abort`
- `qsort`
- `bsearch`

### Math (math.h):
- `sqrt`
- `pow`
- `fabs`
- `ceil`
- `floor`
- `sin`, `cos`, `tan`
- `asin`, `acos`, `atan`
- `exp`, `log`
- `round`
- `rand`

### Character Handling (ctype.h):
- `isalpha`
- `isdigit`
- `isalnum`
- `islower`
- `isupper`
- `tolower`
- `toupper`

### Time and Date (time.h):
- `time`
- `ctime`
- `localtime`
- `gmtime`
- `mktime`
- `strftime`

These are just a few examples, and there are many more functions available in the C Standard Library. If you have a specific area or functionality in mind, feel free to ask for more details!