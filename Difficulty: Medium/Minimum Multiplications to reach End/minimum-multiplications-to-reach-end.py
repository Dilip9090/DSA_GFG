from collections import deque
class Solution:
    def minSteps(self, arr, start, end):
        # code here
        if start == end:
            return 0

        MOD = 1000
        
        # distance array
        dist = [float('inf')] * MOD
        dist[start] = 0

        q = deque()
        q.append((start, 0))

        while q:
            num, steps = q.popleft()

            for x in arr:
                new_num = (num * x) % MOD

                if steps + 1 < dist[new_num]:
                    dist[new_num] = steps + 1

                    if new_num == end:
                        return steps + 1

                    q.append((new_num, steps + 1))

        return -1
