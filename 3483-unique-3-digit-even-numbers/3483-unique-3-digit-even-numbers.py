class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        
        used = [False] * len(digits)
        global_set = set()

        def backtrack(current_number):
            if len(current_number) == 3:
                if current_number[0] == 0:
                    return
                
                if current_number[-1] % 2 != 0:
                    return
                
                result = int("".join(map(str, current_number)))
                global_set.add(result)
            
            if len(current_number) < 3:
                for idx in range(len(digits)):
                    if used[idx] == False:
                        used[idx] = True
                        current_number.append(digits[idx])
                        backtrack(current_number)

                        current_number.pop()
                        used[idx] = False
        
        backtrack([])
        return len(global_set)




            
