class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        if not arr:
            return ""

        prefix = arr[0]

        for word in arr[1:]:
            i = 0
            while i < len(prefix) and i < len(word) and prefix[i] == word[i]:
                i += 1
            prefix = prefix[:i]
            if prefix == "":
                return ""

        return prefix