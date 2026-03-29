class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        list1 = []
        list2 = []
        for i in range(2):
            list1.append(s1[i])
            list1.append(s1[i+2])
            
            list2.append(s2[i])
            list2.append(s2[i+2])
            if set(list1) != set(list2):
                return False
            list1 = []
            list2 = []

        return True