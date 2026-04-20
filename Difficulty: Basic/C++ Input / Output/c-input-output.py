#User function Template for python3
class Solution:
    def multiplication(self, A, B):
        result = 0
        for _ in range(abs(B)):
            result += A
        return result if B >= 0 else -result