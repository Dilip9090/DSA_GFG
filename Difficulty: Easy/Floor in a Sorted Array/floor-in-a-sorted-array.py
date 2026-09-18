class Solution:
    def findFloor(self, arr, x):
        # code here
        n = len(arr)
        
        for i in range(n-1,-1,-1):
            if arr[i] <= x:
                return i
        return -1        