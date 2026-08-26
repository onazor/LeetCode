class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        final_ans = ''
        count = 0

        for idx in range(len(s)):
            if s[idx] == '1':
                count += 1

            while count == k:
                current = s[left:idx+1]
                if not final_ans or len(current) < len(final_ans):
                    final_ans = current
                elif len(current) == len(final_ans):
                    final_ans = min(final_ans, current)

                if s[left] == '1':
                    count -= 1
                
                left += 1
        
        return final_ans
            

