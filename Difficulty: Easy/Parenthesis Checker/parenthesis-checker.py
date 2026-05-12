class Solution:
    def isBalanced(self, s):
        # code here
        stack = []
        
        # mapping closing → opening
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            else:
                # if stack empty or mismatch
                if not stack or stack[-1] != mapping[ch]:
                    return False
                stack.pop()
        
        return len(stack) == 0
        
        