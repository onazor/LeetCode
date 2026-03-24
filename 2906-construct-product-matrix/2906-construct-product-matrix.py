class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n = len(grid)
        m = len(grid[0])

        size = n * m
        list_array = [0] * size
        prefix_array = [1] * size
        suffix_array =  [1] * size
        product_array = [0] * size
        matrix_product_array = [[0] * m for _ in range(n)]

        idx = 0
        for r in range(n):
            for c in range(m):
                list_array[idx] = grid[r][c]
                idx += 1
        
        prefix_product = list_array[0]
        #prefix_array[0] = prefix_product
        for idx in range(1, len(list_array)):
            prefix_array[idx] = prefix_product % MOD
            prefix_product *= list_array[idx] % MOD

        suffix_product = list_array[-1]
        #suffix_array[-1] = suffix_product
        for idx in reversed(range(len(list_array)- 1)):
            suffix_array[idx] = suffix_product % MOD
            suffix_product *= list_array[idx] % MOD
        
        for idx in range(len(list_array)):
            product_array[idx] = (prefix_array[idx]*suffix_array[idx]) % MOD

        idx = 0
        for r in range(n):
            for c in range(m):
                matrix_product_array[r][c] = product_array[idx]
                idx += 1
                
        return matrix_product_array