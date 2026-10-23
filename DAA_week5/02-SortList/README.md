# 2. Sort List

## 1. Problem
Sort a singly linked list into ascending order without converting the list into an array.

## 2. Approach
I use Merge Sort, which works well for linked lists.

1. If the list has zero or one node, it is already sorted.
2. Use slow and fast pointers to find the middle.
3. Cut the list into two smaller lists.
4. Recursively sort each half.
5. Merge the two sorted halves by repeatedly attaching the smaller front node to the result.

### Trace
Input: `4 -> 2 -> 1 -> 3`

1. Find the middle and split into `4 -> 2` and `1 -> 3`.
2. Split `4 -> 2` into `4` and `2`. Each one-node list is already sorted, so merge them as `2 -> 4`.
3. Split `1 -> 3` into `1` and `3`. Merge them as `1 -> 3`.
4. Merge `2 -> 4` and `1 -> 3`:
   - Compare `2` and `1`: take `1`.
   - Compare `2` and `3`: take `2`.
   - Compare `4` and `3`: take `3`.
   - Attach the remaining `4`.
5. Final list: `1 -> 2 -> 3 -> 4`.

### Testing and challenges
Test an empty list, one node, already sorted values, reverse order, duplicate values, and negative values. A key detail is cutting the list at the midpoint (`beforeSlow.next = null`); without cutting, recursive calls may keep receiving the same list and never reach the base case. Check midpoint logic for both even and odd lengths. Only describe difficulties you actually encountered.

## 3. Complexity
- **Time: O(n log n)** — each recursion level splits the list into halves. Merging across one level processes all `n` nodes in O(n) time, and there are O(log n) levels.
- **Space: O(log n)** auxiliary call-stack space for recursive calls. The merge relinks existing nodes and uses O(1) extra node storage.

## 4. Reflection / Improvement
Merge Sort is a standard efficient approach for linked lists and gives O(n log n) time. Copying values into an array, sorting it, and writing values back can also take O(n log n) time but requires O(n) extra space. This implementation avoids the extra array and preserves the original nodes by relinking them.
