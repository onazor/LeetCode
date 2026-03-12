class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.components = n
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == root_j:
            return False
        
        self.parent[root_i] = root_j
        self.components -= 1
        return True

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        check_dsu = DisjointSetUnion(n)
        for u, v, strength, must in edges:
            check_dsu.union(u,v)
        if check_dsu.components > 1:
            return -1
        
        # set up the binary search
        low = 0
        high = 2 * max(edges[i][2] for i in range(len(edges)))

        # define a function that checks whether we can build spanning tree given a strength
        def check_spanning_tree(num):
            dsu = DisjointSetUnion(n)
            upgrades_used = 0

            # Priority 1: Must Edges
            for u, v, strength, must in edges:
                if must == 1:
                    if strength < num:
                        return False
                    
                    # If connecting this mandatory edge creates a cycle, a valid spanning tree is impossible!
                    if not dsu.union(u, v):
                        return False
            
            # Priority 2: Free Edges
            for u, v, strength, must in edges:
                if must == 0 and strength >= num:
                    dsu.union(u, v)
            
            # Priority 3: Upgradable Edges
            for u, v, strength, must in edges:
                if must == 0 and (strength < num) and ((strength * 2) >= num):
                    if dsu.union(u, v):
                        upgrades_used += 1
            
            return dsu.components == 1 and upgrades_used <= k

        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if check_spanning_tree(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans