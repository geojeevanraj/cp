#lc problem link: https://leetcode.com/problems/island-perimeter/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        row = len(grid)
        col = len(grid[0])

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    cell_side = 4
                    if r > 0 and grid[r-1][c] == 1:
                        cell_side -= 1
                    if r < row - 1 and grid[r+1][c] == 1:
                        cell_side -= 1
                    if c > 0 and grid[r][c-1] == 1:
                        cell_side -= 1
                    if c < col - 1 and grid[r][c+1] == 1:
                        cell_side -= 1
                    perimeter += cell_side
        return perimeter
