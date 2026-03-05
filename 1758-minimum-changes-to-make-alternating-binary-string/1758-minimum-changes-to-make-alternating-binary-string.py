class Solution:
    def minOperations(self, s: str) -> int:
        length = len(s)
        start_0 = ''
        start_1 = ''
        for index in range(length):
            if index % 2 == 0:
                start_0 += '0'
                start_1 += '1'
            else:
                start_0 += '1'
                start_1 += '0'
        
        start_zero_count = 0
        start_one_count = 0

        for idx in range(length):
            # check for start 0:
            if s[idx] != start_0[idx]:
                start_zero_count += 1
            # check for start 1:
            if s[idx] != start_1[idx]:
                start_one_count += 1

        print(f"start 1: {start_1}")
        print(f"start 0: {start_0}")
        return min(start_zero_count, start_one_count)