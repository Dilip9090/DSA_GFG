class Solution:
    def countAndSay(self, n):
        # code here
        ans = "1"

        for _ in range(1, n):

            temp = ""
            count = 1

            for i in range(1, len(ans) + 1):

                if i < len(ans) and ans[i] == ans[i - 1]:
                    count += 1
                else:
                    temp += str(count) + ans[i - 1]
                    count = 1

            ans = temp

        return ans