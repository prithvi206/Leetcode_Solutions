# 1572. Matrix Diagonal Sum
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        sum=0
        for i in range(n):
            for j in range(n):
                if i==j:
                    sum = sum + mat[i][j]
                elif j==n-i-1:
                    sum = sum + mat[i][j]
                    
        return sum