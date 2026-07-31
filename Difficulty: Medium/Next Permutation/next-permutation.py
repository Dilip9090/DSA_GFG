class Solution:
    def nextPermutation(self, arr):
        # code here
        n = len(arr)
        idx = -1
        
        for i in range(n-2,-1,-1):
            if arr[i] < arr[i+1]:
                idx = i
                break
        if idx == -1:
            arr.reverse()
            return arr
        for j in range(n-1,idx,-1):
            if arr[j] > arr[idx]:
                arr[j], arr[idx] = arr[idx], arr[j]
                break
        left = idx + 1
        right = n - 1
        
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr
                
            