class Solution:
    def find (self, arr, key):
        #code here
        first = self.lower(arr, key)
        second = self.upper(arr, key, first)

        return (first, second)


    def lower(self, arr, key):
        n = len(arr)
        low = 0
        high = n - 1
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == key:
                ans = mid
                high = mid - 1
            elif arr[mid] > key:
                high = mid - 1
            else:
                low = mid + 1
        return ans                 

    def upper(self, arr, key, low):
        n = len(arr)
        high = n - 1
        ans = low

        for i in range(low + 1,n):
            if arr[i] == key:
                ans = i
        return ans 