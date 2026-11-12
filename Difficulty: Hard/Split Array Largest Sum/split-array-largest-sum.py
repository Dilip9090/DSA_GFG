class Solution:
    def splitArray(self, arr, k):
        # code here
        n = len(arr)
        
        if n < k:
            return -1
        
        low = max(arr)
        high = sum(arr)
        
        while low <= high:
            mid = (low + high) // 2
            countpersons = self.counters(arr, mid)
            if countpersons <= k:
                high = mid - 1
            else:
                low = mid + 1
        return low        
        
        
        
    def counters(self, arr, count):
        person = 1
        numcount = 0
        
        for i in range(len(arr)):
            if arr[i] + numcount <= count:
                numcount += arr[i]
            else:
                person += 1
                numcount = arr[i]
        return person
        
        
        
        
        
        # n = len(arr)
        
        # if n < k:
        #     return -1
        
    #     low = max(arr)
    #     high = sum(arr)
    #     for i in range(low, high + 1):
    #         ans = self.counters(arr, i)
    #         if ans == k:
    #             return i
    
    
    # def counters(self, arr, count):
    #     person = 1
    #     getnum = 0
        
    #     for i in range(len(arr)):
    #         if arr[i] + getnum <= count:
    #             getnum += arr[i]
    #         else:
    #             person += 1
    #             getnum = arr[i]
    #     return person        