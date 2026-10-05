class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for char in s:
            if char == '(':
                stack.append(0)
            elif char == ')':
                inner_score = stack.pop()
                score_to_add = max(1, 2 * inner_score)
                stack[-1] += score_to_add
                
        return stack[0]