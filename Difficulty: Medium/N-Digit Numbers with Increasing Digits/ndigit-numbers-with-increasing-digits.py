class Solution:
    def increasingNumbers(self, n):
        # code here
        if n > 10:
            return []

        if n == 1:
            return [i for i in range(10)]

        ans = []

        def backtrack(num, last_digit, length):
            if length == n:
                ans.append(num)
                return

            for d in range(last_digit + 1, 10):
                backtrack(num * 10 + d, d, length + 1)

        for start in range(1, 10):
            backtrack(start, start, 1)

        return ans
