class Solution:
    def mergeArrays(self, arr1, arr2):
        # code here
        arr3 = []
        n = len(arr1)
        m = len(arr2)
        p = len(arr3)
        left = 0
        right = 0
        
        while left < n and right < m:
            if arr1[left] <= arr2[right]:
                arr3.append(arr1[left])
                left += 1
            else:
                arr3.append(arr2[right])
                right += 1
        while left < n:
            arr3.append(arr1[left])
            left += 1
        while right < m:
            arr3.append(arr2[right])
            right += 1
        
        for i in range(n):
            arr1[i] = arr3[i]
        for j in range(m):
            arr2[j] = arr3[j + n]
        
            