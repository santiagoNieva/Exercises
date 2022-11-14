"""
You are given an m x n grid where each cell can have one of three values:

    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 10
    grid[i][j] is 0, 1, or 2.


---!SECTION TIMING
    Start Time = 14/11/22 00:37
    End Time = 14/11/22 02:49

"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        
        rotten_indexes = []
        not_rotten_indexes = []
        
        # I need indexes so I'm using range()
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 2:
                    rotten_indexes.append([i,j])
                if grid[i][j] == 1:
                    not_rotten_indexes.append([i,j])
        
        if not rotten_indexes:
            if not_rotten_indexes:
                return -1
            else:
                return 0
            
        minutes = 0
        new_indexes = []
        while True:
            for i,j in rotten_indexes:
                if i > 0 and grid[i-1][j] == 1:
                    new_indexes.append([i-1,j])
                    grid[i-1][j] = 2
                if i < rows-1 and grid[i+1][j] == 1:
                    new_indexes.append([i+1,j])
                    grid[i+1][j] = 2
                if j > 0 and grid[i][j-1] == 1:
                    new_indexes.append([i,j-1])
                    grid[i][j-1] = 2
                if j < columns-1 and grid[i][j+1] == 1:
                    new_indexes.append([i,j+1])
                    grid[i][j+1] = 2
            if not new_indexes:
                for i in range(rows):
                    for j in range(columns):
                        if grid[i][j] == 1:
                            return -1
                return minutes
            
            rotten_indexes = new_indexes
            new_indexes = []
            minutes +=1
        else:
            # Imposible situation
            return -1