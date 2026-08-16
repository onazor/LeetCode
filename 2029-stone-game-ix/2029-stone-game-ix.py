class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        # memoization = {}

        # stones_mod3_freq = {0:0, 1:0, 2:0}
        # for stone in stones:
        #     stones_mod3_freq[stone % 3] += 1

        # # define a function that takes the current state and turn of the players
        # # turn is an important state here since the game is asymmetrical
        # # reference point here is alice: 0, bob: 1
        # def can_win(turn, current_sum, zero_freq, one_freq, two_freq):
        #     if current_sum % 3 == 0 and (zero_freq + one_freq + two_freq != len(stones)):
        #         return True

        #     state = (turn, current_sum % 3, zero_freq, one_freq, two_freq)
        #     if state in memoization:
        #         return memoization[state]

        #     if zero_freq == 0 and one_freq == 0 and two_freq == 0:
        #         return turn == 1

        #     if zero_freq > 0:
        #         if not can_win(1 - turn, current_sum, zero_freq - 1, one_freq, two_freq):
        #             memoization[state] = True
        #             return True
            
        #     if one_freq > 0:
        #         if not can_win(1-turn, current_sum+1, zero_freq, one_freq-1, two_freq):
        #             memoization[state] = True
        #             return True
            
        #     if two_freq > 0:
        #         if not can_win(1-turn, current_sum+2, zero_freq, one_freq, two_freq-1):
        #             memoization[state] = True
        #             return True

        #     memoization[state] = False
        #     return False

        # return can_win(0, 0, stones_mod3_freq[0], stones_mod3_freq[1], stones_mod3_freq[2])

        counts = [0, 0, 0]
        for num in stones:
            counts[num % 3] += 1

        if counts[0] % 2 == 0:
            return counts[1] > 0 and counts[2] > 0
        else:
            return abs(counts[1] - counts[2]) > 2
