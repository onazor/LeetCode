class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        good_tuples = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                for k in range(j, len(nums)):
                    if (i != j and j !=k) and (nums[i] == nums[j] and nums[j] == nums[k]):
                        good_tuples.append((i, j, k))
        
        minimum = 1000000

        if not good_tuples:
            return -1

        for triple in good_tuples:
            current = abs(triple[0]-triple[1])+abs(triple[1]-triple[2])+abs(triple[2]-triple[0])
            minimum = min(minimum, current)

        return minimum
