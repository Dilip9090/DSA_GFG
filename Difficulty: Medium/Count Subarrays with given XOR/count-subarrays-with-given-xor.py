class Solution:
    def subarrayXor(self, arr, k):
        # code here
        xor_count = {0: 1}

        xr = 0
        count = 0

        for num in arr:
            xr ^= num

            count += xor_count.get(xr ^ k, 0)

            xor_count[xr] = xor_count.get(xr, 0) + 1

        return count
        