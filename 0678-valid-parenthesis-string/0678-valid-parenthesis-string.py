class Solution:
    def checkValidString(self, s: str) -> bool:
        if s[0] == ')':
            return False
        
        if s[-1] == '(':
            return False
        
        open_stack = []
        star_stack = []

        for idx in range(len(s)):
            if s[idx] == '(':
                open_stack.append(idx)
            elif s[idx] == '*':
                star_stack.append(idx)
            elif s[idx] == ')':
                if open_stack:
                    open_stack.pop() 
                elif star_stack:
                    star_stack.pop() 
                else:
                    return False
            
        while star_stack and open_stack:
            top_star = star_stack.pop()
            top_open = open_stack.pop()

            if top_open > top_star:
                return False
        
        if open_stack:
            return False
        
        return True

