class Solution:
    def intersect(self, a, b):
        
        #Best Approach
        
        set_a = set(a)
        set_b = set(b)
        
        result = list(set_a & set_b)
        return result
        
        
        
        
        
        
        
        
        # #Time limit exceeded.
        # final = []
        
        # for i in a :
        #     while i in b:
        #         if i not in final:
        #             final.append(i)
        # for j in b:
        #     while j in a:
        #         if j not in final:
        #             final.append(j)
        
        # return final        
        
        # code here
