class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        ans = []
        for idx in range(len(nums)):
            to_char = map(int, list(str(nums[idx])))
            total_sum = 0
            for digit in to_char:
                total_sum += digit
                
            if total_sum == idx:
                return idx
        
        return -1
