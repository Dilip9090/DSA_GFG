class Solution:
    def checkElements(self, start, end, arr):
        # code here
        s = set(arr)
        
        for nums in range(start,end+1):
            if nums not in s:
                return False
        else:
            return True
        
        
        
        
        
        
        
        
        # arr.sort()
        # n = len(arr)
        
        # for i in range (start,end-1):
        #     if start and end in arr:
                
        #         if arr[i] == arr[i+1]-1:
        #             return True
        # else:
        #     return False
        
