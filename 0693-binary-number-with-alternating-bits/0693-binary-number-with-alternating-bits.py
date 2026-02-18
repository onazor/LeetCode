class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        check = (n << 1) & n
        print(bin(check)[2:])
        if check.bit_count() == 0:
            return True
        return False