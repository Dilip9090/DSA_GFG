class Solution: 
    def selectionSort(self, arr):
        #code here
        n = len(arr)
        
        for i in range(n):
            mini = i
            
            for k in range(i+1,n):
                if arr[k] < arr[mini]:
                    mini = k
            arr[i], arr[mini] = arr[mini], arr[i]
        return arr        