class Solution:
    def minFlips(self, s: str) -> int:
        string_length = len(s)
        start_with_zero = ''
        start_with_one = ''

        for i in range(2*len(s)):
            if i % 2 == 0:
                start_with_zero += '0'
            else:
                start_with_zero += '1'
            
            if (i + 1) % 2 == 0:
                start_with_one += '0'
            else:
                start_with_one += '1'
        master_string = 2*s

        mismatch_zero = 0
        mismatch_one = 0

        for j in range(len(s)):
            if s[j] != start_with_zero[j]:
                mismatch_zero += 1
            if s[j] != start_with_one[j]:
                mismatch_one += 1

        minimum = min(mismatch_zero, mismatch_one)
        for k in range(len(s)):
            # slide to the right
            character_moving_out = s[k]

            # check for a mismatch
            if character_moving_out != start_with_zero[k]:
                mismatch_zero -= 1
            if character_moving_out != start_with_one[k]:
                mismatch_one -= 1

            character_moving_in = master_string[k+len(s)]
            if character_moving_in != start_with_zero[k+len(s)]:
                mismatch_zero += 1
            if character_moving_in != start_with_one[k+len(s)]:
                mismatch_one += 1
            minimum = min(minimum, mismatch_zero, mismatch_one)
        return minimum
    