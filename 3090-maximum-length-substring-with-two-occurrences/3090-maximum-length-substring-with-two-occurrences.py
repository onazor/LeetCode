class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
        left = 0
        max_length = 0
        default_dict = {}
        for char in s:
            default_dict[char] = 0
        

        for i in range(len(s)):
            default_dict[s[i]] += 1

            while default_dict[s[i]] > 2:
                default_dict[s[left]] -= 1
                left += 1
            
            current_length = i - left + 1
            max_length = max(max_length, current_length)

        return max_length