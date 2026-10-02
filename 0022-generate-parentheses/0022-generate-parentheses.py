class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        answers = []

        def isValid(s: str) -> bool:
            parenthesis_stack = []
            if len(s) <= 1:
                return False

            for idx in range(len(s)):
                if s[idx] == "(":
                    parenthesis_stack.append(s[idx])
                elif s[idx] == ")":
                    if len(parenthesis_stack) == 0:
                        return False

                    if parenthesis_stack[-1] != '(':
                        return False
                    else:
                        parenthesis_stack.pop()
            
            if len(parenthesis_stack) > 0:
                return False
            return True

        def generate_valid_p(current_string, left, right):
            if len(current_string) == 2 * n and left == 0 and right == 0:
                if isValid(current_string):
                    answers.append(current_string) 
                return 
            

            if right > 0:
                current_string_r = current_string + ")"
                generate_valid_p(current_string_r, left, right-1)

            if left > 0:
                current_string_l = current_string + "("
                generate_valid_p(current_string_l, left-1, right)
        
        generate_valid_p('(', n-1, n)

        return answers