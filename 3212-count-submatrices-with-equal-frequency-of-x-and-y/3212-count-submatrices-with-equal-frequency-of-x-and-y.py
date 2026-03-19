class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        matrix_0 = [[0] * len(grid[0]) for _ in range(len(grid))]
        matrix_1 = [[0] * len(grid[0]) for _ in range(len(grid))]
        matrix_count_0 = [[0] * len(grid[0]) for _ in range(len(grid))]
        matrix_count_1 = [[0] * len(grid[0]) for _ in range(len(grid))]
        num_matrices = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 'X':
                    matrix_0[row][col] = 1
                    matrix_count_0[row][col] = 1
                elif grid[row][col] == 'Y':
                    matrix_0[row][col] = -1
                else:
                    matrix_0[row][col] = 0

        for row_idx in range(len(grid)):
            matrix_1[row_idx][0] = matrix_0[row_idx][0]
            matrix_count_1[row_idx][0] = matrix_count_0[row_idx][0]
        for col_idx in range(len(grid[0])):
            matrix_1[0][col_idx] = matrix_0[0][col_idx]
            matrix_count_1[0][col_idx] = matrix_count_0[0][col_idx]
        
        for row in range(1, len(grid)):
            matrix_1[row] = [a+b for a, b in zip(matrix_0[row], matrix_1[row-1])]
            matrix_count_1[row] = [a+b for a, b in zip(matrix_count_0[row], matrix_count_1[row-1])]

        for row in range(len(grid)):
            row_sum = 0
            row_sum_count = 0
            for col in range(len(grid[0])):
                row_sum += matrix_1[row][col]
                row_sum_count += matrix_count_1[row][col]
                if row_sum == 0 and row_sum_count >=1:
                    num_matrices += 1
        return num_matrices