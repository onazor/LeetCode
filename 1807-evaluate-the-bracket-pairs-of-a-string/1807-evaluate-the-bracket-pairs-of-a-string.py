class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        
        to_dict = {}

        for pair in knowledge:
            to_dict[pair[0]] = pair[1]
        
        final_string = []
        current_string = []
        for char in s:
            if char == '(':
                final_string.append(current_string)
                current_string = []
            elif char == ')':
                check = "".join(current_string)
                if check in to_dict:
                    to_replace = to_dict[check]
                    previous = final_string.pop()
                    current_string = previous + list(to_replace)
                else:
                    previous = final_string.pop()
                    current_string = previous + ['?']
            else:
                current_string.append(char)

        return "".join(current_string)
