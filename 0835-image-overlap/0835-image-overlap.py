class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        list1 = []
        list2 = []

        n = len(img1)
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    list1.append((i,j))

                if img2[i][j] == 1:
                    list2.append((i,j))

        dict_counter = {}
        for coord1 in list1:
            for coord2 in list2:
                dx = coord1[0] - coord2[0]
                dy = coord1[1] - coord2[1]
                shift = (dx, dy)
                if shift in dict_counter:
                    dict_counter[shift] += 1
                else:
                    dict_counter[shift] = 1

        if not dict_counter:
            return 0

        counters = list(dict_counter.values())
        max_ans = float('-inf')

        for counter in counters:
            max_ans = max(max_ans, counter)

        return max_ans
