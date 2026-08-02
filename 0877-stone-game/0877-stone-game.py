class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        def max_diff(left, right):
            if (left, right) in memo:
                return memo[(left, right)]

            if left == right:
                return piles[left]
            
            left_score = piles[left] - max_diff(left+1, right)
            right_score = piles[right] - max_diff(left, right-1)

            best_score = max(left_score, right_score)
            memo[(left, right)] = best_score

            return best_score
        
        score = max_diff(0, len(piles)-1)
        if score > 0:
            return True
        return False