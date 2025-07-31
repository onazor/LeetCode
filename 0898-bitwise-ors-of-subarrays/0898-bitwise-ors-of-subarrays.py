class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        answer = set()
        current = {0}

        for num in arr:
            current = {num | cur_vals for cur_vals in current} | {num}
            answer |= current
        
        return len(answer)