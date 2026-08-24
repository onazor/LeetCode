class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        memoization = {}
        # precompute the sum prefix
        prefix_sum = [stones[0]]
        current_sum = stones[0]

        for i in range(1, len(stones)):
            current_sum += stones[i]
            prefix_sum.append(current_sum)
        

        def score_diff(number_of_stones):
            if number_of_stones == len(stones)-1:
                return prefix_sum[-1]

            if number_of_stones in memoization:
                return memoization[number_of_stones]
            
            score_pick = prefix_sum[number_of_stones] - score_diff(number_of_stones + 1)
            score_leave = score_diff(number_of_stones+1)
            final_score = max(score_pick, score_leave)

            memoization[number_of_stones] = final_score
            return final_score
        
        return score_diff(1)
            
