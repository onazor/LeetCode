class Solution:
    def binaryGap(self, n: int) -> int:
        longest_distance = 0
        while n & 1 == 0:
            n = n >> 1
        binary_string = bin(n)[2:]
        if len(binary_string) == 1:
            return 0

        max_gap = 0
        current_gap = 0
        for bit in binary_string:
            if bit == "1":
                max_gap = max(current_gap, max_gap)
                current_gap = 0
            else:
                current_gap += 1

        
        return max_gap + 1