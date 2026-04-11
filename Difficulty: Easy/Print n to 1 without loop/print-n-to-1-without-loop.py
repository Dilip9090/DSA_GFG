class Solution:
    def printNos(self, n):
        while n == 0:
            return
        print(n,end=" ")
        self.printNos(n-1)
        # print(n,end=" ")