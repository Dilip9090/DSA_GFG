class Solution:
    def getSecondLargest(self, arr):
        largest1 = float('-inf')
        largest2 = float('-inf')

        for num in arr:
            if num > largest1:
                largest2 = largest1
                largest1 = num

            elif largest1 > num > largest2:
                largest2 = num

        return -1 if largest2 == float('-inf') else largest2      
        
        
        
        # Code Here
        # n = len(arr)
        # arr.sort()
        
        # while arr[n-1] != arr[0]:
        #     for i in range (n-1,0,-1):
        #         if arr[i] > arr[i-1]:
        #             return arr[i-1]
        # while arr[n-1] == arr[0]:
        #     return -1