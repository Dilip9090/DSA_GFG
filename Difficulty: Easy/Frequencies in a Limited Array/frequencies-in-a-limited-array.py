class Solution:
    def frequencyCount(self, arr):
        n = len(arr)
        
        fre = {}
        
        for num in arr:
            fre[num] = fre.get(num, 0) + 1
        
        resu = [0] * n
        
        for i in range (1, n+1):
            resu[i - 1]= fre.get(i , 0)
        return resu    
        
        
        
        # n = max(arr) + 1
        # freq = [0] * n
        # # p = len(hash)
        # arr.remove(0)
        
        # for nums in arr:
        #     freq[nums-1] += 1
            
        # return freq

