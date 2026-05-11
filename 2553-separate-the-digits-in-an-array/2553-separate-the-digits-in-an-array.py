class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        separated = []
        for num in nums:
            for char in str(num):
                separated.append(int(char))
        
        return separated