class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        if k == 0:
            return grid
            
        remainder = (m * n) % k
        if k >= (m * n) and remainder == 0:
            return grid
        
        for _ in range(k):
            temp = grid[0][0]
            final = grid[m-1][n-1]
            for i in range(m):
                for j in range(n):
                    save = grid[i][j]
                    grid[i][j] = temp
                    temp = save
            grid[0][0] = final
        return grid



