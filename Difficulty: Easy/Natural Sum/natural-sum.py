#User function Template for python3
class Solution:
    def find(self, N):
        x = 1 + 8 * N
        
        # Manual square root (binary search)
        left, right = 0, x
        
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                root = mid
                break
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        else:
            return -1   # not perfect square
        
        s = (root - 1) // 2
        
        if s * (s + 1) // 2 == N:
            return s
        
        return -1	    
		# Code here