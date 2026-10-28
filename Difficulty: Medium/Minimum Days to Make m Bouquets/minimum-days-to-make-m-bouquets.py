class Solution:
    def minDaysBloom(self, arr, k, m):
        # Code here
        n = len(arr)
        
        if (m * k) > n:
            return -1
        
        low = min(arr)
        high = max(arr)
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            if self.possibal(arr, mid, k, m) >= m :
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return low     
    
    
    def possibal(self, arr, mid, k, m):
        ans = 0
        count = 0
        
        for i in range(len(arr)):
            if arr[i] <= mid:
                count += 1
                if count == k:
                    ans += 1
                    count = 0
            else:
                count = 0
        return ans        