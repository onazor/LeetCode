class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        frequency = {}
        for char in s:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        frequency_acs = dict(sorted(frequency.items()))

        ans = ''
        for idx in range(len(s)):
            if target[idx] in frequency_acs and frequency_acs[target[idx]] > 0:
                ans += target[idx]
                frequency_acs[target[idx]] -= 1
            else:
                flag = 0
                for letter in frequency_acs:
                    if letter > target[idx] and frequency_acs[letter] > 0:
                        ans += letter
                        frequency_acs[letter] -= 1
                        flag += 1
                        break

                if flag > 0:
                    for letter in frequency_acs:
                        ans += letter * frequency_acs[letter]
                    return ans

                if flag == 0:
                    while idx >= 0:
                        if len(ans) > 0: 
                            last_letter = ans[-1]
                            frequency_acs[last_letter] += 1
                            ans = ans[:-1]
                        idx -= 1

                        if idx < 0:
                            return ''

                        second_flag = 0
                        for letter in frequency_acs:
                            if letter > target[idx] and frequency_acs[letter] > 0:
                                second_flag += 1
                                ans += letter
                                frequency_acs[letter] -= 1
                                break

                        if second_flag > 0:
                            for letter in frequency_acs:
                                ans += letter * frequency_acs[letter]
                            return ans
                
                    if idx < 0:
                        return ''

        idx = len(s) - 1
        while idx >= 0:
            if len(ans) > 0:
                last_letter = ans[-1]
                frequency_acs[last_letter] += 1
                ans = ans[:-1]
            
            # Check if we can bump the CURRENT idx before stepping back
            for letter in frequency_acs:
                if letter > target[idx] and frequency_acs[letter] > 0:
                    ans += letter
                    frequency_acs[letter] -= 1
                    for char in frequency_acs:
                        ans += char * frequency_acs[char]
                    return ans
            
            # If we couldn't find a greater letter, step backward
            idx -= 1
                    
        return ''