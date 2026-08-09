# initially, Alice can take one or two stones given M = 1, 1 <= X <= 2M
# but we need to iterate for all the possible use cases where she takes 1 <= X <= 2M

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memoization = {}
        #precalculate indices
        total_sum = sum(piles)
        suffix_sum = [0] * len(piles)
        for i in range(len(piles)):
            suffix_sum[i] = total_sum
            total_sum = total_sum - piles[i]

        def score(i, m):
            score_obtained = float('-inf')
            if (i, m) in memoization:
                return memoization[(i,m)]

            if i >= len(piles):
                return 0

            if i + 2 * m >= len(piles):
                return suffix_sum[i]

            for X in range(1, 2*m+1):
                current_score = suffix_sum[i] - score(i+X, max(m, X)) 
                score_obtained = max(score_obtained, current_score)
            
            memoization[(i,m)] = score_obtained
            return score_obtained
        
        return score(0,1)
