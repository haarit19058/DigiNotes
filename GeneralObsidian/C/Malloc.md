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