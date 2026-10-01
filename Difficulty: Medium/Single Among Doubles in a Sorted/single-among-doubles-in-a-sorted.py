class Solution:
    def single(self, arr):
        # code here
        n = len(arr)
        low = 0
        high = n - 1
        
        if n == 1:
            return arr[0]
        elif low == 0:
            if arr[low] != arr[low + 1]:
                return arr[low]
            low += 1    
        if high == n - 1:
            if arr[high] != arr[high - 1]:
                return arr[high]
            high -= 1    
        
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] != arr[mid - 1] and arr[mid] != arr[mid + 1]:
                return arr[mid]
            elif arr[mid] == arr[mid - 1] and 1 == mid%2:
                low = mid + 1
            else:
                high = mid - 1