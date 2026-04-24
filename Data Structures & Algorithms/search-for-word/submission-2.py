class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i,j,word,bboard):
            
            if word == [] or len(word) == 0 or word == None:
                return True
            if j < 0 or i < 0 or j > len(board[0])-1 or i > len(board)-1:
                return False
            if bboard[i][j] != word[0]:
                return False
            t = bboard[i][j]
            bboard[i][j] = "#"

            if (backtrack(i, j-1, word[1:], bboard) or 
            backtrack(i, j+1, word[1:], bboard) or 
            backtrack(i-1, j, word[1:], bboard) or
            backtrack(i+1, j, word[1:], bboard)):
                bboard[i][j] = t
                return True
            else:
                bboard[i][j] = t
                return False
            
            
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    t = backtrack(i, j, word,board)
                    if t == True:
                        return True
        return False