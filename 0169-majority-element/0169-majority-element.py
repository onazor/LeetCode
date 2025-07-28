from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        data = Counter(nums)
        majority = data.most_common(1)
        return majority[0][0]