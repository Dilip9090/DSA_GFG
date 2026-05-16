class Solution:
    def removeDuplicates(self, arr):
        a = 0
        b = 1
        arr1 = []
        n = len(arr)
        
        for i in range (n):
            if arr[i] != a:
                a = arr[i]
                arr1.append(a)
        return arr1        
        
        
        
        # code here 
        # arr = list(set(arr))
        # arr.sort()
        # return arr