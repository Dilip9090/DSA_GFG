class Solution:
    def find (self, arr, key):
        #code here
        first = self.lower(arr, key)
        if first == -1:
            return (0)
        second = self.upper(arr, key, first)

        return ((second - first) + 1)


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
        high = len(arr) - 1
        ans = low

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == key:
                ans = mid
                low = mid + 1
            elif arr[mid] > key:
                high = mid - 1
            else:
                low = mid + 1

        return ans  
# class Solution:
    def countFreq(self, arr, key):
        # code here
        return (self.find(arr, key))
        
        
        
        
        
        
        
        
        
        
        
        
        
        # n = len(arr)
        # count = 0
        # for i in range(n):
        #     if arr[i] == target:
        #         count += 1
        # return count        