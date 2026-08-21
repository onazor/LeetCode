from math import lcm
from itertools import combinations

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        # binary search
        left = 1
        right = min(coins) * k
        best_answer = right

        def count_nums(coins, mid):
            total_num = 0
            n = len(coins)

            for parity in range(1, n+1): # this is to check if odd -> +,  even -> - and combinations
                for combination in combinations(coins, parity):
                    combo_lcm = combination[0]
                    for num in combination[1:]:
                        combo_lcm = lcm(combo_lcm, num)
                    current_count = mid // combo_lcm
                
                    if parity % 2 == 0:
                        total_num -= current_count
                    else:
                        total_num += current_count
            return total_num

        while left <= right:
            mid = (left + right) // 2

            current_count = count_nums(coins, mid)
            if current_count < k:
                left = mid + 1
            else:
                best_answer = mid
                right = mid - 1
        
        return best_answer


