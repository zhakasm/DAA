# 3. Remove Linked List Elements

## 1. Problem
Given a linked list and a value `val`, remove every node whose value equals `val`, then return the possibly changed head.

## 2. Approach
I create a dummy node before the original head. This handles cases where the original first node must be removed. `current` checks the node after itself:

- If `current.next.val == val`, skip that node.
- Otherwise, move `current` forward.
- Return `dummy.next`, which points to the new head.

### Trace
Input: `1 -> 2 -> 6 -> 3 -> 6`, `val = 6`

1. `current` starts at the dummy node. The next value is `1`, so move to `1`.
2. The next value is `2`, so move to `2`.
3. The next value is `6`, so skip it. The list becomes `1 -> 2 -> 3 -> 6`.
4. The next value is `3`, so move to `3`.
5. The next value is `6`, so skip it.
6. The result is `1 -> 2 -> 3`.

### Testing and possible challenge
Test an empty list, no matching values, all values matching, and matching values at the beginning and end. The dummy node helps avoid a separate special case for deleting the head. After deleting a node, do not move `current` immediately: the next node may also have the target value. Only describe this as a challenge you faced if it matches your experience.

## 3. Complexity
- **Time: O(n)** — the algorithm checks each node at most once.
- **Space: O(1)** — the dummy node and pointer use constant extra space.

## 4. Reflection / Improvement
The solution is already O(n) time and O(1) extra space. A recursive solution is possible, but it uses O(n) call-stack space in the worst case, so it is not better in space complexity.
