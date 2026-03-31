class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)

        word = ["*"]*(n+m-1)
        for i in range(n):
            if str1[i] == "T":
                for j in range(i, i+m):
                    if word[j] != '*' and word[j] != str2[j-i]:
                        return ""
                    word[j] = str2[j-i]

        f_asterisks = [0]*n
        f_conflicts = [0]*n

        for i in range(n):
            if str1[i] == 'F':
                for j in range(i, i+m):
                    if word[j] == '*':
                        f_asterisks[i] += 1
                    elif word[j] != str2[j-i]:
                        f_conflicts[i] += 1

                if f_asterisks[i] == 0 and f_conflicts[i] == 0:
                    return ""

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for k in range(n + m - 1):
            if word[k] == '*':
                forbidden = set()
        
                start_i = max(0, k - m + 1)
                end_i = min(n - 1, k)

                for i in range(start_i, end_i + 1):
                    if str1[i] == 'F':
                        if f_asterisks[i] == 1 and f_conflicts[i] == 0:
                            forbidden.add(str2[k - i])

                chosen_char = ''
                for char in alphabet:
                    if char not in forbidden:
                        chosen_char = char
                        break
                
                if not chosen_char: 
                    return ""

                word[k] = chosen_char

                for i in range(start_i, end_i + 1):
                    if str1[i] == 'F':
                        f_asterisks[i] -= 1
                        if chosen_char != str2[k - i]:
                            f_conflicts[i] += 1
                            
        return "".join(word)