class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        mapping_dicts = {}
        for i in range(len(nums)):
            if nums[i] in mapping_dicts:
                mapping_dicts[nums[i]].append(i)
            else:
                mapping_dicts[nums[i]] = [i]
        
        minimum = float('inf')
        for key in mapping_dicts:
            if len(mapping_dicts[key]) >= 3:
                min_difference = float('inf')
                index = 0
                for i in range(len(mapping_dicts[key])-2):
                    current_dif = 2*(mapping_dicts[key][i+2]-mapping_dicts[key][i])
                    if current_dif < min_difference:
                        index = i
                        min_difference = current_dif
                current = 2*(mapping_dicts[key][index+2]-mapping_dicts[key][index])
                minimum = min(minimum, current)
        
        if minimum == float('inf'):
            return -1

        return minimum