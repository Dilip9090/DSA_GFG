class Solution:
    def removeDuplicates(self, arr):
        # code here 
        arr = list(set(arr))
        arr.sort()
        return arr