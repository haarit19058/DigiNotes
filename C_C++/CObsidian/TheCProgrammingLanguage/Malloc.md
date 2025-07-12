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