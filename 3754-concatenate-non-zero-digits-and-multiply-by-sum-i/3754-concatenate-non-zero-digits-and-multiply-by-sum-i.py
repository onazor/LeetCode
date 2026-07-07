class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        
        string = ''
        string_orig = str(n)
        total_sum = 0
        for char in string_orig:
            if char != '0':
                total_sum += int(char)
                string += char
        return int(string)*total_sum