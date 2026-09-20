class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        def check_palindrome(idx, num_char):
            palindrome = s[idx:idx+num_char]
            if palindrome == palindrome[::-1]:
                return True
            return False
        
        count = 0
        idx = 0
        while idx < len(s):
            if idx+k-1 < len(s) and check_palindrome(idx, k):
                count += 1
                idx = idx+k
            elif idx+k<len(s) and check_palindrome(idx, k+1):
                count += 1
                idx = idx+k+1
            else:
                idx +=1

        return count
