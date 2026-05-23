class Solution:
    def check(self, nums: List[int]) -> bool:
        counter = 0

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                counter += 1
        if nums[-1] > nums[0]:
            counter += 1

        if counter >= 2:
            return False
        
        return True