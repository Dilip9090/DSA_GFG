class Solution:
    def findPages(self, arr, k):
        # code here
        n = len(arr)
        if n < k:
            return -1
        
        low = max(arr)
        high = sum(arr)
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            countthepage = self.countpages(arr, mid)
            # if countthepage == k:
            #     return mid
            if countthepage > k:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1
        return ans
        
        
        
        
    def countpages(self, arr, pages):
        student = 1
        currpages = 0
        
        for i in range(len(arr)):
            if arr[i] + currpages <= pages:
                currpages += arr[i]
            else:
                student += 1
                currpages = arr[i]
        return student        
        
        
        
        
    #     n = len(arr)
        
    #     if n < k:
    #         return -1
    #     low = max(arr)
    #     high = sum(arr)
        
    #     for i in range(low, high + 1):
    #         countstudent = self.maxipages(arr, i)
    #         if countstudent == k:
    #             return i


    # def maxipages(self, arr, pages):
    #     student = 1
    #     pagesstudent = 0
        
        
    #     for i in range(len(arr)):
    #         if arr[i] + pagesstudent <= pages:
    #             pagesstudent += arr[i]
    #         else:
    #             student += 1
    #             pagesstudent = arr[i]
    #     return student        