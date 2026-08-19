class Solution:
    def findTwoElement(self, arr):
        # code here
        n = len(arr)
        arr1 = [0] * (n + 1)
        repet = 0
        miss = 0
        
        for num in arr:
            arr1[num] += 1
        
        for i in range(1, n + 1):
            if arr1[i] == 2:
                repet = i
            elif arr1[i] == 0:
                miss = i
        
        return (repet, miss)        
        
        # n = len(arr)
        # repet = -1
        # miss = -1
        
        # for num in range(1, n + 1):
        #     count = 0
        #     for i in range(n):
        #         if arr[i] == num:
        #             count += 1
        #     if count == 2:
        #         repet = num
        #     elif count == 0:
        #         miss = num
        #     if repet != -1 and miss != -1:
        #         break
        # return (repet, miss)            