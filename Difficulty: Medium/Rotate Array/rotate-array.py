class Solution:
    def rotateArr(self, arr, d):
        #code here
        n = len(arr)
        d = d % n
        temp = []
        j = 0
        
        for i in range(d):
            temp.append(arr[i])
        
        for k in range(d,n):
            arr[k-d] = arr[k]
        
        for m in range(n-d,n):
            arr[m] = temp[j]
            j += 1
        return arr    
            
            
        