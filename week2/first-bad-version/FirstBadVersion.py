class Solution:
    def firstBadVersion(self, n):
        for version in range(1, n + 1):
            if isBadVersion(version):
                return version
