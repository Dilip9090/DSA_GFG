class Solution:
    def smallestDivisor(self, arr, k):
        # Code here
        n = len(arr)
        low = 1
        high = max(arr)
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            total = 0
            for i in range(n):
                sum1 = (arr[i] + mid - 1) // mid
                total += sum1
            if total <= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans         
        
        # ans = -1
        # for i in range(1,max(arr)+1):
        #     total = 0
        #     for j in range(len(arr)):
        #         sum1 = (arr[j] + i - 1) // i
        #         total += sum1
        #     if total <= k:
        #         ans = i
        #         break
        # return ans        