class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cur_max = 1
        cur_min = 1

        for i in nums:
            if i == 0:
                cur_min, cur_max = 1, 1
                continue
            max_temp = cur_max
            cur_max = max(cur_max * i, cur_min * i, i)
            cur_min = min(max_temp * i, cur_min * i, i)
            res = max(res, cur_max)
        
        return res