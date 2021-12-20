class Solution:
    def dailyTemperatures(self, temperatures):
        count = 0
        lst = []
        for i in range(len(temperatures)):
            
            for j in range(i+1, len(temperatures)):
                if(temperatures[i]<temperatures[j]):
                    count += 1
                    lst.append(count)
                    break
                else:
                    count += 1
            lst.append(count)
            count = 0
        return tuple(lst)


soln = Solution()
print(soln.dailyTemperatures([73,74,75,71,69,72,76,73]))