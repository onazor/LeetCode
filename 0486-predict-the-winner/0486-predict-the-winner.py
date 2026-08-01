class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        memo = {}

        def max_diff(left, right):
            if (left, right) in memo:
                return memo[(left, right)]

            if left == right:
                return nums[left]
            left_score = nums[left] - max_diff(left+1, right)
            right_score = nums[right] - max_diff(left, right-1)

            best_score = max(left_score, right_score)
            memo[(left, right)] = best_score
            return best_score
        
        score = max_diff(0, len(nums)-1)
        if score < 0:
            return False

        return True