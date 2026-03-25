class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        row_array = []
        col_array = []
        row_array_sum = []
        col_array_sum = []

        m = len(grid)
        n = len(grid[0])

        for row in range(m):
            for col in range(n):
                row_array.append(grid[row][col])
        
        for col in range(n):
            for row in range(m):
                col_array.append(grid[row][col])
        
        for i in range(n, len(col_array)+1, n):
            print(i)
            row_sum = 0
            for j in range(i-n, i):
                row_sum += row_array[j]
            row_array_sum.append(row_sum)
        print(row_array_sum)
        for i in range(m, len(col_array)+1, m):
            col_sum = 0
            for j in range(i-m, i):
                col_sum += col_array[j]
            col_array_sum.append(col_sum)

        prefix_col_sum = [0] * len(col_array_sum)
        suffix_col_sum = [0] * len(col_array_sum)
        prefix_row_sum = [0] * len(row_array_sum)
        suffix_row_sum = [0] * len(row_array_sum)

        # prefix row
        prefix_row_sum[0] = row_array_sum[0]
        current_sum = prefix_row_sum[0]
        for i in range(1, len(row_array_sum)):
            current_sum += row_array_sum[i]
            prefix_row_sum[i] = current_sum
        
        # suffix row
        suffix_row_sum[-1] = row_array_sum[-1]
        current_sum = suffix_row_sum[-1]
        for i in reversed(range(len(row_array_sum)-1)):
            current_sum += row_array_sum[i]
            suffix_row_sum[i] = current_sum

        # prefix col
        prefix_col_sum[0] = col_array_sum[0]
        current_sum = prefix_col_sum[0]
        for i in range(1, len(col_array_sum)):
            current_sum += col_array_sum[i]
            prefix_col_sum[i] = current_sum
        
        # suffix col
        suffix_col_sum[-1] = col_array_sum[-1]
        current_sum = suffix_col_sum[-1]
        for i in reversed(range(len(col_array_sum)-1)):
            current_sum += col_array_sum[i]
            suffix_col_sum[i] = current_sum
        
        print(row_array_sum)
        print(prefix_row_sum)
        print(suffix_row_sum)

        print(col_array_sum)
        print(prefix_col_sum)
        print(suffix_col_sum)

        # check row
        for i in range(len(row_array_sum)-1):
            if prefix_row_sum[i] == suffix_row_sum[i+1]:
                return True
        
        for i in range(len(col_array_sum)-1):
            if prefix_col_sum[i] == suffix_col_sum[i+1]:
                return True

        return False