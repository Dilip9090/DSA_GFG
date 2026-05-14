class Solution:
    def isSorted(self, arr) -> bool:
        # code here
        n = len(arr)
        
        for i in range (1,n):
            if arr[i] >= arr[i-1]:
                # return True 
                continue
            else:
                return False
        return True        