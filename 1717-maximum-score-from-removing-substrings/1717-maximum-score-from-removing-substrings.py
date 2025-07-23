class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # ab - > x
        # ba - > y
        count = 0
        if x > y: # prioritize ab
            target_x = 'ab'
            target_y = 'ba'
            stack = []
            for char in s:
                stack.append(char)
                if len(stack) >= len(target_x) and ''.join(stack[-len(target_x):]) == target_x:
                    for _ in range(len(target_x)):
                        stack.pop()
                    count += x
            result = ''.join(stack)
            stack1 = []
            for char in result:
                stack1.append(char)
                if len(stack1) >= len(target_y) and ''.join(stack1[-len(target_y):]) == target_y:
                    for _ in range(len(target_y)):
                        stack1.pop()
                    count += y
        else: # prioritize ba
            target_x = 'ab'
            target_y = 'ba'
            stack = []
            for char in s:
                stack.append(char)
                if len(stack) >= len(target_y) and ''.join(stack[-len(target_y):]) == target_y:
                    for _ in range(len(target_y)):
                        stack.pop()
                    count += y
            result = ''.join(stack)
            stack1 = []
            for char in result:
                stack1.append(char)
                if len(stack1) >= len(target_x) and ''.join(stack1[-len(target_x):]) == target_x:
                    for _ in range(len(target_x)):
                        stack1.pop()
                    count += x
        return count
        
