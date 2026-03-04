class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        sum_col = [0]*len(mat[0])
        sum_row = []

        col_n, row_n = len(mat[0]), len(mat)

        for col in mat:
            sum_col = list(map(lambda x, y: x+y, sum_col, col))
        
        for row in mat:
            row_sum = sum(row)
            sum_row.append(row_sum)

        count = 0
        for i in range(row_n):
            for j in range(col_n):
                if mat[i][j] == 1:
                    if sum_row[i] == 1 and sum_col[j] == 1:
                        count += 1

        return count