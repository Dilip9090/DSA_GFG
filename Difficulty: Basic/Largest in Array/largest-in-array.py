class Solution:
    def largest(self, arr):
        # code here
        n = len(arr)
        maxi = 0
        for i in range (n):
            if arr[i] > maxi:
                maxi = arr[i]
        return maxi    