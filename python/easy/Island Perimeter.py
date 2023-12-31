from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimetr = 0
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    perimetr += 4
                    if i > 0 and grid[i-1][j]:
                        perimetr -= 2
                    if j > 0 and grid[i][j-1]:
                        perimetr -= 2


        return perimetr
