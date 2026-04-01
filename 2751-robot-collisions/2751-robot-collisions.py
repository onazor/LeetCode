class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        combined_list = []
        for i in range(len(positions)):
            combined_list.append((positions[i], healths[i], directions[i], i))
        
        combined_list.sort()
        stack = []
        
        for robot in combined_list:
            pos, health, direction, original_idx = robot
            
            if direction == 'R':
                stack.append([pos, health, direction, original_idx])
            else: 
                while stack and stack[-1][2] == 'R' and health > 0:
                    if stack[-1][1] > health:
                        stack[-1][1] -= 1  
                        health = 0         
                    elif stack[-1][1] < health:
                        stack.pop()        
                        health -= 1        
                    else:
                        stack.pop()        
                        health = 0         

                if health > 0:
                    stack.append([pos, health, direction, original_idx])
                    
        stack.sort(key=lambda x: x[3]) 
        
        result = []
        for survivor in stack:
            result.append(survivor[1]) 
            
        return result