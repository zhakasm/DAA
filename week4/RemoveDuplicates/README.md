# 1. Remove Duplicates from Sorted List

## 1. Problem
Given a sorted linked list, remove repeated values so each value appears only once. Keep the original order.

## 2. Approach
I use a pointer called `current` to inspect adjacent nodes. Because the list is sorted, duplicate values are next to each other.

- If `current.val == current.next.val`, I skip the next node by setting `current.next = current.next.next`.
- Otherwise, I move `current` to the next node.
- I return `head`, which is still the start of the list.

### Trace
Input: `1 -> 1 -> 2 -> 3 -> 3`

1. `current` is at the first `1`. The next value is also `1`, so skip the second node: `1 -> 2 -> 3 -> 3`.
2. The next value is `2`, so move `current` to `2`.
3. `2` and `3` differ, so move `current` to `3`.
4. The two `3` values match, so skip the last node.
5. The result is `1 -> 2 -> 3`.

### Testing and possible challenge
Test an empty list, a list without duplicates, duplicates at the beginning/end, and several equal values in a row. One easy mistake is moving `current` after deleting a duplicate; that can skip checking a repeated value that is still next to it. Only describe this as a challenge you faced if it matches your own testing experience.

## 3. Complexity
- **Time: O(n)** — each node is visited a constant number of times, so work grows linearly with the number of nodes.
- **Space: O(1)** — the algorithm uses only a fixed number of pointer variables and changes links in place.

## 4. Reflection / Improvement
The solution is already optimal for time because every node may need to be checked. It also uses constant extra space. No asymptotic improvement is needed.
