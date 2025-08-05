class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        
        total = len(fruits)
        basket_idx = []
        for i in range(len(baskets)):
            basket_idx.append(i)

        for fruit in fruits:
            idx = 0
            print('fruit', fruit)
            print('total', total)
            print('basket', baskets[basket_idx[idx]])
            print('basket_idx', basket_idx)
            while basket_idx:
                if (idx <= len(basket_idx)-1) and (baskets[basket_idx[idx]] >= fruit):
                    basket_idx.pop(idx)
                    total -= 1
                    break
                elif idx > len(basket_idx)-1:
                    break
                idx += 1
        
        return total