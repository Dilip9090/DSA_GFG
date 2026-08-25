class Solution:
    def findTwoElement(self, arr):
        # code here
        n = len(arr)
        
        xr = 0
        
        for i in range(0,n,1):
            xr = xr ^ arr[i]
            xr = xr ^ (i + 1)
        
        bitno = 0
        while (1):
            if (xr & (1 << bitno) != 0):
                break
            bitno += 1
        
        zero = 0
        one = 0
        
        for i in range(n):
            if (arr[i] & (1 << bitno) != 0):
                one = one ^ arr[i]
            else:
                zero = zero ^ arr[i]
        
        for i in range(1,n + 1):
            if (i & (1 << bitno) != 0):
                one = one ^ i
            else:
                zero = zero ^ i
        count = 0        
        for i in range(n):
            if arr[i] == zero:
                count += 1  
        
        if count == 2:
            return (zero, one)
    
        return (one, zero)
        
        
        
        
        # n = len(arr)
        # SN = (n * (n + 1)) // 2
        # S2N = (n * (n + 1)) * (2 * n + 1) // 6
        # s = 0
        # s2 = 0
        # for i in range(n):
        #     s += arr[i]
        #     s2 += arr[i] * arr[i]
        
        # val1 = s - SN
        # val2 = s2 - S2N
        # val2 = val2 // val1
        # x = (val1 + val2) //2
        # y = x - val1
        # return (x, y)
        
        
        
        
        
        
        # n = len(arr)
        # arr1 = [0] * (n + 1)
        # repet = -1
        # miss = -1
        
        # for num in arr:
        #     arr1[num] += 1
        
        # for i in range(1, n + 1):
        #     if arr1[i] == 2:
        #         repet = i
        #     elif arr1[i] == 0:
        #         miss = i
        #     if repet != -1 and miss != -1:
        #         break
        # return (repet, miss)        
        
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