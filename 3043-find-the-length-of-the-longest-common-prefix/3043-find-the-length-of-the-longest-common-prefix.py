class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix_arr1 = list(set(arr1))
        prefix_arr2 = list(set(arr2))

        prefixes1 = []
        for n in prefix_arr1:
            s = str(n)
            for i in range(1, len(s) + 1):
                prefixes1.append(s[:i])
        
        prefixes2 = []
        for n in prefix_arr2:
            s = str(n)
            for i in range(1, len(s) + 1):
                prefixes2.append(s[:i])
        
        final_1 = set(prefixes1)
        final_2 = set(prefixes2)

        answer = 0
        for prefix in final_2:
            if prefix in final_1:
                answer = max(answer, len(prefix))

        return answer
