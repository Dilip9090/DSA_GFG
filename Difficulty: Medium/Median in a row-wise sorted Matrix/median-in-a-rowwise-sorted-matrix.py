class Solution:
    def median(self, mat):
    	# code here 
    	n = len(mat)
        m = len(mat[0])

        low = min(row[0] for row in mat)
        high = max(row[m - 1] for row in mat)

        req = (n * m) // 2

        while low <= high:

            mid = (low + high) // 2

            count = 0

            for row in mat:
                count += bisect_right(row, mid)

            if count <= req:
                low = mid + 1
            else:
                high = mid - 1

        return low