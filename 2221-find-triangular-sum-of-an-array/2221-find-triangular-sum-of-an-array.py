class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            temp = [0]*(len(nums)-1)
            for i in range(len(nums)-1):
                temp[i] = (nums[i]+nums[i+1]) % 10
            nums = temp
            return self.triangularSum(nums)

