Channel for algorithm


# Insertion sort
- Put the next number in  it correct place in the stored array using swaps.
- Its time complexity is roughly n$^2$.
- To do superscipt and subscript in obsidai$_n$.
- 

```python
def sort(l):
    for i in range(len(l)):
        j=i
        while j>=1:
            if l[j]<l[j-1]:
                l[j],l[j-1]=l[j-1],l[j]
            else:
                break
            j-=1
    return l
        
l=[4,3,7,3,0,7,8,5,2]
print(sort(l))
```




# Que : Merge two sorted arrays

If two sorted are given then write a efficient algo to sort the union of both the arrays.
- time complexity is = c(len(A)+len(B))=O(Max{len(A),len(B)})
Solution:

```python
def merge(left, right):

i = 0
j = 0
merged = []

while i < len(left) and j < len(right):

	if left[i] < right[j]:
		merged.append(left[i])
		i += 1
	else:
		merged.append(right[j])
		j += 1

# Checking if any elements are left
while i < len(left):
	merged.append(left[i])
	i += 1

while j < len(right):
	merged.append(right[j])
	j += 1

return merged


```

# Merge Sort


- Merge sort is not  a in place sorting algorithm it means that it makes new arrays while sorting.
-  time complexity of it is log(n).
- time  complexity is T(n)= 2T(n/2)+cn
- T(1)=c


- do this k times 
- T(n)=2$^k$T(n/2$^k$)+kcn

- we will hit the base case when k will be log(n)
	- n,n/2,,n/4,.......
	- n/2$^k$=1
	- k=log$_2$n    the number of levels.
	- this is the k in above equation.
- so the running time of merge sort is nlogn
- 

```python
def merge(left, right):

	i = 0
    j = 0
    merged = []

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Checking if any elements are left
    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


def merge_sort(arr):
	if len(arr) > 1:
	
		# Finding the mid of the array
		mid = len(arr) // 2
	
		# Parting the array into two halves
		left = merge_sort(arr[:mid])
		right = merge_sort(arr[mid:])
	
		# Merge the sorted halves
		arr = merge(left, right)
	
	return arr
```

# Quick Sort

- Worst case input.
	- It is very bad at sorting the already sorted array.  
	- time complexity for this is O(n$^2$)
- Best Case
	- if the pivot always lmagically lands in the middle, then Quicksort behaves like mergesort.
- Best Case nlogn
- Worst Case n$^2$
- Average Case nlogn



- the tricky part is the partition function should run with single for loop.



```python
def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high

    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            # Swap arr[left] and arr[right]
            arr[left], arr[right] = arr[right], arr[left]

    # Swap pivot with arr[right]
    arr[low], arr[right] = arr[right], arr[low]

    return right

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
n = len(arr)
quick_sort(arr, 0, n - 1)

print("Sorted array:", arr)

```


# Finding the kth minimum
# QuickSelect
# BinarySearch






