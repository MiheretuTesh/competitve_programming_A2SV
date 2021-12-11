
class Solution(object):
    def kClosest(self, points, k):
        
        # closest_distance = Solution.calcDistance(points[0])
        temp = []
        for i in range(0, len(points)):
            min = i
            for j in range(i+1, len(points)):
                if(((points[min][0])**2 + (points[min][1])**2)>((points[j][0])**2 + (points[j][1])**2)):
                    min = j
            points[min], points[i] = points[i], points[min]
        for i in range(k):
            temp.append(points[i])
                
        return temp
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
soln = Solution()
print(soln.kClosest([[1,3],[-2,2]],
1138))