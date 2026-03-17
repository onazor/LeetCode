class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        col_sum = matrix[0]
        #print(col_sum)
        area = 0

        if len(matrix) == 1:
            col_sum = sorted(col_sum, reverse=True)
            return max([col_sum[idx] * (idx+1) for idx in range(len(col_sum))])

        for row in range(1, len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 1:
                    col_sum[col] += matrix[row][col]
                else:
                    col_sum[col] = 0
            
                new_sorted = sorted(col_sum, reverse=True)
                #print(new_sorted)
            areas = max([new_sorted[idx] * (idx+1) for idx in range(len(new_sorted))])
            area = max(area, areas)
        

        return area
