class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = ["0"]
        def reverse_string(s):
            return s[::-1]
        
        def invert(s):
            return ''.join('1' if char=='0' else '0' for char in s)
        
        for index in range(1, n):
            invert_s = invert(s[index-1])
            s.append(str(s[index-1]+"1"+reverse_string(invert_s)))

        target_string = s[n-1]
        return target_string[k-1]
