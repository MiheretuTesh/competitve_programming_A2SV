import math


class Solution(object):
    def kClosest(self, points, k):

        for i in range(len(points)):
            distance = self.calc_distance(points[i])
            points[i] = [distance, points[i]]

        points.sort(key=lambda point: point[0])

        return [points[i][1] for i in range(k)]

    def calc_distance(self, point):
        return math.sqrt((point[1])**2 + (point[0])**2)


# closest_distance = Solution.calcDistance(points[0])
        # points.sort(key )
        # for i in range(0, len(points)):
        #     min = i
        #     for j in range(i+1, len(points)):
        #         if(((points[min][0])**2 + (points[min][1])**2)>((points[j][0])**2 + (points[j][1])**2)):
        #             min = j
        #     points[min], points[i] = points[i], points[min]
        # return points[:k]

        # Second method of implementation

        # temp = [0] * len(points)


soln = Solution()
print(soln.kClosest([[2, 2], [2, -4], [3, 3]], 2))
