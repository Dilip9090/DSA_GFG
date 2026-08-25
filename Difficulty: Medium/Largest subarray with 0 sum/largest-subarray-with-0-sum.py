class Solution:
    def maxLength(self, arr):
        # code here
        mpp = {}
        sum1 = 0
        maxlen = 0

        for i in range(len(arr)):

            sum1 += arr[i]

            if sum1 == 0:
                maxlen = i + 1

            elif sum1 in mpp:
                maxlen = max(maxlen, i - mpp[sum1])

            else:
                mpp[sum1] = i

        return maxlen        