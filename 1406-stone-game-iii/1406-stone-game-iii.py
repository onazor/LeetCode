class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        memo = {}
        
        def max_diff(first_idx):
            max_score = float('-inf')
            if first_idx in memo:
                return memo[first_idx]

            if first_idx == len(stoneValue):
                return 0
            
            if first_idx < len(stoneValue):
                first_pick_score = stoneValue[first_idx] - max_diff(first_idx+1)
                max_score = max(max_score, first_pick_score)

            if first_idx + 1 < len(stoneValue):
                second_pick_score = stoneValue[first_idx] + stoneValue[first_idx+1] - max_diff(first_idx+2)
                max_score = max(max_score, second_pick_score)

            if first_idx + 2 < len(stoneValue):
                third_pick_score = stoneValue[first_idx] + stoneValue[first_idx+1] + stoneValue[first_idx+2] - max_diff(first_idx+3)
                max_score = max(max_score, third_pick_score)

            memo[first_idx] = max_score

            return max_score
        
        score = max_diff(0)
        print(score)

        if score > 0:
            return "Alice"
        elif score < 0:
            return "Bob"
        else:
            return "Tie"