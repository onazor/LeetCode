class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) == 3:
            if s[0] == s[1] and s[1] == s[2]:
                return s[0:2]
        elif len(s) <= 2:
            return s
        
        result = '' 
        #print(len(s)-1)
        for idx in range(len(s)-2):
            #print("char1: %c, char2: %c, char3: %c" % (s[idx], s[idx+1], s[idx+2]))
            if (s[idx] != s[idx+1]) or (s[idx+1] != s[idx+2]):
                result += s[idx]
        
        result += s[len(s)-2:len(s)]
        
        return result