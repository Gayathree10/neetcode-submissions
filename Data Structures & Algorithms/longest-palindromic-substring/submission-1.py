class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0

        for i in range(len(s)):
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left > end - start:
                    start, end = left, right
                left -= 1
                right += 1
            
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left > end - start:
                    start, end = left, right
                left -= 1
                right += 1

        return s[start: end + 1]