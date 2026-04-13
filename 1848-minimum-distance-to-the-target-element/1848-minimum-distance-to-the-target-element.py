class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        current_min = float('inf')
        for i in range(len(nums)):
            if nums[i] == target:
                current = abs(i-start)
                current_min = min(current_min, current)
        
        return current_min
