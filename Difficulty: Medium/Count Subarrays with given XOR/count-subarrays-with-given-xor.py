class Solution:
    def subarrayXor(self, arr, m):
        # code here
        n = len(arr)
        mpp = {0: 1}
        xor = 0
        count = 0
        for i in range(n):
            xor ^= arr[i]
            need = xor ^ m
            
            if need in mpp:
                count += mpp[need]
            if xor in mpp:    
                mpp[xor] += 1
            else:
                mpp[xor] = 1
        return count        
        
        
        
        
        
        # n = len(arr)
        # sum1 = 0
        # for i in range(n):
        #     xor = 0
        #     for j in range(i,n):
        #         xor = xor ^ arr[j]
        #         if xor == m:
        #             sum1 += 1
        # return sum1                 