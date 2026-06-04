class Solution:
    def findTwoElement(self, arr):
        # code here
        n = len(arr)

        expected_sum = n * (n + 1) // 2
        actual_sum = sum(arr)

        expected_sq_sum = n * (n + 1) * (2 * n + 1) // 6
        actual_sq_sum = sum(x * x for x in arr)

        diff = actual_sum - expected_sum         
        sq_diff = actual_sq_sum - expected_sq_sum

        sum_xy = sq_diff // diff                 

        repeating = (diff + sum_xy) // 2
        missing = repeating - diff

        return [repeating, missing]
