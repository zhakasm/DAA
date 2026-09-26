# First Bad Version

## 1. Problem

There are `n` versions of a product.

At some point, one version becomes bad. Every version after the first bad version is also bad.

The goal is to find the first bad version.

We can use the provided `isBadVersion(version)` API to check whether a particular version is bad.

## 2. Approach

I decided to start with a simple linear search.

The algorithm checks versions starting from version `1`.

For each version, it calls `isBadVersion()`:

* If the version is not bad, the algorithm continues to the next version.
* If the version is bad, it returns that version immediately.

Because all versions after the first bad version are also bad, the first bad version found is the answer.

## 3. Time Complexity

**Time Complexity: O(n)**

In the worst case, the first bad version can be version `n`.

Then the algorithm has to check all `n` versions before finding it.

Therefore, the number of API calls can grow linearly with `n`, giving a time complexity of `O(n)`.

## 4. Space Complexity

**Space Complexity: O(1)**

The algorithm only stores the current version number.

It does not create an additional array, list, or other data structure whose size depends on `n`.

Therefore, the additional space complexity is `O(1)`.

## 5. Reflection / Improvement

There is a more efficient approach because the versions have a special property:

Once a version is bad, all versions after it are also bad.

This means the versions can be viewed as two groups:

`good good good good bad bad bad`

We can use binary search to find the boundary between the good and bad versions.

Instead of checking every version, we check the middle version and decide which half can be discarded.

The improved solution can achieve:

**Time Complexity: O(log n)**

**Space Complexity: O(1)**

The main improvement is reducing the number of calls to `isBadVersion()` from potentially `n` calls to approximately `log₂(n)` calls.
