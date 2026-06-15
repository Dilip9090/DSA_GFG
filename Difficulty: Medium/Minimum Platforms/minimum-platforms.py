class Solution:    
    def minPlatform(self, arr, dep):
        # code here
        n = len(arr)
        arr.sort()
        dep.sort()

        i = 0
        j = 0

        platforms = 0
        ans = 0

        while i < n and j < n:

            if arr[i] <= dep[j]:
                platforms += 1
                ans = max(ans, platforms)
                i += 1
            else:
                platforms -= 1
                j += 1

        return ans