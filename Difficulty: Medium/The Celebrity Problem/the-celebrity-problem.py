class Solution:
    def celebrity(self, mat):
        # code here
        n = len(mat)

        stack = []

        for i in range(n):
            stack.append(i)

        while len(stack) > 1:

            a = stack.pop()
            b = stack.pop()

            if mat[a][b] == 1:
                stack.append(b)
            else:
                stack.append(a)

        candidate = stack.pop()

        for i in range(n):

            if i != candidate:

                if mat[candidate][i] == 1 or mat[i][candidate] == 0:
                    return -1

        return candidate