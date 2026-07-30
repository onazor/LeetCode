class Solution:
    def minimumPushes(self, word: str) -> int:
        length = len(word)
        if length <= 8:
            return len(word)
        
        ans = 0
        multiplier = 1
        while length >= 0:
            left = length - 8
            if left >= 0:
                ans += 8*multiplier
                multiplier += 1
            else:
                ans += length * multiplier
                multiplier += 1
            length = left
        return ans
