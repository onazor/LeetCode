class Solution:
    def minElement(self, nums: List[int]) -> int:
        sum_list = []
        for num in nums:
            split = list(str(num))
            total = 0
            for char in split:
                total += int(char)
            sum_list.append(total)
        return min(sum_list)