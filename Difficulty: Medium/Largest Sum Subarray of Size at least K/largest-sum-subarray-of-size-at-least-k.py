#User function Template for python3

class Solution():
    def maxSumWithK(self, a, n, k):
        # Step 1: max subarray sum ending at each index (Kadane)
        max_end = [0] * n
        max_end[0] = a[0]
        
        for i in range(1, n):
            max_end[i] = max(a[i], max_end[i-1] + a[i])
        
        # Step 2: sum of first k elements
        curr_sum = sum(a[:k])
        result = curr_sum
        
        # Step 3: slide window
        for i in range(k, n):
            curr_sum += a[i] - a[i-k]
            
            # Case 1: take only k elements
            result = max(result, curr_sum)
            
            # Case 2: extend with previous best
            result = max(result, curr_sum + max_end[i-k])
        
        return result