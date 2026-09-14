class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        ax1, ay1, ax2, ay2 = rec1
        bx1, by1, bx2, by2 = rec2
        if ax2 <= bx1:
            return False
        elif ax1 >= bx2:
            return False
        elif ay2 <= by1:
            return False
        elif ay1 >= by2:
            return False
        
        
        return True