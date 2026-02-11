class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        longest = 0
        for left in range(len(nums)):
            odd_dict = {}
            even_dict = {}
            for right in range(left, len(nums)):
                if nums[right] % 2 == 0:
                    even_dict[nums[right]] = even_dict.get(nums[right], 0) + 1
                else:
                    odd_dict[nums[right]] = odd_dict.get(nums[right], 0) + 1
            
                if len(odd_dict) == len(even_dict):
                    longest = max(longest, right-left+1)
        return longest

        
            