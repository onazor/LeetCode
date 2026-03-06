class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        index_start_zero = 0
        while s[index_start_zero] == '1':
            index_start_zero += 1
            if index_start_zero >= len(s):
                break
        
        if index_start_zero == len(s):
            return True
        
        for i in range(index_start_zero, len(s)):
            if s[i] == '1':
                return False
        
        return True