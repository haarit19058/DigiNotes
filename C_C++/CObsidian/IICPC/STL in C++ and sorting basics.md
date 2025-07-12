## CHEAT SHEET GFG
https://www.geeksforgeeks.org/cpp-stl-cheat-sheet/

# For loop

```cpp
#include <iostream>

int main() {
    int arr[] = {1, 2, 3, 4, 5};  // Normal array of integers

    for (auto x : arr) {  // Range-based for loop
        std::cout << x << " ";
    }
    std::cout << "\n";

    return 0;
}

```

like in python
# Auto keyword in c++ stl 

In C++, the `auto` keyword is used to automatically deduce the type of a variable at compile-time, based on the initializer expression. This allows the programmer to avoid specifying the type explicitly, making the code cleaner and often easier to maintain.

Here are some examples of how `auto` can be used in C++:

1. **Basic Usage:**
   ```cpp
   auto x = 10;  // x is deduced to be of type int
   auto y = 3.14;  // y is deduced to be of type double
   ```

2. **With Pointers and References:**
   ```cpp
   int a = 5;
   int* p = &a;
   auto q = p;  // q is deduced to be of type int*

   int& r = a;
   auto s = r;  // s is deduced to be of type int (not int&)
   ```

3. **With Iterators:**
   ```cpp
   std::vector<int> vec = {1, 2, 3, 4, 5};
   for (auto it = vec.begin(); it != vec.end(); ++it) {
       // it is deduced to be of type std::vector<int>::iterator
       std::cout << *it << " ";
   }
   ```

4. **With Complex Types:**
   ```cpp
   std::map<int, std::string> m = {{1, "one"}, {2, "two"}};
   for (const auto& pair : m) {
       // pair is deduced to be of type const std::pair<const int, std::string>&
       std::cout << pair.first << ": " << pair.second << std::endl;
   }
   ```

5. **With Lambda Functions:**
   ```cpp
   auto lambda = [](int x, int y) { return x + y; };
   int sum = lambda(3, 4);  // sum is deduced to be of type int
   ```

### Benefits of Using `auto`

- **Reduces Boilerplate Code:** Eliminates the need to repeatedly type complex type names.
- **Enhances Code Readability:** Makes it easier to read and write code, especially when dealing with long and complex types.
- **Type Safety:** Ensures type safety as the type is determined by the compiler based on the initializer.

### Considerations

- **Explicitness:** Sometimes, explicitly stating the type can make the code more understandable, especially for someone who is not familiar with the context.
- **Type Inference:** The type deduced might not always be what is expected, especially with pointers and references. For example, `auto` does not deduce the reference type unless explicitly stated using `auto&`.

Using `auto` effectively requires understanding both its strengths and limitations. It can significantly enhance productivity and code readability when used appropriately.

# Basics of Time Complexity and Space Complexity

# Notes
- How to include the stl library
```cpp
#include <bits/stdc++.h>

using namespace std;

int main(){
return 0;
}
```
- the stl library contains all the necessary header files like vectors, strings etc.

# Sorting

### O(n$^2$) Algorithms

### 1. Bubble Sort (In-Place)
```cpp
#include <bits/stdc++.h>
using namespace std;

void bubbleSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1])
                swap(arr[j], arr[j+1]);
        }
    }
}

int main() {
    vector<int> arr = {64, 34, 25, 12, 22, 11, 90};
    bubbleSort(arr);
    for (int x : arr)
        cout << x << " ";
    return 0;
}
```

### 2. Insertion Sort (In-Place)
```cpp
#include <bits/stdc++.h>
using namespace std;

void insertionSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

int main() {
    vector<int> arr = {64, 34, 25, 12, 22, 11, 90};
    insertionSort(arr);
    for (int x : arr)
        cout << x << " ";
    return 0;
}
```

### 3. Selection Sort (In-Place)
```cpp
#include <bits/stdc++.h>
using namespace std;

void selectionSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n-1; i++) {
        int min_idx = i;
        for (int j = i+1; j < n; j++)
            if (arr[j] < arr[min_idx])
                min_idx = j;
        swap(arr[min_idx], arr[i]);
    }
}

int main() {
    vector<int> arr = {64, 34, 25, 12, 22, 11, 90};
    selectionSort(arr);
    for (int x : arr)
        cout << x << " ";
    return 0;
}
```

### 4. Merge Sort (Not In-Place)
```cpp
#include <bits/stdc++.h>
using namespace std;

void merge(vector<int>& arr, int l, int m, int r) {
    int n1 = m - l + 1;
    int n2 = r - m;

    vector<int> L(n1), R(n2);

    for (int i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

void mergeSort(vector<int>& arr, int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

int main() {
    vector<int> arr = {64, 34, 25, 12, 22, 11, 90};
    mergeSort(arr, 0, arr.size() - 1);
    for (int x : arr)
        cout << x << " ";
    return 0;
}
```

### 5. Quick Sort (In-Place)
```cpp
#include <bits/stdc++.h>
using namespace std;

int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[high];
    int i = (low - 1);
    for (int j = low; j <= high - 1; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return (i + 1);
}

void quickSort(vector<int>& arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

int main() {
    vector<int> arr = {64, 34, 25, 12, 22, 11, 90};
    quickSort(arr, 0, arr.size() - 1);
    for (int x : arr)
        cout << x << " ";
    return 0;
}
```

### 6. Binary Search
```cpp
#include <bits/stdc++.h>
using namespace std;

int binarySearch(vector<int>& arr, int l, int r, int x) {
    while (l <= r) {
        int m = l + (r - l) / 2;
        if (arr[m] == x)
            return m;
        if (arr[m] < x)
            l = m + 1;
        else
            r = m - 1;
    }
    return -1;
}

int main() {
    vector<int> arr = {2, 3, 4, 10, 40};
    int x = 10;
    int result = binarySearch(arr, 0, arr.size() - 1, x);
    if (result != -1)
        cout << "Element is present at index " << result;
    else
        cout << "Element is not present in array";
    return 0;
}
```

### 7. Finding kth Minimum Element (QuickSelect)
```cpp
#include <bits/stdc++.h>
using namespace std;

int partition(vector<int>& arr, int l, int r) {
    int pivot = arr[r];
    int i = l;
    for (int j = l; j < r; j++) {
        if (arr[j] <= pivot) {
            swap(arr[i], arr[j]);
            i++;
        }
    }
    swap(arr[i], arr[r]);
    return i;
}

int quickSelect(vector<int>& arr, int l, int r, int k) {
    if (l <= r) {
        int pi = partition(arr, l, r);
        if (pi == k)
            return arr[pi];
        else if (pi < k)
            return quickSelect(arr, pi + 1, r, k);
        else
            return quickSelect(arr, l, pi - 1, k);
    }
    return -1;
}

int main() {
    vector<int> arr = {12, 3, 5, 7, 19};
    int k = 2;
    cout << "K-th minimum element is " << quickSelect(arr, 0, arr.size() - 1, k);
    return 0;
}
```

### 8. Finding kth Maximum Element (QuickSelect)
```cpp
#include <bits/stdc++.h>
using namespace std;

int partition(vector<int>& arr, int l, int r) {
    int pivot = arr[r];
    int i = l;
    for (int j = l; j < r; j++) {
        if (arr[j] >= pivot) {
            swap(arr[i], arr[j]);
            i++;
        }
    }
    swap(arr[i], arr[r]);
    return i;
}

int quickSelect(vector<int>& arr, int l, int r, int k) {
    if (l <= r) {
        int pi = partition(arr, l, r);
        if (pi == k)
            return arr[pi];
        else if (pi < k)
            return quickSelect(arr, pi + 1, r, k);
        else
            return quickSelect(arr, l, pi - 1, k);
    }
    return -1;
}

int main() {
    vector<int> arr = {12, 3, 5, 7, 19};
    int k = 2;
    cout << "K-th maximum element is " << quickSelect(arr, 0, arr.size() - 1, k);
    return 0;
}
```

### Time and Space Complexity Table

| Algorithm                 | Best Time Complexity | Average Time Complexity | Worst Time Complexity | Space Complexity         |
| ------------------------- | -------------------- | ----------------------- | --------------------- | ------------------------ |
| Bubble Sort               | \(O(n)\)             | \(O(n^2)\)              | \(O(n^2)\)            | \(O(1)\) (in-place)      |
| Insertion Sort            | \(O(n)\)             | \(O(n^2)\)              | \(O(n^2)\)            | \(O(1)\) (in-place)      |
| Selection Sort            | \(O(n^2)\)           | \(O(n^2)\)              | \(O(n^2)\)            | \(O(1)\) (in-place)      |
| Merge Sort                | \(O(n \log n)\)      | \(O(n \log n)\)         | \(O(n \log n)\)       | \(O(n)\) (not in-place)  |
| Quick Sort                | \(O(n \log n)\)      | \(O(n \log n)\)         | \(O(n^2)\)            | \(O(\log n)\) (in-place) |
| Binary Search             | \(O(1)\)             | \(O(\log n)\)           | \(O(\log n)\)         | \(O(1)\)                 |
| QuickSelect (kth min/max) | \(O(n)\)             | \(O(n)\)                | \(O(n^2)\)            | \(O(\log n)\) (in-place) |



# Covered in lecture
## Vectors
## sort in stl

## imp function of stl

The Standard Template Library (STL) in C++ provides a wide range of containers and algorithms to work with. Here's a list of important functions and classes from the STL, categorized by containers, algorithms, and other utilities:

### Containers

1. **`std::vector`**: Dynamic array.
2. **`std::deque`**: Double-ended queue.
3. **`std::list`**: Doubly linked list.
4. **`std::forward_list`**: Singly linked list.
5. **`std::set`**: Ordered set (no duplicates).
6. **`std::multiset`**: Ordered multiset (allows duplicates).
7. **`std::map`**: Ordered map (key-value pairs, no duplicates).
8. **`std::multimap`**: Ordered multimap (key-value pairs, allows duplicates).
9. **`std::unordered_set`**: Unordered set (no duplicates).
10. **`std::unordered_multiset`**: Unordered multiset (allows duplicates).
11. **`std::unordered_map`**: Unordered map (key-value pairs, no duplicates).
12. **`std::unordered_multimap`**: Unordered multimap (key-value pairs, allows duplicates).
13. **`std::stack`**: LIFO (last-in, first-out) stack.
14. **`std::queue`**: FIFO (first-in, first-out) queue.
15. **`std::priority_queue`**: Priority queue (heap).

### Algorithms

1. **Sorting**:
   - `std::sort`
   - `std::stable_sort`
   - `std::partial_sort`
   - `std::nth_element`
2. **Searching**:
   - `std::find`
   - `std::binary_search`
   - `std::lower_bound`
   - `std::upper_bound`
   - `std::equal_range`
3. **Modifying**:
   - `std::copy`
   - `std::copy_if`
   - `std::transform`
   - `std::fill`
   - `std::replace`
4. **Numeric**:
   - `std::accumulate`
   - `std::inner_product`
   - `std::partial_sum`
   - `std::adjacent_difference`
5. **Set Operations**:
   - `std::set_union`
   - `std::set_intersection`
   - `std::set_difference`
   - `std::set_symmetric_difference`
6. **Heap**:
   - `std::make_heap`
   - `std::push_heap`
   - `std::pop_heap`
   - `std::sort_heap`
7. **Permutations**:
   - `std::next_permutation`
   - `std::prev_permutation`
8. **Miscellaneous**:
   - `std::reverse`
   - `std::rotate`
   - `std::shuffle`
   - `std::unique`

### Utilities

1. **Iterators**:
   - `std::begin`
   - `std::end`
   - `std::advance`
   - `std::distance`
2. **Functors**:
   - `std::less`
   - `std::greater`
   - `std::function`
   - `std::bind`
3. **Memory**:
   - `std::unique_ptr`
   - `std::shared_ptr`
   - `std::weak_ptr`
   - `std::make_unique` (C++14)
   - `std::make_shared` (C++11)
4. **Strings**:
   - `std::string`
   - `std::getline`
   - `std::to_string`
   - `std::stoi`, `std::stod`, etc.
5. **Random Numbers**:
   - `std::rand`
   - `std::srand`
   - `<random>` library (C++11)

### Miscellaneous

1. **`std::pair`**: Simple pair of values.
2. **`std::tuple`**: Collection of heterogeneous values.
3. **`std::chrono`**: Time utilities (C++11).
4. **`std::thread`**: Threading support (C++11).

These are some of the most commonly used functions and classes from the STL. They provide powerful tools for a wide range of tasks in C++ programming, from data manipulation to algorithm implementation and more.

## Pair


## Tuples

## Vector of vectors and vector of pairs and vector of tuples

## Strings

## Sets 

## Unordered Sets

## Multiset

## Iterators in sets

## Maps and Unordered maps
- similar to dictionary in python

# Advanced Data Sturctures
## Deque

## Stack

## Que

## Priority Que

## Bit Set

## Policy Based Data Structure (PDBS)




















# STL

# Vectors
