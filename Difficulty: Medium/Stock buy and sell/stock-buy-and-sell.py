class Solution:
    #Function to find the days of buying and selling stock for max profit.
	def stockBuySell(self, arr):
        # code here
        n = len(arr)
        profit = 0
        
        for i in range(n-1):
            if arr[i] < arr[i+1]:
                profit += arr[i] - arr[i+1]
        return - profit        