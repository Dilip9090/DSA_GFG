class Solution:
    def booleanMatrix(self, mat):
        # code here     
        col0 = 0
        m = len(mat)
        n = len(mat[0])
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    mat[i][0] = 1
                    if j != 0:
                        mat[0][j] = 1
                    else:
                        col0 = 1
        
        for i in range(1,m):
            for j in range(1,n):
                if mat[i][0] == 1 or mat[0][j] == 1:
                    mat[i][j] = 1
        
        if matrix[0][0] == 1:
            for j in range(n):
                mat[0][j] = 1
        
        if col0 == 1:
            for i in range(m):
                mat[i][0] = 1
        return mat        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # def markrow(self,mat, row):
    #         for j in range(len(mat[0])):
    #             if mat[row][j] != 1:
    #                 mat[row][j] = -1
            
    
    # def markcol(self,mat, col):    
    #     for i in range(len(mat)):
    #         if mat[i][col] != 1:
    #             mat[i][col] = -1
                    
                
    
    
    # def booleanMatrix(self, mat):
    #     # code here 
        
    #     for i in range(len(mat)):
    #         for j in range(len(mat[0])):
    #             if mat[i][j] == 1:
    #                 self.markrow(mat, i)
    #                 self.markcol(mat, j)
            
    #     for k in range(len(mat)):
    #         for l in range(len(mat[0])):
    #             if mat[k][l] == -1:
    #                 mat[k][l] = 1
    
        