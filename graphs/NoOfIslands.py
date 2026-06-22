from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        q = deque()
        visited = set()
        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i,j) not in visited:
                    island_count += 1
                    visited.add((i,j))
                    q.append((i,j))
                    while q:
                        row , col = q.popleft()
                        if row+1 < len(grid) and grid[row+1][col] == "1" and (row+1,col) not in visited:
                            q.append((row+1,col))
                            visited.add((row + 1 , col))
                        if row-1 >= 0 and grid[row-1][col] == '1' and (row-1,col) not in visited:
                            q.append((row-1,col))
                            visited.add((row - 1 , col))
                        if col + 1 < len(grid[0]) and grid[row][col + 1] == '1' and (row,col+1) not in visited:
                            q.append((row,col + 1))
                            visited.add((row  , col +1))
                        if col - 1  >= 0 and grid[row][col - 1] == '1' and (row,col-1) not in visited:
                            q.append((row,col -1))
                            visited.add((row  , col - 1))
        return island_count
        