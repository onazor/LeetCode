class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        longest = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i-1]:
                longest.append(nums[i])
            else: 
                break
        print(longest)
        total = sum(longest)
        while True:
            if total not in nums:
                return total
            else:
                total += 1 