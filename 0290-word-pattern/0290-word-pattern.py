class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        strings = list(s.split())
        letters = list(''.join(pattern))
        
        tuples_list = []
        if len(strings) != len(letters):
            return False

        for i in range(len(strings)):
            tuples_list.append((strings[i], letters[i]))
        
        tuples_set = set(tuples_list)
        return len(set(tuples_list)) == len(set(strings)) == len(set(letters))