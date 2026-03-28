class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp[0])
        word = [''] * n
        
        current_char = 'a'
        for i in range(n):
            if word[i] != '':
                continue
            if current_char > 'z':
                return ""

            word[i] = current_char
            for j in range(i, n):
                if lcp[i][j]>0:
                    word[j] = current_char
            current_char = chr(ord(current_char)+1)
        
        for i in reversed(range(n)):
            for j in reversed(range(n)):
                if word[i] != word[j]:
                    if lcp[i][j] != 0:
                        return ""
                else:
                    if i == n-1 or j == n-1:
                        if lcp[i][j] == 1:
                            continue
                        return ""
                    else:
                        if lcp[i][j] == 1 + lcp[i+1][j+1]:
                            continue
                        return ""
        return ''.join(word)
