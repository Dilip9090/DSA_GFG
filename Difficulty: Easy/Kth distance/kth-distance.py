#User function Template for python3
class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        s = set()
        
        for i in range(len(arr)):
            # agar element already set me hai → duplicate within k
            if arr[i] in s:
                return True
            
            s.add(arr[i])
            
            # window size maintain karo (max k)
            if len(s) > k:
                s.remove(arr[i - k])
        
        return False
                
        # your code