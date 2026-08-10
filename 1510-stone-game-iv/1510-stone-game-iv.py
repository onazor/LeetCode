# note that we just need to find all the non-zero square number less than or equal to n
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        memoization = {}

        # let us precompute all the squares less than or equal to n
        square_num = 1
        square_list = []
        while square_num ** 2 <= 10**5:
            square_list.append(square_num ** 2)
            square_num += 1
        
        
        def canwin(n):
            if n in memoization:
                return memoization[n]

            if n == 0:
                return False
            
            for square in square_list:
                if square > n:
                    break

                if not canwin(n-square):
                    memoization[n] = True
                    return True

            memoization[n] = False
            return False

        return canwin(n)