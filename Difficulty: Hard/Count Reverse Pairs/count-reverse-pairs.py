class Solution:
    def countRevPairs(self, arr):
        # Code here
        n = len(arr)
        return self.mergeSort(arr, 0, n - 1)
        
        
    def countpair(self, arr, l, m, r):
        right = m + 1
        count = 0
        for i in range(l,m + 1):
            while right <= r and arr[i] > 2*arr[right]:
                right += 1
            count += right - (m + 1)
        return count     
                
    def mergeSort(self, arr, l, r):
        if l >= r:
            return 0
        count = 0    
        m = (l + r) // 2
        count += self.mergeSort(arr, l, m)
        count +=self.mergeSort(arr, m + 1, r)
        count += self.countpair(arr, l, m, r)
        self.merge(arr, l, m, r)
        return count
            
    def merge(self,arr, l, m, r):
        left = l
        right = m + 1
        temp = []

        while left <= m and right <= r:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
        while left <= m:
            temp.append(arr[left])
            left += 1
        while right <= r:
            temp.append(arr[right])
            right += 1

        for i in range(l, r + 1):
            arr[i] = temp[i - l]
        
        
        
        
        
        
        
        
        
        
        # n = len(arr)
        # count = 0
        # for i in range(n):
        #     total = 0
        #     for j in range(i + 1, n):
        #         total = arr[j] * 2
        #         if arr[i] > total:
        #             count += 1
        # return count            