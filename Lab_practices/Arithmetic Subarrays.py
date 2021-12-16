class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):
        arithmeticLst = []
        temp = []
        sub = 0
        count = 0
        for i in range(len(l)):
            temp = nums[l[i]:r[i]+1]
            temp.sort()
            sub = temp[1] - temp[0]
            s = len(temp)-1
            count = 0
            while(count<s and sub == temp[1] - temp[0]):
                if(temp[count+1]-temp[count] == sub):
                    count+=1
                    continue
                else:
                    sub = temp[count+1] - temp[count]
            if(count == s):
                arithmeticLst.append(True)
            else:
                arithmeticLst.append(False)
        return arithmeticLst
                
            
            
soln = Solution()
print(soln.checkArithmeticSubarrays([-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10],[0,1,6,4,8,7],[4,4,9,7,9,10]))