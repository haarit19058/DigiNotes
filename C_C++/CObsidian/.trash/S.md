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
