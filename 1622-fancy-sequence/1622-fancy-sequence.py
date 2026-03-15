class Fancy:
    
    def __init__(self):
        self.mod = 10**9+7
        self.seq = []
        self.add = 0
        self.mul = 1

    def append(self, val: int) -> None:
        x = ((val - self.add) * pow(self.mul, -1, self.mod)) % self.mod
        self.seq.append(x)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.mod

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % self.mod
        self.add = (self.add * m) % self.mod

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        
        x = self.seq[idx]
        result = (x * self.mul + self.add) % self.mod
        return result

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)