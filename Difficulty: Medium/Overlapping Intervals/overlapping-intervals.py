class Solution:
	def mergeOverlap(self, arr):
		# Code here
		arr.sort()
		n = len(arr)
		ans = []
		for i in range(n):
		    start = arr[i][0]
		    end = arr[i][1]
		    if ans and start <= ans [-1][1]:
		        continue
		    for j in range(i + 1, n):
		        if arr[j][0] <= end:
		            end = max(end, arr[j][1])
		        else:
		            break
		    ans.append([start,end])      
		
		
		return ans 