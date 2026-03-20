class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        array_ans = [[0] * (len(grid[0]) - k + 1) for _ in range(len(grid) - k + 1)]
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows - k + 1):
            for col in range(cols - k + 1):
                distinct_val = set()
                for i in range(row, row+k):
                    for j in range(col, col+k):
                        distinct_val.add(grid[i][j])

                if len(distinct_val) == 1:
                    array_ans[row][col] = 0
                else:
                    minimum = float('inf')
                    sorted_set = sorted(list(distinct_val))
                    for idx in range(1, len(sorted_set)):
                        abs_diff = abs(sorted_set[idx] - sorted_set[idx-1])
                        minimum = min(minimum, abs_diff)
                    array_ans[row][col] = minimum

        return array_ans