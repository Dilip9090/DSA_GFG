class Solution:
    def visibleBuildings(self, arr):
        # code here
        height = 0
        count = 0
        
        for i in arr:
            if i >= height:
                count += 1
                height = i
        return count