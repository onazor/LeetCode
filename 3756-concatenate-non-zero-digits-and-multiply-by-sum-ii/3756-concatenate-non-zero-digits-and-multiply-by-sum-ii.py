class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9+7

        string_prefix = []
        string_sum = []
        string_nonzero = []
        powers_of_10 = [1]

        current_val = 0
        total_sum = 0
        nonzero_count = 0
        mult = 1
        for char in s:
            if char != '0':
                current_val = (current_val * 10 + int(char)) % MOD
                nonzero_count += 1

            total_sum += int(char)
            mult = (mult * 10) % MOD
            powers_of_10.append(mult)
            string_prefix.append(current_val)
            string_nonzero.append(nonzero_count)
            string_sum.append(total_sum)
            
        ans = []
        for interval in queries:
            right = interval[1]
            if interval[0] == 0:
                stringstring = string_prefix[right] % MOD
                sumsum = string_sum[right] % MOD
            else:
                left = interval[0]
                stringstring = (string_prefix[right]-(powers_of_10[string_nonzero[right] - string_nonzero[left-1
                ]])*(string_prefix[left-1])) % MOD
                sumsum = (string_sum[right] - string_sum[left-1]) % MOD

            current_ans = (sumsum*stringstring) % MOD
            ans.append(current_ans)

        return ans