class Solution:
    def countStrings(self, n, k): 
        # code here 
        MOD = 10**9 + 7

        dp0 = [[0] * (k + 1) for _ in range(n + 1)]
        dp1 = [[0] * (k + 1) for _ in range(n + 1)]

        dp0[1][0] = 1
        dp1[1][0] = 1

        for i in range(2, n + 1):
            for j in range(k + 1):
                dp0[i][j] = (dp0[i - 1][j] + dp1[i - 1][j]) % MOD
                dp1[i][j] = (dp0[i - 1][j] + (dp1[i - 1][j - 1] if j > 0 else 0)) % MOD

        return (dp0[n][k] + dp1[n][k]) % MOD
