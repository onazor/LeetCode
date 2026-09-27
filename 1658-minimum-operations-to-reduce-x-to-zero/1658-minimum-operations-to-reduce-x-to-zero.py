class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        left = 0
        total_target = sum(nums) - x

        if total_target == 0:
            return len(nums)
        elif total_target < 0:
            return -1

        max_length = float('-inf')
        current_sum = 0
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum > total_target:
                current_sum -= nums[left]
                left += 1
            
            if current_sum == total_target:
                current_length = right - left + 1
                max_length = max(current_length, max_length)
        
        if max_length == float('-inf'):
            return -1

        return len(nums) - max_length

