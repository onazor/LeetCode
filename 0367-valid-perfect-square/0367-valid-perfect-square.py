class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        integer = 1
        while integer**2 <= num:
            if integer**2 == num:
                return True
            integer += 1
        return False