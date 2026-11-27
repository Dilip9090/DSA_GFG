class Solution:
    def kthElement(self, arr1, arr2, k):
        # code here
        arr = []
        n = len(arr1)
        m = len(arr2)
        
        low = 0
        high = 0
        
        while low < n and high < m:
            if arr1[low] < arr2[high]:
                arr.append(arr1[low])
                low += 1
            else:
                arr.append(arr2[high])
                high += 1
        while low < n:
            arr.append(arr1[low])
            low += 1
        while high < m:
            arr.append(arr2[high])
            high += 1
        return arr[k-1]    