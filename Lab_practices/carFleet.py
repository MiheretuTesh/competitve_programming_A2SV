class Solution:
    def carFleet(self, target: int, position, speed) -> int:
        lst = []
        for i in range(len(position)):
            lst.append([position[i], speed[i]])
        # lst.append([position[i], speed[i]] for i in range(len(position)))
        lst.sort(key= lambda x: x[0])
        for i in range(len(lst)):
            lst[i][0] = ((target-lst[i][0])/lst[i][1])
        print(lst)
        
        currentFleet = 0
        finalFleet = 0
        # lst3 = reversed(lst2)
        # print(lst3)
        for i in reversed(lst):
            if i[0]>currentFleet:
                currentFleet = i[0]
                finalFleet += 1
        return finalFleet
    
soln = Solution()
print(soln.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))