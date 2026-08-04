class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        minimum = min(nums)
        maximum = max(nums)
        ans = []
        for i in range(minimum, maximum+1):
            if i not in nums:
                ans.append(i)
        
        return ans
