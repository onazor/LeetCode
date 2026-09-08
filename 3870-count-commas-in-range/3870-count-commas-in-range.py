class Solution:
    def countCommas(self, n: int) -> int:
        count = 0
        start = 1000
        while start >= 1000 and start <= n:
            count += 1
            start += 1
        
        return count
