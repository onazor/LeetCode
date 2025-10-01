class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        if numExchange > numBottles:
            return 0

        total = numBottles
        while numBottles >= numExchange:
            print(numBottles)
            remainder = numBottles % numExchange
            quotient = numBottles // numExchange
            total += quotient
            numBottles = remainder + quotient
        return total
