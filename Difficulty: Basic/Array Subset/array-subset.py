#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        freq = {}
        
        # count elements in a
        for num in a:
            freq[num] = freq.get(num, 0) + 1
        
        # check elements in b
        for num in b:
            if num not in freq or freq[num] == 0:
                return False
            freq[num] -= 1
        
        return True

        
        #Brute Force
        # for i in b:
        #     found = False
            
        #     for j in a:
        #         if i == j:
        #             found = True
        #             break
            
        #     if not found:
        #         return False
        
        # return True
                 
    
    
    
    
