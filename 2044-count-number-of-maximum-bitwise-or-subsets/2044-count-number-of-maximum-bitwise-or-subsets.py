class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return 1
        
        if len(nums) > 0 and len(set(nums)) == 1:
            return 2**len(nums) - 1

        # get the maximum bitwise OR in the list
        bitwise_val = 0
        for num in nums:
            bitwise_val |= num
        
        def count_bits(n):
            return bin(n).count('1')
        
        all_subsets = []
        n = len(nums)
        for mask in range(1 << n):
            for k in range(1, n+1):
                if count_bits(mask) == k:
                    subset = [nums[i] for i in range(n) if (mask >> i) & 1]
                    all_subsets.append(subset)
        
        count = 0
        for sub_set in all_subsets:
            bitwise_sub_val = 0
            for num in sub_set:
                bitwise_sub_val |= num
            
            if bitwise_sub_val == bitwise_val:
                count += 1
        
        return count

