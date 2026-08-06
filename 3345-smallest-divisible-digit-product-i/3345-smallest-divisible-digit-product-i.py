class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        print(str(n))
        while True:
            string_n = str(n)
            product = 1
            for char in string_n:
                product *= int(char)
                
            if product % t == 0:
                return n
            
            n = n + 1

