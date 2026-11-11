class Solution:
    def aggressiveCows(self, arr, k):
        # code here
        arr.sort()
        n = len(arr)
        low = 0
        high = arr[n - 1]
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            possi = self.possibal(arr, k, mid)
            if possi == True:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans        
        
        
    def possibal(self, arr, k, dis):
        cows = 1
        lastcow = arr[0]
        
        for i in range(1, len(arr)):
            if arr[i] - lastcow >= dis:
                cows += 1
                lastcow = arr[i]
            if cows >= k:
                return True
        return False        
        
    #     arr.sort()
    #     n = len(arr)
    #     low = 0
    #     high = arr[n - 1]
    #     ans = -1
        
    #     while low <= high :
    #         mid = (low + high) // 2
    #         possi = self.countcowss(arr, k, mid)
    #         if possi == True:
    #             ans = mid
    #             low = mid + 1
    #         else:
    #             high = mid - 1
    #     return ans        
    
    
    # def countcowss(self, arr, k, dist):
    #     countcow = 1
    #     lastcow = arr[0]
        
    #     for i in range(1, len(arr)):
    #         if arr[i] - lastcow >= dist:
    #             countcow += 1
    #             lastcow = arr[i]
        
    #         if countcow >= k:
    #             return True
    #     return False        
    
    
    
    
    #     arr.sort()
    #     maxi = max(arr)
    #     mini = min(arr)
        
    #     for i in range(1,(maxi - mini)):
    #         if self.canweplace(arr,k,i) == True:
    #             continue
    #         else:
    #             return (i - 1)
    #     return (maxi - mini)        
        
        
    # def canweplace(self, arr, k, dis):
    #     countcow = 1
    #     lastcow = arr[0]
        
    #     for i in range(1, len(arr)):
    #         if arr[i] - lastcow >= dis:
    #             countcow += 1
    #             lastcow = arr[i]
            
        
    #         if countcow >= k:
    #             return True
    
    #     return False