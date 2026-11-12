class Solution:
    def minTime (self, arr, k):
        # code here
        n = len(arr)
        
        if n < k:
            return -1
        
        low = max(arr)
        high = sum(arr)
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            countpainters = self.timetoget(arr, mid)
            if countpainters > k:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1
        return low        
    
    
    
    def timetoget(self, arr, time):
        painter = 1
        painttiem = 0
        
        for i in range(len(arr)):
            if arr[i] + painttiem <= time:
                painttiem += arr[i]
            else:
                painter += 1
                painttiem = arr[i]
        return painter        
    
    
    #     n = len(arr)
    #     if k > n:
    #         return -1
        
    #     low = max(arr)
    #     high = sum(arr)
        
    #     for i in range(low, high + 1):
    #         countt = self.timetoget(arr, i)
    #         if countt == k:
    #             return i
    
    
    # def timetoget(self, arr, time):
    #     painter = 1
    #     paint = 0
        
    #     for i in range(len(arr)):
    #         if arr[i] + paint <= time:
    #             paint += arr[i]
    #         else:
    #             painter += 1
    #             paint = arr[i]
    #     return painter        