#User function Template for python3
class Solution:
    # Function to check if two arrays are disjoint
    def areDisjoint(self, a, b):
        s = set(a)
        
        for num in  b:
            if num in s:
                return False
        
        return True        
        #code here