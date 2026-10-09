# 2. Intersection of Two Linked Lists

## 1. Problem
Given the heads of two linked lists, return the actual node where they first join. If they do not share a node, return `null`.

Important: intersection means the same node object in memory, not merely two nodes with equal values.

## 2. Approach
I use two pointers, `a` and `b`. Pointer `a` traverses list A and then list B; pointer `b` traverses list B and then list A. When a pointer reaches `null`, it starts at the other list's head. This makes both pointers travel the same combined distance.

The loop stops when the pointers reference the same node. That node is the intersection, or both are `null` if there is no intersection.

### Trace
Suppose list A is `4 -> 1 -> 8 -> 4 -> 5` and list B is `5 -> 6 -> 1 -> 8 -> 4 -> 5`, where both lists share the same node containing `8`.

- At first, `a` starts at A's `4` and `b` starts at B's `5`.
- Both move one node per iteration.
- When `a` reaches the end of A, it starts at B's head. When `b` reaches the end of B, it starts at A's head.
- After each pointer has traversed both lists' prefixes, the pointers align at the shared node `8`.
- The method returns the reference to that node.

If the lists do not intersect, both pointers eventually become `null`, so the loop ends and the method returns `null`.

### Testing and possible challenge
Test lists that intersect at the head, intersect near the end, have different lengths, or do not intersect. A common mistake is comparing `a.val == b.val`; equal values do not prove that the nodes are the same object. Only describe this as a challenge you faced if it matches your experience.

## 3. Complexity
Let `m` and `n` be the lengths of the lists.
- **Time: O(m + n)** — each pointer travels at most the length of both lists combined.
- **Space: O(1)** — only two pointer variables are used, regardless of list size.

## 4. Reflection / Improvement
A hash set could store every node from one list and then search the other list, also taking O(m + n) time but using O(m) extra space. The two-pointer method improves the auxiliary space to O(1), so it is preferable.
