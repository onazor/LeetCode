class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        result = []
        for i in range(1, len(nums)-1):
            idx_left = i-1
            idx_right = i+1

            while nums[i] == nums[idx_left] and idx_left > 0:
                idx_left -= 1

            while nums[i] == nums[idx_right] and idx_right < len(nums)-1:
                idx_right += 1
            
            if (nums[idx_left] != nums[i]) and (nums[idx_right] != nums[i]):
                if (nums[i] > nums[idx_right]) and (nums[i] > nums[idx_left]):
                    result.append('h')
                elif (nums[i] < nums[idx_right]) and (nums[i] < nums[idx_left]):
                    result.append('v')
        
        if result:
            modified = [result[0]]
        else:
            return 0
            
        for i in range(1, len(result)):
            if result[i] != result[i-1]:
                modified.append(result[i])

        return len(modified)

