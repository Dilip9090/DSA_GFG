class Solution:
    def leaders(self, arr):
        # code here
        maxi = float('-inf')
        n = len(arr)
        arr1 = []
        
        for i in range(n-1,-1,-1):
            if arr[i] >= maxi:
                maxi = arr[i]
                arr1.append(maxi)
        arr1.reverse()        
        return arr1        
        
        
        ##Brute Force Solution
        # n = len(arr)
        # arr1 = []
        # for i in range(n):
        #     leader = True
        #     for j in range(i + 1,n):
        #         if arr[j] > arr[i]:
        #             leader = False
        #             break
        #     if leader == True:
        #         arr1.append(arr[i])
        # return arr1