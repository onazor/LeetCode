class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
            
        sum = 0
        for i in range(1, n+1):
            sum += i
            if sum > n:
                return i-1