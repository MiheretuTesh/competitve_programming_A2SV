class Solution:
    def merge(self, intervals):
        size = len(intervals)
        intervals.sort()
        count=0
        while (count<size-1):
            if intervals[count][1]>=intervals[count+1][0]:
                base = max(intervals[count+1][1],intervals[count][1])
                intervals[count]=[intervals[count][0], base]
                intervals.pop(count+1)
                size-=1
                continue
            count+=1
        return intervals

        # for i in range()
soln = Solution()
print(soln.merge([[1,4],[2,3]]))
