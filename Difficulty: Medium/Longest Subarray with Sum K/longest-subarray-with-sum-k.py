class Solution:
    def longestSubarray(self, arr, k):  
        prefix = {}
        s = 0
        maxi = 0

        for i in range(len(arr)):
            s += arr[i]

            if s == k:
                maxi = i + 1

            rem = s - k

            if rem in prefix:
                maxi = max(maxi, i - prefix[rem])

            if s not in prefix:
                prefix[s] = i

        return maxi
        
        
        
        
        
        
        
        
        
        
        
        # code here
        # left  = 0
        # right = 0
        # n = len(arr)
        # maxi = 0
        # sum1 = 0
        
        # while right < n:
        #     while right >= left and sum1 > k:
        #         sum1 -= arr[left]
        #         left += 1    
        #     if k < min(arr):
        #         return 0
        #     if sum1 == k:
        #         maxi = max(maxi, right - left + 1)
        #     right += 1
        #     if right < n :
        #         sum1 += arr[right]
        # return maxi
    
