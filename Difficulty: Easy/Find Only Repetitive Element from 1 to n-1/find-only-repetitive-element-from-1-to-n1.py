#User function Template for python3
class Solution:
    def findDuplicate(self, arr):
        arr.sort()
        lenth = len(arr)
        for i in range(lenth):
            if arr[i] == arr[i+1]:
                return arr[i]
                
        #code here