class Solution:
    def booleanMatrix(self, mat):
        # code here 
        n = len(mat)
        m = len(mat[0])

        rows = [False] * n
        cols = [False] * m

        # Mark rows and columns containing 1
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    rows[i] = True
                    cols[j] = True

        # Update matrix
        for i in range(n):
            for j in range(m):
                if rows[i] or cols[j]:
                    mat[i][j] = 1

        return mat
        