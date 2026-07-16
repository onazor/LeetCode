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

    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        mx = [0] * n
        max_num = -1
        for i in range(n):
            if nums[i] > max_num:
                max_num = nums[i]
            mx[i] = max_num
        
        prefixgcd = [0] * n
        for i in range(n):
            prefixgcd[i] = self.gcf(nums[i], mx[i])
        
        prefixgcd.sort()
        to_sum = []
        for i in range(n // 2):
            to_sum.append(self.gcf(prefixgcd[i], prefixgcd[n-i-1]))

        return sum(to_sum)
        