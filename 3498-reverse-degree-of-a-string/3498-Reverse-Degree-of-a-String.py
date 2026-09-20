class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, ch in enumerate(s):
            reversed_val = 26 - (ord(ch) - ord('a'))
            total += reversed_val * (i + 1)
        return total