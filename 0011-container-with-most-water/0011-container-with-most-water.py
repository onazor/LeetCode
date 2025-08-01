class Solution:
    def maxArea(self, height: List[int]) -> int:

        idx_left = 0
        idx_right = len(height) - 1
        ans = min(height[idx_right],height[idx_left])*(idx_right-idx_left)
        while idx_left != idx_right:
            if height[idx_left] < height[idx_right]:
                idx_left += 1
                area = min(height[idx_right],height[idx_left])*(idx_right-idx_left)
                ans = max(ans, area)
            else:
                idx_right -= 1
                area = min(height[idx_right],height[idx_left])*(idx_right-idx_left)
                ans = max(ans, area)
        return ans
