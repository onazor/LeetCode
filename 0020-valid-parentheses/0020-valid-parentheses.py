class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis_stack = []
        if len(s) <= 1:
            return False

        for idx in range(len(s)):
            if s[idx] == "(":
                parenthesis_stack.append(s[idx])
            elif s[idx] == "[":
                parenthesis_stack.append(s[idx])
            elif s[idx] == "{":
                parenthesis_stack.append(s[idx])
            elif s[idx] == ")":
                if len(parenthesis_stack) == 0:
                    return False

                if parenthesis_stack[-1] != '(':
                    return False
                else:
                    parenthesis_stack.pop()
            elif s[idx] == "]":
                if len(parenthesis_stack) == 0:
                    return False

                if parenthesis_stack[-1] != '[':
                    return False
                else:
                    parenthesis_stack.pop()
            elif s[idx] == "}":
                if len(parenthesis_stack) == 0:
                    return False

                if parenthesis_stack[-1] != '{':
                    return False
                else:
                    parenthesis_stack.pop()
        
        if len(parenthesis_stack) > 0:
            return False
        return True