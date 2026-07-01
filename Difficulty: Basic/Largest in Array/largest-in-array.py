class Solution:
    def largest(self, arr):
        # code here
        maz = 0
        for i in arr:
            if i > maz :
                maz = i
        return maz        