class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = []
        current = 1
        for index in range(1, len(s)):
            if s[index] == s[index-1]:
                current += 1
            else:
                count.append(current)
                current = 1
        count.append(current)
        
        ans = 0
        for index in range(len(count)-1):
            ans += min(count[index], count[index+1])

        return ans
