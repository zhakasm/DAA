# 1. Sort an Array

## 1. Problem
Given an integer array, return its values in ascending order.

## 2. Approach
For this first solution, I use Java's built-in `Arrays.sort()` method. It sorts the array in place, so I return the same array afterward.

### Trace
Input: `[5, 2, 3, 1]`

1. Before sorting: `[5, 2, 3, 1]`
2. Call `Arrays.sort(nums)`. Java rearranges the elements into ascending order.
3. After sorting: `[1, 2, 3, 5]`
4. Return the sorted array.

This approach delegates the individual sorting iterations to Java's library, so its internal steps are not shown here.

### Testing and challenges
Useful tests include an already sorted array (`[1, 2, 3]`), reverse order (`[3, 2, 1]`), repeated values (`[4, 2, 4, 1]`), negative values, and a one-element array. If you tried a nested-loop approach first, describe what happened and how you tested it here. Do not claim to have tried something you did not actually try.

## 3. Complexity
- **Time: O(n log n)** — Java's primitive `int[]` sorting uses Dual-Pivot Quicksort, with O(n log n) typical performance and a guaranteed O(n log n) worst-case bound in modern Java implementations.
- **Space: implementation-dependent** — the library may use auxiliary stack space; this solution does not create a separate array in our code.

## 4. Reflection / Improvement
A manual algorithm such as Bubble Sort is easier to trace but takes O(n²) time. Merge Sort or Heap Sort can provide O(n log n) worst-case time. The built-in library method is concise and practical. If the assignment expects your own sorting algorithm, replace `Arrays.sort()` with an implementation such as Merge Sort and analyze that implementation instead.
