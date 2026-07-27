class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = -1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    product = (nums[i]-1)*(nums[j]-1)
                    max_prod = max(max_prod, product)
        
        return max_prod