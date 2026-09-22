class Solution:
    def findCeil(self, arr, x):
        # code here
        n = len(arr)
        ans = -1
        
        for i in range(n):
            if arr[i] >= x:
                return i
        return ans        