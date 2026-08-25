class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        multiple = 1
        while True:
            if multiple * k not in nums:
                return multiple * k
            multiple += 1