class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # odd - odd = even
        # even - even = even
        # odd - even = odd
        # even - odd = odd

        minimum = min(nums1)
        if minimum % 2 == 1:
            return True
        else:
            for num in nums1:
                if num % 2 == 1:
                    return False
            return True