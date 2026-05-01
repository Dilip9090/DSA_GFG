class Solution:
    def quickSort(self, arr, low, high):
        #code here 
        if low < high:
            
            pi = self.partition(arr,low,high)
            self.quickSort(arr,low,pi-1)
            self.quickSort(arr,pi+1,high)

    def partition(self, arr, low, high):
        #code here
        povit = arr[low]
        i = low +1
        j = high
        
        while True:
            while i <= j and arr[i] <= povit:
                i += 1
            while i <= j and arr[j] > povit:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break
        arr[low], arr[j] = arr[j], arr[low]
        return j