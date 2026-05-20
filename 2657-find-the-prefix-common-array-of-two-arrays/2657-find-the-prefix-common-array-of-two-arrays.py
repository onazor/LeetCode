class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        answer = []
        count = 0
        frequency = {}
        for i in range(len(A)):
            if A[i] in frequency:
                frequency[A[i]] += 1
            else:
                frequency[A[i]] = 1
            
            if frequency[A[i]] == 2:
                count += 1

            if B[i] in frequency:
                frequency[B[i]] += 1
            else:
                frequency[B[i]] = 1
            
            if frequency[B[i]] == 2:
                count += 1
            
            answer.append(count)

        return answer
