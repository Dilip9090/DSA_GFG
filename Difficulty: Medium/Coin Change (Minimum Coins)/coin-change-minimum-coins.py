class Solution:
	def minCoins(self, coins, sum):
		# code here
		dp = [float('inf')] * (sum + 1)

        dp[0] = 0

        for amount in range(1, sum + 1):

            for coin in coins:

                if coin <= amount:
                    dp[amount] = min(dp[amount],
                                     dp[amount - coin] + 1)

        return dp[sum] if dp[sum] != float('inf') else -1
		