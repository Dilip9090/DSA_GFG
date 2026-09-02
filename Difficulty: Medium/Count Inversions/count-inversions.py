class Solution:
    def inversionCount(self, arr):
        # code here
        n = len(arr)
        return self.mergeSort(arr, 0, n - 1)
    
    
    
    
    def mergeSort(self, arr, l, r):
        # code here
        count = 0
        if l >= r:
            return 0
        m = (l + r) // 2
        count += self.mergeSort(arr, l, m)
        count += self.mergeSort(arr, m + 1, r)
        count += self.merge(arr, l, m, r)
        return count
    def merge(self,arr, l, m, r):
        left = l
        right = m + 1
        temp = []
        count = 0

        while left <= m and right <= r:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                count += (m - left + 1)
                right += 1
        while left <= m:
            temp.append(arr[left])
            left += 1
        while right <= r:
            temp.append(arr[right])
            right += 1

        for i in range(l, r + 1):
            arr[i] = temp[i - l]
        return count
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        # n = len(arr)
        # count = 0
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if arr[i] > arr[j]:
        #             count += 1
        # return count             