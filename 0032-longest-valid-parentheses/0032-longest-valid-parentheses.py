class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_length = float('-inf')

        for idx in range(len(s)):
            if s[idx] == '(':
                stack.append(idx)
            elif s[idx] == ')':
                stack.pop()

                if not stack:
                    stack.append(idx)
                else:
                    length = idx - stack[-1]
                    max_length = max(max_length, length)
                    
        if max_length == float('-inf'):
            return 0

        return max_length