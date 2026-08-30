class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minimum = min(nums)
        maximum = max(nums)

        for idx in range(len(nums)):
            if nums[idx] == minimum:
                idx_min = idx
            
            if nums[idx] == maximum:
                idx_max = idx
        
        max_left = idx_max+1
        max_right = len(nums)-idx_max
        min_left = idx_min+1
        min_right = len(nums)-idx_min

        # both front
        front = max(max_left, min_left)
        back = max(max_right, min_right)
        both = min(min_left, min_right) + min(max_left, max_right)

        return min(front, back, both)