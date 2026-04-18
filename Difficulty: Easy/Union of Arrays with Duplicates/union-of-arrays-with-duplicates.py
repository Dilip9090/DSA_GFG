class Solution:
    def findUnion(self, a, b):
        s = set()
        
        for x in a:
            s.add(x)
        for x in b:
            s.add(x)
            
        return list(s)
        