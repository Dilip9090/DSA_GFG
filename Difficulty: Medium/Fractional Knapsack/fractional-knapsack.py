class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        #code here
        items = []

        for i in range(len(val)):
            items.append((val[i] / wt[i], val[i], wt[i]))

        items.sort(reverse=True)

        total = 0.0

        for ratio, value, weight in items:

            if capacity >= weight:
                total += value
                capacity -= weight

            else:
                total += ratio * capacity
                break

        return round(total, 6)