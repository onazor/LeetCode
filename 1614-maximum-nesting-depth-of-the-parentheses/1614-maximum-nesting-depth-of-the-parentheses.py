class Solution:
    def maxDepth(self, s: str) -> int:
        
        final_max = 0
        current_count = 0

        for char in s:
            if char == '(':
                current_count += 1
            elif char == ')':
                final_max = max(final_max, current_count)
                current_count -= 1
            else:
                continue
        
        return final_max