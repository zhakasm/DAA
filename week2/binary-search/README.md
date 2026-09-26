# Binary Search

## 1. Problem

We are given a sorted array of integers and a target value.

The goal is to find the index of the target in the array. If the target does not exist, the algorithm should return `-1`.

## 2. Approach

I decided to start with a simple linear search instead of using the optimal binary search approach.

The algorithm goes through the array from the first element to the last one.

For each element, it checks whether the element is equal to the target:

* If they are equal, the current index is returned.
* If the loop finishes without finding the target, the algorithm returns `-1`.

The fact that the array is sorted is not used in this first solution.

## 3. Time Complexity

**Time Complexity: O(n)**

In the worst case, the target can be the last element of the array or it may not exist at all.

In that case, the algorithm checks all `n` elements once.

Therefore, the number of operations grows linearly with the size of the array, so the time complexity is `O(n)`.

## 4. Space Complexity

**Space Complexity: O(1)**

The algorithm only uses a loop variable and does not create any additional data structures that depend on the size of the input.

Therefore, the additional space used is constant: `O(1)`.

## 5. Reflection / Improvement

There is a more efficient solution because the array is already sorted.

Instead of checking every element one by one, we can use binary search.

Binary search checks the middle element and determines whether the target is to the left or to the right. This allows us to discard approximately half of the remaining elements after each comparison.

The improved solution has:

**Time Complexity: O(log n)**

**Space Complexity: O(1)** if implemented iteratively.

The main improvement is using the sorted property of the array.
