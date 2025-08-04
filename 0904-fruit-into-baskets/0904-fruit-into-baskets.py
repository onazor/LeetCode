class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        def pop_first(ordered_dict):
            first = next(iter(ordered_dict))
            ordered_dict.pop(first)

        current_set = dict.fromkeys([])
        last_index = {}  # stores last seen index of each fruit
        left = 0
        max_count = 0

        for right in range(len(fruits)):
            fruit = fruits[right]
            current_set[fruit] = None
            last_index[fruit] = right

            if len(current_set) > 2:
                # Find fruit with the leftmost last seen index
                fruit_to_remove = min(current_set.keys(), key=lambda k: last_index[k])
                left = last_index[fruit_to_remove] + 1  # move left pointer
                current_set.pop(fruit_to_remove)
                last_index.pop(fruit_to_remove)

            max_count = max(max_count, right - left + 1)

        return max_count
