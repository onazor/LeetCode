class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memoization = {}
        def count_valid(start_idx, t_idx):
            if (start_idx, t_idx) in memoization:
                return memoization[(start_idx, t_idx)]
            if t_idx == len(t):
                return 1
            if start_idx == len(s):
                return 0

            total_ways = count_valid(start_idx + 1, t_idx)

            if s[start_idx] == t[t_idx]:
                total_ways += count_valid(start_idx+1, t_idx+1)
            
            memoization[(start_idx, t_idx)] = total_ways
            return total_ways
    
        return count_valid(0,0)
