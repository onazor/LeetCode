from collections import deque

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        queue = deque()
        start_health = health - grid[0][0]
        visited_health = [[-1]*n for _ in range(m)]
        visited_health[0][0] = start_health

        if start_health <= 0:
            return False
        queue.append((0, 0, start_health))

        while queue:
            row, col, health = queue.popleft()
            if row == m-1 and col == n-1:
                if visited_health[row][col] > 0:
                    return True

            if (row+1<m and row+1>=0):
                new_health = health - grid[row+1][col]
                if new_health > 0 and new_health > visited_health[row+1][col]:
                    visited_health[row+1][col] = new_health
                    queue.append((row+1, col, new_health))

            if (row-1<m and row-1>=0):
                new_health = health - grid[row-1][col]
                if new_health > 0 and new_health > visited_health[row-1][col]:
                    visited_health[row-1][col] = new_health
                    queue.append((row-1, col, new_health))
            
            if (col-1<n and col-1>=0):
                new_health = health - grid[row][col-1]
                if new_health > 0 and new_health > visited_health[row][col-1]:
                    visited_health[row][col-1] = new_health
                    queue.append((row, col-1, new_health))
            
            if (col+1<n and col+1>=0):
                new_health = health - grid[row][col+1]
                if new_health > 0 and new_health > visited_health[row][col+1]:
                    visited_health[row][col+1] = new_health
                    queue.append((row, col+1, new_health))

        return False

