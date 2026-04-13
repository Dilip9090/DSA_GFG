class Solution:
    def isPalindrome(self, s):
        a = 0
        b = len(s)-1
        while a < b:
            if s[a] != s[b] :
                return False
            a += 1
            b -= 1
        return True    
        
        # b = s[::-1]
        # if s == b:
        #     return True
        # code here
        
