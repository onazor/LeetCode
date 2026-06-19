class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alts = [0]
        summ = 0
        for i in range(len(gain)):
            summ += gain[i]
            alts.append(summ)
        print(alts)
        return max(alts)
