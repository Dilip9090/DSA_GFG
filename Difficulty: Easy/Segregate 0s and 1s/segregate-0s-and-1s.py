class Solution:
    def segregate0and1(self, arr):
        zero = []
        one = []
        
        for i in arr:
            if i == 0:
                zero.append(i)
            else:
                one.append(i)
        
        result = zero + one
        
        for i in range(len(arr)):
            arr[i] = result[i]
        
        # code here