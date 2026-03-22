class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for rotation in range(4):
            new_grid = [[0] * len(mat) for _ in range(len(mat[0]))]
            for row in range(len(mat)):
                for col in range(len(mat[0])):
                    new_grid[col][len(mat)-row-1] = mat[row][col]
            mat = new_grid
            if new_grid == target:
                return True
        return False