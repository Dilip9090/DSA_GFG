class Solution:
    # Function to calculate factorial of a number.
    def factorial(self, n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)
        # code here