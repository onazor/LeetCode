class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        total_rows = query_row + 2
        dp_array = [[0.0] * total_rows for i in range(total_rows)]
        dp_array[0][0] = poured

        for row in range(query_row):
            for col in range(row+1):
                amount_to_pour = dp_array[row][col]
                keep = min(1, amount_to_pour)
                overflow = max(0, amount_to_pour - 1)
                dp_array[row+1][col] += overflow / 2
                dp_array[row+1][col+1] += overflow / 2 
        return min(1, dp_array[query_row][query_glass])

        