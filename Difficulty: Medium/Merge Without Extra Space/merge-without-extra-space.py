class Solution:
    def swapthegrater(self, arr1, arr2, idx1, idx2):
        if arr1[idx1] > arr2[idx2]:
            arr1[idx1], arr2[idx2] = arr2[idx2], arr1[idx1]
    def mergeArrays(self, arr1, arr2):
        # code here
        n = len(arr1)
        m = len(arr2)
        
        length = m + n
        
        gap = (length // 2) + (length % 2)
        
        while gap > 0:
            left = 0 
            right = left + gap
            
            while right < length:
                
                if left < n and right >= n:
                    self.swapthegrater(arr1, arr2, left, right - n)
                elif left >= n:
                    self.swapthegrater(arr2, arr2, left - n, right - n)
                else:
                    self.swapthegrater(arr1, arr1, left, right)
                left += 1
                right += 1
            if gap == 1:
                break
            gap = (gap // 2) + (gap % 2)
        
        
        
        
        
        
        
        
        
        
        
        # n = len(arr1)
        # m = len(arr2)
        # left = n - 1
        # right = 0
        # while left >= 0 and right < m:
        #     if arr1[left] > arr2[right]:
        #         arr1[left], arr2[right] = arr2[right], arr1[left]
        #         left -= 1
        #         right += 1
        #     else:
        #         break
        # arr1.sort()
        # arr2.sort()
        
        
        
        
        
        
        # arr3 = []
        # n = len(arr1)
        # m = len(arr2)
        # left = 0
        # right = 0
        
        # while left < n and right < m:
        #     if arr1[left] <= arr2[right]:
        #         arr3.append(arr1[left])
        #         left += 1
        #     else:
        #         arr3.append(arr2[right])
        #         right += 1
        # while left < n:
        #     arr3.append(arr1[left])
        #     left += 1
        # while right < m:
        #     arr3.append(arr2[right])
        #     right += 1
        
        # for i in range(n + m):
        #     if i < n:
        #         arr1[i] = arr3[i]
        #     else:
        #         arr2[i - n] = arr3[i]
        
            