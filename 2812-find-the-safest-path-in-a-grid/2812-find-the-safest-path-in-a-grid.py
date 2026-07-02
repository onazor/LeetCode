from collections import deque

class Solution:
    def is_path_possible(self, mid:int, score_grid:List[List[int]], n: int) -> bool:
        if score_grid[0][0] < mid or score_grid[n-1][n-1] < mid:
            return False
        
        queue = deque()
        queue.append((0,0))
        visited = set()

        while queue:
            row, col = queue.popleft()
            if row == n-1 and col == n-1:
                return True
            
            if (row-1 < n and row-1 >= 0) and ((row-1, col) not in visited) and (score_grid[row-1][col] >= mid):
                visited.add((row-1, col))
                queue.append((row-1, col))
            
            if (row+1 < n and row+1 >= 0) and ((row+1, col) not in visited) and (score_grid[row+1][col] >= mid):
                visited.add((row+1, col))
                queue.append((row+1, col))
            
            if (col-1 < n and col-1 >= 0) and ((row, col-1) not in visited) and (score_grid[row][col-1] >= mid):
                visited.add((row, col-1))
                queue.append((row, col-1))
            
            if (col+1 < n and col+1 >= 0) and ((row, col+1) not in visited) and (score_grid[row][col+1] >= mid):
                visited.add((row, col+1))
                queue.append((row, col+1))
        
        return False

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        queue = deque()
        n = len(grid)
        score_grid = [[-1]*len(grid[0]) for _ in range(len(grid[0]))]

        # looping through the grid
        for row in range(len(grid)):
            for col in range(len(grid)):
                if grid[row][col] == 1:
                    score_grid[row][col] = 0
                    queue.append((row, col))
        
        while queue:
            coordinates = queue.popleft()
            row, col = coordinates[0], coordinates[1]
            # up neighbor
            if (row-1 < n and row-1 >= 0) and (score_grid[row-1][col] == -1):
                score_grid[row-1][col] = score_grid[row][col] + 1
                queue.append((row-1, col))
            # down neighbor
            if (row+1 < n and row+1 >= 0) and (score_grid[row+1][col] == -1):
                score_grid[row+1][col] = score_grid[row][col] + 1
                queue.append((row+1, col))

            # left neighbor
            if (col-1 < n and col-1 >= 0) and (score_grid[row][col-1] == -1):
                score_grid[row][col-1] = score_grid[row][col] + 1
                queue.append((row, col-1))

            # right neighbor
            if (col+1 < n and col+1 >= 0) and (score_grid[row][col+1] == -1):
                score_grid[row][col+1] = score_grid[row][col] + 1
                queue.append((row, col+1))

        # do binary search
        left = 0
        right = min(score_grid[0][0], score_grid[n-1][n-1])
        ans = 0
        while left <= right:
            mid = (left+right) // 2
            if self.is_path_possible(mid, score_grid, n):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
            
        return ans
