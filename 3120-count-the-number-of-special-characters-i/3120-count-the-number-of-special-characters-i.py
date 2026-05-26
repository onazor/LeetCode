class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        total = 0
        for i in range(62, 91):
            if chr(i) in word:
                if chr(i+32) in word:
                    total += 1
        return total