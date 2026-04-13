class Solution:
    def isPalindrome(self, s):
        #Easy Way  
        b = s[::-1]
        if s == b:
            return True
        
        
        
        #Complex Way Using Pointer
        # a = 0
        # b = len(s)-1
        # while a < b:
        #     if s[a] != s[b] :
        #         return False
        #     a += 1
        #     b -= 1
        # return True
        

        
