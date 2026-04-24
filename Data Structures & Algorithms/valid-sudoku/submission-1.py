class Solution:
    
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        def check_box(start_row, start_col):
            box = {}
            for i in range(start_row, start_row+3):
                for j in range(start_col, start_col+3):
                    if board[i][j] != ".":
                        if box.get(board[i][j],-1) == -1:
                            box[board[i][j]] = 1
                        else:
                            return False
            #print(box)
        
        
        
        for row in board:
            row_d = {}
            for num in row:
                if num != ".":
                    if row_d.get(num,-1) == -1:
                        row_d[num] = 1
                    else:
                        return False
        
        for i in range(len(board)):
            column_d = {}
            for j in range(len(board)):
                if board[j][i] != ".":
                    if column_d.get(board[j][i],-1) == -1:
                        column_d[board[j][i]] = 1
                    else:
                        return False
                #print(board[j][i])
                #print(column_d)
        for i in range(0, 9, 3):
            for j in range(0,9,3):
                res = check_box(i, j)
                if res == False:
                    return False
        return True
