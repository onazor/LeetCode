class Solution:
    def canWinNim(self, n: int) -> bool:
        if n <= 3:
            return True
        elif (n) % 4 == 0:
            return False
        else:
            return True
        