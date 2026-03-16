class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        all_sums = []
        # rows = len(grid)
        # cols = len(grid[0])

        # get each cell
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                all_sums.append(grid[row][col])

        # traverse to each cell with growing border (size)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                border = 1

                # the while checks if we are outside the grid
                while (row+border) < len(grid) and (row-border) >= 0 and (col+border) < len(grid[0]) and (col-border) >= 0:
                    rhombus_sum = 0
                    for i in range(1, border):
                        rhombus_sum += grid[row+i][col-border+i]
                        rhombus_sum += grid[row-i][col-border+i]
                        rhombus_sum += grid[row+i][col+border-i]
                        rhombus_sum += grid[row-i][col+border-i]
                    # we also need to add the bottom and top cells    
                    all_sums.append(rhombus_sum + grid[row][col-border]+grid[row][col+border]+grid[row-border][col]+grid[row+border][col])
                    border += 1
    
        return sorted(list(set(all_sums)), reverse=True)[:3]