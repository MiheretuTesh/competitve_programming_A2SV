from itertools import permutations


class Solution(object):
    def largestNumber(self, nums):
        lst = self.permute(nums)
        return max(lst)
    def permute(self, s):
        out = []

        if len(s) == 1:
            out = [s]
        else:
            for i,let in enumerate(s):
                for perm in self.permute(s[:i]+s[i+1:]):
                    out += [let+perm]
        return out
        
soln = Solution()
print(soln.largestNumber("123"))
