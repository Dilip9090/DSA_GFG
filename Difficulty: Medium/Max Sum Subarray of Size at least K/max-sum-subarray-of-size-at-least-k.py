class Solution:
    def maxSumWithK(self, arr: list[int], k: int) -> int:
        # code here
        n = len(arr)

        max_end = [0] * n
        max_end[0] = arr[0]

        for i in range(1, n):
            max_end[i] = max(arr[i], max_end[i - 1] + arr[i])

        curr = sum(arr[:k])
        ans = curr

        for i in range(k, n):
            curr += arr[i] - arr[i - k]

            ans = max(ans, curr)

            ans = max(ans, curr + max_end[i - k])

        return ans