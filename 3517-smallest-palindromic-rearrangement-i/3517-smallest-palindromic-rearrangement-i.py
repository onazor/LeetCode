class Solution:
    def smallestPalindrome(self, s: str) -> str:
        length_s = s
        left_half = ''
        right_half = ''
        mid_odd = ''
        dictionary_s = {}
        
        for char in s:
            if char in dictionary_s:
                dictionary_s[char] += 1
            else:
                dictionary_s[char] = 1
        sorted_dic = dict(sorted(dictionary_s.items(), key=lambda item: item[0]))
        for key, value in sorted_dic.items():
            while value != 0:
                if value % 2 != 0 and value != 1:
                    left_half += key
                    right_half += key
                    value -= 2
                elif value % 2 != 0 and value == 1:
                    mid_odd += key
                    value -= 1
                else:
                    left_half += key
                    right_half += key
                    value -= 2

        return left_half + mid_odd + right_half[::-1]