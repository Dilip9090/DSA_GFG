class Solution:
    def subarraySum(self, arr, target):
        # code here
        
        left = 0
        right = 0
        n = len(arr)
        sum1 = 0
        while right < n:
            sum1 += arr[right]
            while left <= right and sum1 > target:
                sum1 -= arr[left]
                left += 1
            if sum1 == target:
                return [left +1, right+1]
            right += 1
        return [-1]    