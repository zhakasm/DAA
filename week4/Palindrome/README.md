# 4. Palindrome Linked List

## 1. Problem
Determine whether the sequence of values in a linked list reads the same forward and backward.

## 2. Approach
I use slow and fast pointers to find the middle of the list. Then I reverse the second half and compare it with the first half, one node at a time.

- `slow` moves one step and `fast` moves two steps, so `slow` reaches the middle.
- If the list length is odd, `fast` is not `null` at the end; I skip the middle node because it does not need to be compared.
- I reverse the second half using three pointers: `previous`, `current`, and `nextNode`.
- I compare values from the beginning and from the reversed half. Any mismatch means the list is not a palindrome.

### Trace
Input: `1 -> 2 -> 2 -> 1`

1. Slow/fast pointers locate the start of the second half at the second `2`.
2. Reverse the second half: its traversal order becomes `1 -> 2`.
3. Compare the first half (`1`, then `2`) with the reversed half (`1`, then `2`).
4. Both comparisons match, so return `true`.

For input `1 -> 2`, the reversed second half starts at `2`; comparing `1` with `2` finds a mismatch, so return `false`.

### Testing and possible challenge
Test an even-length palindrome (`1 -> 2 -> 2 -> 1`), an odd-length palindrome (`1 -> 2 -> 3 -> 2 -> 1`), a non-palindrome (`1 -> 2`), and a list with one node. Be careful to skip the middle node for odd-length lists. This implementation reverses part of the input list; if preserving the original links is required, the list should be restored before returning. Only describe a difficulty as something you personally faced if it matches your experience.

## 3. Complexity
- **Time: O(n)** — finding the middle, reversing the second half, and comparing values each take at most linear time. Their total is O(n).
- **Space: O(1)** — the algorithm uses a fixed number of pointers and reverses links in place.

## 4. Reflection / Improvement
A simpler first approach is to copy values into an array and compare from both ends. That takes O(n) time but O(n) extra space. The current approach achieves O(n) time and O(1) extra space. One possible improvement is to reverse the second half back after comparison so the input list is restored.
