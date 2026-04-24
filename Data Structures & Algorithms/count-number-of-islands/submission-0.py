class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def backtrack(i,j,board):
            if j < 0 or i < 0 or j > len(board[0])-1 or i > len(board)-1:
                return False
            if board[i][j] != "1":
                return False
            board[i][j] = "#"

            if (backtrack(i, j-1, board) or 
            backtrack(i, j+1, board) or 
            backtrack(i-1, j, board) or
            backtrack(i+1, j, board)):
                return True
            
            
            
        
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islands += 1
                    t = backtrack(i, j, grid)
                    print(grid)
                    
        return islands