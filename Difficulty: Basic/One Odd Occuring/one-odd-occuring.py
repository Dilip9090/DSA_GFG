class Solution:
    def getOddOccurrence(self, arr):
        # code here 
        
        sum1 = 0
        
        for i in range(len(arr)):
            sum1 ^= arr[i]
        return sum1    