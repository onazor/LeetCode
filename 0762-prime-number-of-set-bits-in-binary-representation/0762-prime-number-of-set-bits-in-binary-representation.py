class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        for num in range(left, right+1):
            ones_count = num.bit_count()
            if ones_count in [2, 3, 5, 7, 11, 13, 17, 19]:
                count += 1
        return count
