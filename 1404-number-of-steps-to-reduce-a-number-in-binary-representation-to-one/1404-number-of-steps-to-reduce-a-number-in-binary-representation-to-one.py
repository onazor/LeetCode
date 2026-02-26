class Solution:
    def numSteps(self, s: str) -> int:
        binary_value = int(s, 2)
        operation = 0

        while binary_value != 1: 
            if binary_value & 1 == 1:
                binary_value += 1
                operation += 1
            else:
                binary_value = binary_value >> 1
                operation += 1
        return operation
        
