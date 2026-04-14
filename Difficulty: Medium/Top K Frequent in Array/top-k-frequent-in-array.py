class Solution:
    def topKFreq(self, arr, k):
        
        freq = {}
        
        
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        sorted_items = sorted(freq.items(), key=lambda x: (-x[1], -x[0]))
        

        result = []
        for i in range(k):
            result.append(sorted_items[i][0])
        
        return result
		
		