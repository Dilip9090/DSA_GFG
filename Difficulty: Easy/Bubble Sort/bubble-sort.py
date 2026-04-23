class Solution:
    def bubbleSort(self,arr):
        # code here
        n = len(arr)
        swap = 0
        
        for i in range(n):
            for k in range (0,n-i-1):
                if arr[k] > arr[k+1]:
                    arr[k] , arr[k+1] = arr[k+1], arr[k]
                    swap += 1
            if swap == 0:
                break
        return arr            