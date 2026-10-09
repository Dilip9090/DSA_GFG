class Solution:
    def kokoEat(self, arr, k):
        # Code here
        low = 1
        high = max(arr)
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            total = self.hours(arr, mid)
            if total <= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans        
        
        
    
    def hours(self, arr, hour):
        banana = 0
        for j in range(len(arr)):
            banana += (arr[j] + hour - 1) // hour
        return banana    
        
        
    #     for i in range(1, max(arr) + 1):
    #         reqtime = self.hours(arr, i)
    #         if reqtime <= k:
    #             return i
    
    
    # def hours(self, arr, hour):
    #     banana = 0
    #     for j in range(len(arr)):
    #         banana += (arr[j] + hour - 1) // hour
    #     return banana    