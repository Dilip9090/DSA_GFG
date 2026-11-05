class Solution:
    def leastWeightCapacity(self, arr, d):
        # code here
        n = len(arr)
        maxi = max(arr)
        sum1 = sum(arr)
        
        low = maxi
        high = sum1
        ans = sum1
        
        while low <= high:
            mid = (low + high) // 2
            solution = self.days(arr, mid)
            if solution > d:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1
        return ans  
    
    
    
    
    
    def days(self, arr, capa):
        din = 1
        weight = 0
        
        for i in range(len(arr)):
            if arr[i] + weight > capa:
                din += 1
                weight = arr[i]
            else:
                weight += arr[i]
        return din        
    
    
    
    
    
    
    
    
    
    
    #     maxi = max(arr)
    #     sum1 = sum(arr)
        
    #     for i in range(maxi, sum1+1):
    #         ans = self.days(arr, i)
    #         if ans <= d:
    #             return i 
    
    # def days(self, arr, capa):
    #     din = 1
    #     weight = 0
        
    #     for i in range(len(arr)):
            
    #         if weight + arr[i] > capa:
    #             din += 1
    #             weight = arr[i]
            
    #         else:
    #             weight += arr[i]
    #     return din        