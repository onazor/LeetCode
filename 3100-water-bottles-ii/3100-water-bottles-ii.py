class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total = numBottles           
        empties = numBottles         
        k = numExchange              

        while empties >= k:
            empties -= k             
            total += 1               
            empties += 1             
            k += 1                   

        return total
