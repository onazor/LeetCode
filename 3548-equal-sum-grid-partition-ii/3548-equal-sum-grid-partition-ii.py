class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        total_sum = 0
        positions = {}

        for r in range(m):
            for c in range(n):
                total_sum += grid[r][c]
                if grid[r][c] in positions:
                    positions[grid[r][c]].append((r,c))
                else:
                    positions[grid[r][c]] = [(r,c)]

        top_sum = 0
        for r in range(m-1):
            top_sum += sum(grid[r])
            bottom_sum = total_sum - top_sum
            
            if top_sum == bottom_sum:
                return True
            
            if top_sum > bottom_sum:
                target = top_sum - bottom_sum
                if target in positions:
                    for pos in positions[target]:
                        if pos[0] <= r:
                            # 1D Row Check: Must be left/right endpoints
                            if r == 0 and pos[1] != 0 and pos[1] != n - 1: continue
                            # 1D Col Check: Must be top/bottom endpoints
                            if n == 1 and pos[0] != 0 and pos[0] != r: continue
                            return True # If it survived the checks, it's valid!

            if bottom_sum > top_sum:
                target = bottom_sum - top_sum
                if target in positions:
                    for pos in positions[target]:
                        if pos[0] > r:
                            # 1D Row Check: Must be left/right endpoints
                            if r == m - 2 and pos[1] != 0 and pos[1] != n - 1: continue
                            # 1D Col Check: Must be top/bottom endpoints
                            if n == 1 and pos[0] != r + 1 and pos[0] != m - 1: continue
                            return True
            
        left_sum = 0
        for c in range(n-1):
            left_sum += sum(row[c] for row in grid) # FIXED += TYPO
            right_sum = total_sum - left_sum
        
            if left_sum == right_sum:
                return True

            if left_sum > right_sum:
                target = left_sum - right_sum
                if target in positions:
                    for pos in positions[target]:
                        if pos[1] <= c:
                            # 1D Col Check: Must be top/bottom endpoints
                            if c == 0 and pos[0] != 0 and pos[0] != m - 1: continue
                            # 1D Row Check: Must be left/right endpoints
                            if m == 1 and pos[1] != 0 and pos[1] != c: continue
                            return True

            if right_sum > left_sum:
                target = right_sum - left_sum
                if target in positions:
                    for pos in positions[target]:
                        if pos[1] > c:
                            # 1D Col Check: Must be top/bottom endpoints
                            if c == n - 2 and pos[0] != 0 and pos[0] != m - 1: continue
                            # 1D Row Check: Must be left/right endpoints
                            if m == 1 and pos[1] != c + 1 and pos[1] != n - 1: continue
                            return True
        return False