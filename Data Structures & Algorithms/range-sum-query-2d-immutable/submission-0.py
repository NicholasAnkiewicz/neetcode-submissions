class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.dic_matrix = {}
        for row_idx in range(len(matrix)):
            self.dic_matrix[row_idx] = matrix[row_idx]
        #print(self.dic_matrix)



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for i in range(row1, row2+1):
            row = self.dic_matrix.get(i)
            for j in range(col1, col2+1):
                res += row[j]
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)