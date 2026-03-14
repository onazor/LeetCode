class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # generate all the happy strings recursively
        happy_strings = []
        def build(current_string):
            if len(current_string) == n:
                happy_strings.append(current_string)
                return
            
            for char in ['a', 'b', 'c']:
                if len(current_string) > 0 and current_string[-1] == char:
                    continue
                build(current_string + char)
        
        build("")
        print(happy_strings)
        return happy_strings[k-1] if len(happy_strings) >= k else ""