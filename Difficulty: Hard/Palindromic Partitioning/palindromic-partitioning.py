#User function Template for python3

class Solution:
    def palPartition(self, s):
        # code here
        n = len(s)

        isPal = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):

                if s[i] == s[j]:

                    if j - i <= 1:
                        isPal[i][j] = True
                    else:
                        isPal[i][j] = isPal[i + 1][j - 1]

        dp = [0] * (n + 1)

        dp[n] = 0

        for i in range(n - 1, -1, -1):

            ans = float('inf')

            for j in range(i, n):

                if isPal[i][j]:
                    ans = min(ans, 1 + dp[j + 1])

            dp[i] = ans

        return dp[0] - 1