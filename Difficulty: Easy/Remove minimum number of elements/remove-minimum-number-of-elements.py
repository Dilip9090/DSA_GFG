from collections import Counter
class Solution:
    def minRemove(self, arr1, arr2):
        count1 = Counter(arr1)
        count2 = Counter(arr2)
        
        result = 0
        
        for x in count1:
            if x in count2:
                result += min(count1[x], count2[x])
                
        return result
        
        
        
