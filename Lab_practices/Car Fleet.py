class Solution:
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        times = [float(target-p)/s for p, s in sorted(zip(position, speed))]
        result, curr = 0, 0
        print(times)
        lst = reversed(times)
        print(lst)
        for t in lst:
            if t > curr:
                print(t)
                print(curr)
                result += 1
                curr = t
        return result


soln = Solution()
print(soln.carFleet(12,
                    [10, 8, 0, 5, 3],
                    [2, 4, 1, 1, 3]))
