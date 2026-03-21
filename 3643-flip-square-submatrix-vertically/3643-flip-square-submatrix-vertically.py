class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        idx = 0
        rows = len(grid)
        
        for row in range(x, x+(k // 2)):
            for col in range(y, y+k):
                temp_store = grid[row][col]
                grid[row][col] = grid[x+k-1-(row-x)][col]
                grid[x+k-1-(row-x)][col] = temp_store
            print(x+k-1-(row-x))
            print(grid)
            idx += 1
        return grid