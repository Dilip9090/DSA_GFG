class Solution:
    def maxPeopleDefeated(self, p):
        # code here
        low, high = 0, 10000
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            total = mid * (mid + 1) * (2 * mid + 1) // 6

            if total <= p:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans