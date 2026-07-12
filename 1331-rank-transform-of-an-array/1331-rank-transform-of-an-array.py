class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        copy_arr = arr.copy()
        copy_arr.sort()
        ranking = {}

        idx = 1
        for num in copy_arr:
            if num not in ranking:
                ranking[num] = idx
                idx += 1

        final_ranking = []
        for number in arr:
            final_ranking.append(ranking[number])

        return final_ranking