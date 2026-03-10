class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9+7
        from functools import cache
        @cache
        def build_array(zero_left, one_left, last_placed):
            if zero_left == 0 and one_left == 0:
                return 1
            
            total = 0
            if last_placed == 1:
                max_zeros_to_place = min(zero_left, limit)
                for i in range(1, max_zeros_to_place+1):
                    total += build_array(zero_left-i, one_left, 0)
            elif last_placed == 0:
                max_ones_to_place = min(one_left, limit)
                for j in range(1, max_ones_to_place+1):
                    total += build_array(zero_left, one_left-j, 1)
            return total
        
        return ((build_array(zero, one, 1) + build_array(zero, one, 0))) % MOD

            
            
