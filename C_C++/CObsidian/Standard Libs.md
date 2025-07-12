# C stdlib

Certainly! Below is a list of standard libraries in C along with a brief description of their uses and some of their key functions:

1. **stdio.h**:
   - **Use**: Standard input-output operations.
   - **Key Functions**:
     - `printf()`: Outputs formatted data to the standard output (usually the console).
     - `scanf()`: Reads formatted data from the standard input (usually the keyboard).
     - `fprintf()`, `fscanf()`: Similar to `printf()` and `scanf()`, but operates on files.
     - `fgets()`, `fputs()`: Reads/writes strings from/to files or standard input/output.
     - `fopen()`, `fclose()`: Opens and closes files for reading or writing.
     - `fread()`, `fwrite()`: Reads and writes blocks of data to/from files.
     - `getc()`, `putc()`: Reads and writes individual characters from/to files.
     - `feof()`, `ferror()`: Checks end-of-file and error conditions for file operations.

2. **stdlib.h**:
   - **Use**: General utilities and memory management.
   - **Key Functions**:
     - `malloc()`, `calloc()`, `realloc()`, `free()`: Memory allocation and deallocation functions.
     - `rand()`, `srand()`: Generates pseudo-random numbers.
     - `exit()`, `abort()`: Terminate the program execution.
     - `system()`: Executes an operating system command.
     - `atoi()`, `atof()`, `atol()`: String to integer/float/long conversions.
     - `rand()`, `srand()`: Random number generation functions.
     - `qsort()`, `bsearch()`: Sorting and binary search functions.

3. **string.h**:
   - **Use**: String manipulation functions.
   - **Key Functions**:
     - `strlen()`: Calculates the length of a string.
     - `strcpy()`, `strncpy()`: Copies strings.
     - `strcat()`, `strncat()`: Concatenates strings.
     - `strcmp()`, `strncmp()`: Compares strings.
     - `strchr()`, `strrchr()`: Finds characters in strings.
     - `strstr()`: Finds substrings in strings.
     - `strtok()`: Splits strings into tokens.
     - `memset()`, `memcpy()`, `memmove()`: Memory manipulation functions.

4. **math.h**:
   - **Use**: Mathematical functions and constants.
   - **Key Functions**:
     - Trigonometric functions: `sin()`, `cos()`, `tan()`, `asin()`, `acos()`, `atan()`.
     - Exponential and logarithmic functions: `exp()`, `log()`, `log10()`, `pow()`.
     - Rounding functions: `ceil()`, `floor()`, `round()`.
     - Others: `sqrt()`, `fabs()`, `fmod()`.

5. **ctype.h**:
   - **Use**: Character classification and conversion functions.
   - **Key Functions**:
     - `isalpha()`, `isdigit()`, `isalnum()`: Checks if a character is alphabetic, numeric, alphanumeric, etc.
     - `isupper()`, `islower()`: Checks if a character is uppercase or lowercase.
     - `toupper()`, `tolower()`: Converts characters to uppercase or lowercase.
     - `isspace()`: Checks if a character is whitespace.

6. **time.h**:
   - **Use**: Date and time functions.
   - **Key Functions**:
     - `time()`: Gets the current calendar time.
     - `gmtime()`, `localtime()`: Converts time to UTC or local time.
     - `strftime()`: Formats time into a string.
     - `difftime()`: Computes the difference between two times.

7. **errno.h**:
   - **Use**: Error handling, provides error numbers for reporting errors that occur during program execution.

8. **assert.h**:
   - **Use**: Debugging, provides the `assert()` macro for checking assumptions during program execution.

These are some of the commonly used standard libraries in C, each serving various purposes to aid in programming tasks.









Certainly! Here's a brief explanation of each of the included libraries in your C++ code:

1. **`#include <cstdint>`**
   - This header file includes fixed-width integer types. It provides typedefs for integer types with a specified width, such as `int8_t`, `uint8_t`, `int16_t`, `uint16_t`, `int32_t`, `uint32_t`, `int64_t`, and `uint64_t`. These types are useful when you need integers of a specific size, which is important for portability and consistency across different platforms.

2. **`#include <fstream>`**
   - This header file includes classes and functions for handling file input and output. It provides the `std::ifstream` class for reading from files, `std::ofstream` class for writing to files, and `std::fstream` class for both reading and writing. It also includes functions for file stream manipulation.

3. **`#include <iomanip>`**
   - This header file includes functions and manipulators for stream input and output formatting. It provides manipulators such as `std::setw` (set width), `std::setprecision` (set precision), `std::setfill` (set fill character), and others. These manipulators are used to format the way data is displayed in streams, which is useful for creating neatly formatted output.

4. **`#include <iostream>`**
   - This header file includes standard input and output stream objects and functions. It provides the `std::cin` object for reading from the standard input (keyboard), `std::cout` object for writing to the standard output (console), and `std::cerr` object for writing error messages to the standard error stream. It also includes various stream manipulators for controlling input and output formatting.

5. **`#include <sstream>`**
   - This header file includes string stream classes for input and output operations on strings. It provides the `std::stringstream` class, which can be used to perform input and output operations on `std::string` objects. This is useful for converting between strings and other data types, and for manipulating strings as streams.

6. **`#include <string>`**
   - This header file includes the `std::string` class and related functions for handling and manipulating strings. The `std::string` class provides a way to store and manipulate sequences of characters. It includes functions for concatenation, comparison, searching, and other string operations.

In summary, these headers collectively provide the necessary tools for handling various aspects of input and output, both for files and streams, as well as for working with specific integer types and strings in a portable and consistent manner.




# STDLIB data structures


Here’s a table summarizing the basic operations along with their time complexities for the key data structures provided by the C++ Standard Library:



| Data Structure    | Operation                                         | Time Complexity          |
| ----------------- | ------------------------------------------------- | ------------------------ |
| **`std::vector`** | Access element by index                           | O(1)                     |
|                   | Insert or remove at end (`push_back`, `pop_back`) | O(1) amortized           |
|                   | Insert or remove in the middle                    | O(n)                     |
|                   | Search for an element (unsorted)                  | O(n)                     |
|                   | Search for an element (sorted)                    | O(log n) (binary search) |
|                   | Resizing                                          | O(n)                     |
|                   | Clear                                             | O(n)                     |

| **`std::list`** | Access element by position           | O(n)                   |
| --------------- | ------------------------------------ | ---------------------- |
|                 | Insert or remove at beginning or end | O(1)                   |
|                 | Insert or remove in the middle       | O(1) if position known |
|                 | Search for an element                | O(n)                   |
|                 | Clear                                | O(n)                   |

| **`std::deque`** | Access element by index              | O(1) |
| ---------------- | ------------------------------------ | ---- |
|                  | Insert or remove at beginning or end | O(1) |
|                  | Insert or remove in the middle       | O(n) |
|                  | Search for an element                | O(n) |
|                  | Clear                                | O(n) |

| **`std::stack`**    | Push (insert element at top)        | O(1)                   |
|----------------|---------------|--------------|
|                    | Pop (remove element from top)       | O(1)                   |
|                    | Access top element                  | O(1)                   |
|                    | Size                               | O(1)                   |
|                    | Empty                              | O(1)                   |

| **`std::queue`**    | Enqueue (insert element at back)    | O(1)                   |
|----------------|---------------|--------------|
|                    | Dequeue (remove element from front) | O(1)                   |
|                    | Access front element                | O(1)                   |
|                    | Size                               | O(1)                   |
|                    | Empty                              | O(1)                   |


| **`std::priority_queue`** | Push (insert element)    | O(log n) |
| ------------------------- | ------------------------ | -------- |
|                           | Pop (remove top element) | O(log n) |
|                           | Access top element       | O(1)     |
|                           | Size                     | O(1)     |
|                           | Empty                    | O(1)     |


| **`std::set` / `std::multiset`** | Insert                         | O(log n) |
| -------------------------------- | ------------------------------ | -------- |
|                                  | Remove element                 | O(log n) |
|                                  | Search for an element          | O(log n) |
|                                  | Access minimum/maximum element | O(1)     |
|                                  | Size                           | O(1)     |
|                                  | Clear                          | O(n)     |




| **`std::unordered_set`** | Insert                | O(1) average, O(n) worst case |
| ------------------------ | --------------------- | ----------------------------- |
|                          | Remove element        | O(1) average, O(n) worst case |
|                          | Search for an element | O(1) average, O(n) worst case |
|                          | Size                  | O(1)                          |
|                          | Clear                 | O(n)                          |




| **`std::map` / `std::multimap`** | Insert                       | O(log n) |
| -------------------------------- | ---------------------------- | -------- |
|                                  | Remove element by key        | O(log n) |
|                                  | Search for an element by key | O(log n) |
|                                  | Access element by key        | O(log n) |
|                                  | Size                         | O(1)     |
|                                  | Clear                        | O(n)     |



| **`std::unordered_map` / `std::unordered_multimap`** | Insert                       | O(1) average, O(n) worst case |
| ---------------------------------------------------- | ---------------------------- | ----------------------------- |
|                                                      | Remove element by key        | O(1) average, O(n) worst case |
|                                                      | Search for an element by key | O(1) average, O(n) worst case |
|                                                      | Access element by key        | O(1) average, O(n) worst case |
|                                                      | Size                         | O(1)                          |
|                                                      | Clear                        | O(n)                          |
|                                                      |                              |                               |

### Notes:
- For `std::unordered_set`, `std::unordered_map`, `std::unordered_multimap`, and `std::unordered_multiset`, the worst-case time complexities occur when many elements hash to the same bucket, leading to degraded performance.
- `std::set` and `std::map` maintain elements in sorted order, while their unordered counterparts do not guarantee order but offer faster average-case performance.
