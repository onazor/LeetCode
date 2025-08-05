class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        count = 0
        for fruit in fruits:
            unset = 1
            for idx in range(len(baskets)):
                if baskets[idx] >= fruit:
                    unset = 0
                    baskets[idx] = -1
                    break
            count += unset
        
        return count