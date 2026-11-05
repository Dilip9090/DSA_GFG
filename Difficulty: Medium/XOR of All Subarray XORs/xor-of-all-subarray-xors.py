class Solution:
    def subarrayXor(self, arr):
        # code here 
        if len(arr) % 2 == 0:
            return 0

        ans = 0
        for i in range(0, len(arr), 2):
            ans ^= arr[i]

        return ans        