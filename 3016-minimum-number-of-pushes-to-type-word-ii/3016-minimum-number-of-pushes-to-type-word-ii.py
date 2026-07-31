class Solution:
    def minimumPushes(self, word: str) -> int:
        if len(word) <= 8:
            return len(word)
        
        frequency = {}
        for char in word:
            if char not in frequency:
                frequency[char] = 1
            else:
                frequency[char] += 1

        sorted_freq = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))
        baseline = 8
        flag = 1
        minimum = 0
        for idx, key in enumerate(sorted_freq):
            if idx > baseline-1:
                flag += 1
                baseline = 8*flag
            minimum = minimum + flag * sorted_freq[key]

        return minimum