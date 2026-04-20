class Solution:
    def mostFreqEle(self, arr):
        
        freq = {}
    
        # Count frequencies
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
    
        maxFreq = 0
        result = float('-inf')
    
     # Find answer
        for num, count in freq.items():
            if count > maxFreq:
                maxFreq = count
                result = num
            elif count == maxFreq:
                result = max(result, num)
    
        return result        
         # code here
        