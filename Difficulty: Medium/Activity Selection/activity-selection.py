class Solution:
    def activitySelection(self, start, finish):
        #code here
        activities = list(zip(start, finish))

        activities.sort(key=lambda x: x[1])

        count = 1
        last_finish = activities[0][1]

        for s, f in activities[1:]:

            if s > last_finish:
                count += 1
                last_finish = f

        return count