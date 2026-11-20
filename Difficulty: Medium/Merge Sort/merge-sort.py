class Solution:
    def mergeSort(self, arr, l, r):
        # code here 
         if l >= r:
             return 
         
         mid = (l + r) // 2
         
         self.mergeSort(arr,l,mid)
         self.mergeSort(arr,mid+1,r)
         self.merge(arr,l,mid,r)
    
    def merge(self,arr,l, mid, r) :
        temp = []
        
        
        low = l
        high = mid + 1
        
        while low <= mid and high <= r:
            if arr[low] <= arr[high]:
                temp.append(arr[low])
                low += 1
            else:
                temp.append(arr[high])
                high += 1
                
        while low <= mid:
            temp.append(arr[low])
            low += 1
        
        while high <= r:
            temp.append(arr[high])
            high += 1
        
        for k in range(len(temp)):
            arr[l+k] = temp[k]
         
         