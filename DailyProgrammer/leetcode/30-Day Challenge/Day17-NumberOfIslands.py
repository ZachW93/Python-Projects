# -*- coding: utf-8 -*-
"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of 
islands. An island is surrounded by water and is formed by connecting adjacent 
lands horizontally or vertically. You may assume all four edges of the grid are 
all surrounded by water.
"""

class Solution:
    def numIslands(self, grid) -> int:
        def get_next(i,j):

            nextLand = set()
            
            if i > 0 and grid[i - 1][j] == "1": 
                nextLand.add((i - 1, j))
                
            if i + 1 < height and grid[i + 1][j] == "1": 
                nextLand.add((i + 1, j))
                
            if j > 0 and grid[i][j - 1] == "1": 
                nextLand.add((i, j - 1))
                
            if j + 1 < width and grid[i][j + 1] == "1": 
                nextLand.add((i, j + 1))
                
            return nextLand

        count = 0
        height = len(grid)
        width = len(grid[0])
        
        for i in range(height):
            
            for j in range(width):
                
                if grid[i][j] == "1":
                    
                    count += 1
                    grid[i][j] = 0
                    check = get_next(i,j)
                    
                    while len(check):
                        
                        next_check = set()
                        
                        for island in check:
                            
                            grid[island[0]][island[1]] = 0
                            
                            next_check |= get_next(island[0],island[1]) 
                            
                        check = next_check
        
        return count
                
    
       
Solution = Solution()