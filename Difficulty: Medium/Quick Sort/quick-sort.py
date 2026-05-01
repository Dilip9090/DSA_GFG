class Solution:
    def quickSort(self, arr, low, high):
        #code here 
        if low < high:
            pi = self.partition(arr,low,high)
            self.quickSort(arr,low,pi-1)
            self.quickSort(arr,pi+1,high)

    def partition(self, arr, low, high):
        #code here
        pivot = arr[low]
        i = low + 1
        j = high
        while True:
            while i <= j and arr[i] <= pivot:
                i += 1
            while i <= j and arr[j] > pivot:
                j -= 1
            if i <= j :
                arr[i] , arr[j] = arr[j], arr[i]
            else:
                break
        arr[low], arr[j] = arr[j], arr[low]    
                
        return j  