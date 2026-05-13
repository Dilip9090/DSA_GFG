class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        n = len(arr)
        arr.sort()
        
        while arr[n-1] != arr[0]:
            for i in range (n-1,0,-1):
                if arr[i] > arr[i-1]:
                    return arr[i-1]
        while arr[n-1] == arr[0]:
            return -1