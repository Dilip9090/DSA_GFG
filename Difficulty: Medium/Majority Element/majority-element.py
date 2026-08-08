class Solution:
    def majorityElement(self, arr):
        #code here
        
        arr.sort()
        n = len(arr)
        majo = arr[n // 2]
        count = 0
        
        for i in range(n):
            if arr[i] == majo:
                count += 1
            if count > n // 2:
                return majo
        return -1        
        
        # mpp = []
        # n = len(arr)
        # for i in range(n):
        #     count = 0
        #     for j in range(n):
        #         if arr[i] == arr[j]:
        #             count += 1
        #         if count > n/2:
        #             return arr[i]
        # return -1            