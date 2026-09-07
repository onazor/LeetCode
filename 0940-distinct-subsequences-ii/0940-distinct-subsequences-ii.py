class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9+7

        buckets = [0] * 26
        for char in s:
            idx = ord(char) - ord('a')
            buckets[idx] = (sum(buckets)+1) % MOD
        return sum(buckets) % MOD


            
            

