class Solution: 
    def selectionSort(self, arr):
        lenth = len(arr)
        
        for i in range(lenth):
            min = i
            
            
            for k in range(i + 1, lenth):
                if arr[k] < arr[min]:
                    min = k
                    
            arr[i], arr[min] = arr[min], arr[i]
            
        return arr    
                    
        #code here