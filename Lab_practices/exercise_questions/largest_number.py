class Solution(object):
    def largestNumber(self, nums):
        s = len(nums)
        for i in range(s-1):
            for j in range(i+1, s):
                if(self.compute(nums[i], nums[j])):
                    nums[i], nums[j] = nums[j], nums[i]
        return str(int("".join(map(str, nums))))
    def compute(self, num1, num2):
        num1 = str(num1)
        num2 = str(num2)
        return num1+num2<num2+num1