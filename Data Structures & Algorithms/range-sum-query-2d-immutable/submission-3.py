class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sum_matrix = []
        for row in range(len(matrix)):
            self.sum_matrix.append([])
            for col in range(len(matrix[0])):
                if row == 0 and col == 0:
                    self.sum_matrix[row].append(matrix[row][col])  
                elif row == 0:
                    self.sum_matrix[row].append(matrix[row][col] + self.sum_matrix[row][col-1])
                elif col == 0:
                    self.sum_matrix[row].append(matrix[row][col] + self.sum_matrix[row-1][col])
                else:
                    self.sum_matrix[row].append(matrix[row][col] + self.sum_matrix[row-1][col] + self.sum_matrix[row][col-1] - self.sum_matrix[row-1][col-1])
            print(self.sum_matrix[row])



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        if row1 == 0 and col1 == 0:
            return self.sum_matrix[row2][col2]
        elif col1==0:
            return self.sum_matrix[row2][col2] - self.sum_matrix[row1-1][col2]
        elif row1==0:
            return self.sum_matrix[row2][col2] - self.sum_matrix[row2][col1-1]
        else:
            return self.sum_matrix[row2][col2] - self.sum_matrix[row2][col1-1] - self.sum_matrix[row1-1][col2] + self.sum_matrix[row1-1][col1-1]
        return 


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)