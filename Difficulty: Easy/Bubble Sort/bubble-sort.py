class Solution:
    def bubbleSort(self,arr):
        #Bubble Sort
        n = len(arr)
        
        for i in range (n):
            for k in range(0,n-i-1):
                if arr[k] > arr[k+1]:
                    arr[k] , arr[k+1] = arr[k+1], arr[k]
        return arr            
        # code here