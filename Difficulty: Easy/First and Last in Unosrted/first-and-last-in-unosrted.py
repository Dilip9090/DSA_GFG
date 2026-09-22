class Solution:
    def findIndex (self, arr, key):
        #code here
        n = len(arr)
        first, last = -1, -1
        
        for i in range(n):
            if arr[i] == key:
                if first == -1:
                    first = i
                    last = i
                elif first != -1:
                    last = i
        return (first, last)            