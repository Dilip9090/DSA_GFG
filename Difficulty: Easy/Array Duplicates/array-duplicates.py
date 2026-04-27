class Solution:
    def findDuplicates(self, arr):
        res = []
        
        for i in range(len(arr)):
            index = abs(arr[i]) - 1
            
            if arr[index] < 0:
                res.append(abs(arr[i]))
            else:
                arr[index] = -arr[index]
        
        return res
        
        # code here
        