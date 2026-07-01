class Solution:
    def getSecondLargest(self, arr):
        # code here
        arr.sort()
        n = len(arr)

        flarge = arr[n - 1]

        for i in range(n - 2, -1, -1):
            if arr[i] != flarge:
                return arr[i]

        return -1       