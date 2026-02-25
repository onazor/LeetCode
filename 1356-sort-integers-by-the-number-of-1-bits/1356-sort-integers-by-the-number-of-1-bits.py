class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        ones = dict()
        items = []
        for num in arr:
            items.append((num, num.bit_count()))
        sorted_tuples = sorted(items, key=lambda item: (item[1], item[0]))
        return [item[0] for item in sorted_tuples]