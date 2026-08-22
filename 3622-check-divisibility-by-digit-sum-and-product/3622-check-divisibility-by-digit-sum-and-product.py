import math

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        return n % (sum([int(char) for char in list(str(n))]) + math.prod([int(char) for char in list(str(n))])) == 0