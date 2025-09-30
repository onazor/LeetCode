class Solution:
    def sumZero(self, n: int) -> List[int]:
        lst = []
        if n % 2 == 0:
            for i in range(1, (n // 2) + 1):
                lst.append(i)
                lst.append(-i)
        else:
            for i in range(1, (n // 2) + 1):
                lst.append(i)
                lst.append(-i)
            lst.append(0)

        return lst