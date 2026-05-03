class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        list_shifts = [s]
        for idx in range(len(s)-1):
            temp = s[idx+1:]+s[:idx+1]
            list_shifts.append(temp)
        if goal in list_shifts:
            return True
        return False
