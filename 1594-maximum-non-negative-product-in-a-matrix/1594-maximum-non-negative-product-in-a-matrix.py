class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        m = len(grid)
        n = len(grid[0])

        if m == 1:
            prod = 1
            for c in range(n):
                prod = prod * grid[0][c]
            if prod < 0:
                return -1
            else:
                return prod % MOD
        
        if n == 1:
            prod = 1
            for r in range(m):
                prod = prod * grid[r][0]
            if prod < 0:
                return -1
            else:
                return prod % MOD


        max_dp = [[0] * n for _ in range(m)]
        min_dp = [[0] * n for _ in range(m)]

        max_dp[0][0] = grid[0][0]
        min_dp[0][0] = grid[0][0]

        for c in range(1, n):
            max_dp[0][c] = max_dp[0][c-1] * grid[0][c]
            min_dp[0][c] = max_dp[0][c]
        
        for r in range(1, m):
            max_dp[r][0] = max_dp[r-1][0] * grid[r][0]
            min_dp[r][0] = max_dp[r][0]

        for r in range(1, m):
            for c in range(1, n):
                val = grid[r][c]
                above_max = val * max_dp[r-1][c]
                above_min = val * min_dp[r-1][c]
                left_max = val * max_dp[r][c-1]
                left_min = val * min_dp[r][c-1]

                max_dp[r][c] = max(above_max, above_min, left_max, left_min)
                min_dp[r][c] = min(above_max, above_min, left_max, left_min)
        
        if max_dp[m-1][n-1] < 0:
            return -1
        return max_dp[m-1][n-1] % MOD 