class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        min_len = float('inf')

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                total -= nums[left]
                min_len = min(min_len, right - left + 1)
                left += 1
                
        return 0 if min_len == float('inf') else min_len