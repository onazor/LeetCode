class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        max_right = []
        for row in grid:
            counter = 0
            index = len(grid) - 1
            print(row[index])
            while index >= 0 and row[index] == 0:
                counter += 1
                index -= 1
            max_right.append(counter)
        new_sort_max_right = sorted(max_right)
        print(new_sort_max_right)
        print(max_right)
        # check
        for index in range(len(new_sort_max_right)):
            if new_sort_max_right[index] > index:
                return -1
        
        # get the minimum number of swaps
        min_swap = 0
        for row in range(len(grid)):
            trailing_zeros = len(grid) - 1 - row
            iterate_index = 0
            while trailing_zeros > max_right[iterate_index]:
                iterate_index += 1
            min_swap += iterate_index
        return min_swap

