class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        if len(nums) == 1:
            if nums[0] == 0:
                return 0
            else:
                return 1

        if sum(nums) == 0:
            return 0
            
        xor_all = 0
        for num in nums:
            xor_all = xor_all ^ num
        
        length = len(nums) 
        idx = 0
        while xor_all == 0:
            if idx < len(nums) and (xor_all ^ nums[idx] != 0):
                xor_all = xor_all ^ nums[idx]
                length -= 1
            idx += 1

        if xor_all == 0:
            return 0

        return length