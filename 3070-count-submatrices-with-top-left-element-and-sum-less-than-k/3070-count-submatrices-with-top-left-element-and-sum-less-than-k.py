class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        num_matrices = 0

        matrix = [[0] * len(grid[0]) for _ in range(len(grid))]
        for row_idx in range(len(grid)):
            matrix[row_idx][0] = grid[row_idx][0]
        for col_idx in range(len(grid[0])):
            matrix[0][col_idx] = grid[0][col_idx]

        for row in range(1, len(grid)):
            matrix[row] = [a+b for a, b in zip(grid[row], matrix[row-1])]

        for row in range(len(grid)):
            row_sum = 0
            for col in range(len(grid[0])):
                row_sum += matrix[row][col]
                if row_sum <= k:
                    num_matrices += 1

        return num_matrices
                


