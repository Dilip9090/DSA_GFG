class Solution:
    def isPalindrome(self, s):
        #Using Recursion
        def check(left, right):
            if left >= right:
                return True
            
            if s[left] != s[right]:
                return False
            
            return check(left + 1, right - 1)
        
        return check(0, len(s) - 1)
        
        
        
        #Easy Way  
        # b = s[::-1]
        # if s == b:
        #     return True
        # code here
        
        
        #Complex Way Using Pointer
        # a = 0
        # b = len(s)-1
        # while a < b:
        #     if s[a] != s[b] :
        #         return False
        #     a += 1
        #     b -= 1
        # return True
        

        
