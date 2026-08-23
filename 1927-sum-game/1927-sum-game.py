class Solution:
    def sumGame(self, num: str) -> bool:
        
        count_of_q = 0
        for char in num:
            if char == '?':
                count_of_q += 1
        
        first_half = 0
        second_half = 0
        first_half_countq = 0
        second_half_countq = 0

        for char in num[:len(num) // 2]:
            if char != '?':
                first_half += int(char)
            else:
                first_half_countq += 1
        for char in num[len(num) // 2:]:
            if char != '?':
                second_half += int(char)
            else:
                second_half_countq += 1
            
        if count_of_q % 2 == 1:
            return True
        else:
            if first_half - second_half == 9*(second_half_countq-first_half_countq) // 2:
                return False
            else:
                return True
