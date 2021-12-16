class Solution:
    def minPairSum(self, nums: List[int]) -> int:
    
        first = 0
        last = len(nums) - 1
        lst = []
        nums.sort()
        for i in range(len(nums)):
            lst.append(nums[(first+i)]+nums[(last-i)])
        return max(lst)