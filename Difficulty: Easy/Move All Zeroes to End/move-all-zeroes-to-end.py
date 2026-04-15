class Solution:
	def pushZerosToEnd(self, arr):
        zero = []
        one = []
        
        for i in arr:
            if i == 0:
                zero.append(i)
            else:
                one.append(i)
        
        result = one + zero
        
        for i in range(len(arr)):
            arr[i] = result[i]
    	# code here