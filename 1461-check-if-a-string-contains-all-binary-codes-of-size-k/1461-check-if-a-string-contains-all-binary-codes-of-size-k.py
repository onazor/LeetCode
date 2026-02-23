class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        empty_set = set()
        position_k = k
        for index in range(len(s)-k+1):
            empty_set.add(s[index:index+k])
        
        if len(empty_set) == (1 << k):
            return True
        return False
        
