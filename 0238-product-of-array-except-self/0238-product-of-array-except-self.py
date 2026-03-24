class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix_array = [1] * length
        suffix_array = [1] * length
        product_array = [1] * length

        prefix_product = nums[0]
        for idx in range(1, length):
            prefix_array[idx] = prefix_product
            prefix_product *= nums[idx]

        suffix_product = nums[-1]
        for idx in reversed(range(length - 1)):
            suffix_array[idx] = suffix_product
            suffix_product *= nums[idx]
        
        for idx in range(length):
            product_array[idx] = prefix_array[idx] * suffix_array[idx]
        
        return product_array
