class Solution:
    def longestConsecutive(self, arr):
        #Optimal Solution
        arr1 = set(arr)
        n = len(arr1)
        small = 0
        count = 1
        longest = 1
        for i in arr1:
            if i - 1 not in arr1:
                small = i
                count = 1
                while small + 1 in arr1:
                    count += 1
                    small += 1
                longest = max(longest,count)    
        return longest         
        # #Batter Solution
        # arr.sort()
        # n = len(arr)
        # longest = 1
        # count = 1
        # lastsmall = float('-inf')
        
        # for i in range(n):
        #     if arr[i] - 1 == lastsmall:
        #         count += 1
        #         lastsmall = arr[i]
        #     elif arr[i] != lastsmall:
        #         count = 1
        #         lastsmall = arr[i]
        #     longest = max(longest, count)    
        # return longest    
                
        
        # Brute Force
        # n = len(arr)
        # longest = 1

        # for i in range(n):
        #     x = arr[i]
        #     count = 1

        #     while True:
        #         found = False

        #         for j in range(n):
        #             if arr[j] == x + 1:
        #                 found = True
        #                 x += 1
        #                 count += 1
        #                 break

        #         if not found:
        #             break

        #     longest = max(longest, count)

        # return longest