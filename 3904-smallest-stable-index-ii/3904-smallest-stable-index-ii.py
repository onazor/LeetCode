class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        dictionary = {}
        maximum_idx = float('-inf')
        minimum_idx = float('inf')
        length = len(nums)

        # initialize
        for i in range(length):
            dictionary[i] = [0,0]

        min_idx = float('inf')
        for idx in range(length):
            max_current = max(maximum_idx, nums[idx])
            maximum_idx = max_current

            dictionary[idx][0] = max_current
        
            min_current = min(minimum_idx, nums[length-idx-1])
            minimum_idx = min_current

            dictionary[length-1-idx][1] = min_current
        
        for idx in dictionary:
            current = dictionary[idx][0] - dictionary[idx][1]
            if current <= k:
                min_idx = min(min_idx, idx)
        
        if min_idx == float('inf'):
            return -1
        return min_idx
