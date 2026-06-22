class Solution:
    def topKSumPairs(self, a, b, k):
        # code here
        n = len(a)

        a.sort(reverse=True)
        b.sort(reverse=True)

        maxHeap = []
        visited = set()

        heapq.heappush(maxHeap, (-(a[0] + b[0]), 0, 0))
        visited.add((0, 0))

        ans = []

        while k:

            currSum, i, j = heapq.heappop(maxHeap)

            ans.append(-currSum)

            if i + 1 < n and (i + 1, j) not in visited:
                heapq.heappush(
                    maxHeap,
                    (-(a[i + 1] + b[j]), i + 1, j)
                )
                visited.add((i + 1, j))

            if j + 1 < n and (i, j + 1) not in visited:
                heapq.heappush(
                    maxHeap,
                    (-(a[i] + b[j + 1]), i, j + 1)
                )
                visited.add((i, j + 1))

            k -= 1

        return ans