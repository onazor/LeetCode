class Solution:
    def reverseParentheses(self, s: str) -> str:
        string_stack = []
        current_string = []

        for char in s:
            if char == '(':
                string_stack.append(current_string)
                current_string = []
            elif char == ')':
                current_string.reverse()
                previous_string = string_stack.pop()
                current_string = previous_string+current_string
            else:
                current_string.append(char)
            
        return "".join(current_string)

