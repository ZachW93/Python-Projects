# -*- coding: utf-8 -*-
"""
Given a m x n grid filled with non-negative numbers, find a path from top left 
to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""
def minPathSum(self, grid) -> int:
    
        width = len(grid)
        height = len(grid[0])
        matrix = [[0] * height for _ in range(width)]
        
        for i in range(width):
            
            for j in range(height):
                
                t = min(matrix[i - 1][j] if i - 1 >= 0 else float('inf'),
                        matrix[i][j - 1] if j - 1 >= 0 else float('inf'))
                
                if t == float('inf'):
                    
                    matrix[i][j] = grid[i][j]
                    
                else:
                    
                    matrix[i][j] = grid[i][j] + t
                    
        return matrix[-1][-1]