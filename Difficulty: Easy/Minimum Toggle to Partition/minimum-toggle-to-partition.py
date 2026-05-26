class Solution:
    def minToggle(self, arr):
        # code here
        n = len(arr)

        # count total 0s and 1s
        total0 = arr.count(0)
        total1 = arr.count(1)

        left1 = 0
        right0 = total0
        ans = n

        for i in range(n + 1):
            
            # toggles needed:
            # left side should contain only 0s
            # right side should contain only 1s
            ans = min(ans, left1 + right0)

            if i < n:
                if arr[i] == 1:
                    left1 += 1
                else:
                    right0 -= 1

        return ans
 