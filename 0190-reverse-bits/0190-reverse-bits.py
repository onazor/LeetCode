class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for iteration in range(32):
            bit = n & 1
            res =  (res << 1) | bit
            n = n >> 1
        print(res)
        return res
