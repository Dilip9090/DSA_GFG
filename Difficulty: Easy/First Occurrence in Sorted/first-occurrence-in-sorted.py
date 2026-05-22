class Solution:
    def firstSearch(self, arr, k):
        # Code Here
        n = len(arr)
        for i in range(n):
            if arr[i] == k :
                return i
            
        return -1
        