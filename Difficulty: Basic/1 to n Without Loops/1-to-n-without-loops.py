class Solution:
    def printTillN(self, N):
        # i = 1
        if N == 0:
            return 
        self.printTillN(N-1)
        print(N,end=" ")
    	#code here 