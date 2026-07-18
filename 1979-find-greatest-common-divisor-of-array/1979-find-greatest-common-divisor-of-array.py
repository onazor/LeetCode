class Solution:
    def gcf(self, x: int, y: int) -> int:
        if x > y:
            while x % y != 0:
                rem = x % y
                x = y
                y = rem
            return y
        else:
            while y % x != 0:
                rem = y % x
                y = x
                x = rem
            return x

    def findGCD(self, nums: List[int]) -> int:
        minimum_num = min(nums)
        maximum_num = max(nums)
        return self.gcf(minimum_num, maximum_num)
        