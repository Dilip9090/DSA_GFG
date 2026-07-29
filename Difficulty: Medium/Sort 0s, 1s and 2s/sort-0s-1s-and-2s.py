class Solution:
    def sort012(self, arr):
        ##1st
        # arr.sort()
        
        ##2nd
        # count0 = arr.count(0)
        # count1 = arr.count(1)
        # count2 = arr.count(2)
        
        # for i in range(count0):
        #     arr[i] = 0
        # for i in range(count0, count0 + count1):
        #     arr[i] = 1
        # for i in range(count0 + count1, len(arr)):
        #     arr[i] = 2
        
        ##3rd
        low = 0
        mid = 0
        high = len(arr) - 1
        
        while mid <= high:
            
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1