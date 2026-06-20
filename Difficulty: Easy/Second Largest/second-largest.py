class Solution:
    def getSecondLargest(self, arr):
        # code here
        
        large = -1
        second = -1
        
        for nums in arr:
            if nums > large:
                second = large
                large = nums
            elif large > nums > second:
                second = nums
        return second        