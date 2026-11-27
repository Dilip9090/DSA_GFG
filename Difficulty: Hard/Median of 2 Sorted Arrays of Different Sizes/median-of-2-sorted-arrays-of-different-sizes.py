class Solution:
    def medianOf2(self, arr1, arr2):
        # code here
        n = len(arr1)
        m = len(arr2)
        
        low = 0
        high = 0
        
        el1 = ((n+m)//2)-1
        el2 = ((n+m)//2)
        
        counter = 0
        ans1 = 0
        ans2 = 0
        
        while low < n and high <m:
            if arr1[low] < arr2[high]:
                val = arr1[low]
                low += 1
            else:
                val = arr2[high]
                high += 1
            
            if counter == el1:
                ans1 = val
            if counter == el2:
                ans2 = val
            counter += 1
        while low < n:
            val = arr1[low]
            if counter == el1:
                ans1 = val
            if counter == el2:
                ans2 = val
            counter += 1
            low += 1
        while high < m:
            val = arr2[high]
            if counter == el1:
                ans1 = val
            if counter == el2:
                ans2 = val
            counter += 1
            high += 1
        if (n+m)%2 == 0:
            return (ans1 + ans2)/2
        else:
            return ans2
        
        
        
        
        
        # arr3 = []
        # n = len(arr1)
        # m = len(arr2)
        
        # low = 0 
        # high = 0
        
        # while low <= (n - 1) and high <= (m - 1):
        #     if arr1[low] < arr2[high]:
        #         arr3.append(arr1[low])
        #         low += 1
        #     else:
        #         arr3.append(arr2[high])
        #         high += 1
                
        # while low <= (n-1):
        #     arr3.append(arr1[low])
        #     low += 1
        # while high <= (m-1):
        #     arr3.append(arr2[high])
        #     high += 1
        
        # k = (n + m) 
        
        # if (k%2) == 1:
        #     return (arr3[(n+m)//2])
        # else:
        #     ans = arr3[((n+m)//2)-1] + arr3[(n+m)//2]
        #     return (ans//2)