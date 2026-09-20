class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        index = 1
    
        for char in s:
            total += index*(ord('z')-ord(char)+1)
            index += 1
        return total