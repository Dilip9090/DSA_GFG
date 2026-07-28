class Solution:
    def getPairs(self, arr):
        # code here
        mpp = {}
        ans = set()
        
        for num in arr:
            if -num in mpp:
                ans.add((min(num, -num), max(num, -num)))

            mpp[num] = 1

        res = []

        for pair in sorted(ans):
            res.append([pair[0], pair[1]])

        return res