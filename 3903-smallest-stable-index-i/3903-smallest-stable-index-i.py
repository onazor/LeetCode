class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        score_current = float('inf')
        min_idx = len(nums)
        for i in range(len(nums)):
            maximum = max(nums[:i+1])
            minimum = min(nums[i:])
            score = maximum-minimum
            if score <= k:
                score_current = score
                min_idx = min(min_idx, i)
            
        if min_idx == len(nums):
            return -1
    
        return min_idx
            
        