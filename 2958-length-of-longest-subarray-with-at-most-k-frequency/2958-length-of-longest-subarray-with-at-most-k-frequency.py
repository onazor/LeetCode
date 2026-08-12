class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq_dict = {}
        for num in nums:
            freq_dict[num] = 0

        max_length = 0
        left = 0

        for right in range(len(nums)):
            current_num = nums[right]
            freq_dict[current_num] += 1

            while freq_dict[current_num] > k:
                num_left = nums[left]
                freq_dict[num_left] -= 1
                left += 1
            
            window = right-left+1
            max_length = max(max_length, window)
        
        return max_length