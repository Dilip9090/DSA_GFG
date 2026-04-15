class Solution:
    def intersection(self,a, b):
        # optimal solution
        return sorted(list(set(a) & set(b)))
        
        
        
        
        # #brute force solution
        # pop = []
        # a = list(a)
        # b = list(b)
        # for i in b:
        #     if i in a and i not in pop:
        #         pop.append(i)
        # return pop
        # # code here
        