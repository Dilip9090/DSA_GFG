class Solution:
    def upperBound(self, arr, target):
        # code here
        n = len(arr)
        
        for i in range(n):
            if arr[i] > target:
                return i
        return n        