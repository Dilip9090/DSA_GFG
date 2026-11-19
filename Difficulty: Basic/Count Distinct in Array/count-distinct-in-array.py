class Solution:
    def countDistinct(self, arr: list[int]) -> int:
        # code here
        set1 = set()
        
        
        for i in range(len(arr)):
            set1.add(arr[i])
        return len(set1)    