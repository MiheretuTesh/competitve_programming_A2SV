from typing import Counter


class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        lst = []
        changed.sort()
        if(len(changed)%2!=0):
            return []
        nums = Counter(changed)
        
        for c in changed:
            if(c>0 and nums[c] and nums[c*2]):
                nums[c] -= 1
                nums[c*2] -= 1
                lst.append(c)
            elif c==0 and nums[c]>=2:
                nums[c] -= 2
                lst.append(c)
        if((len(changed))//2==len(lst)):
            return lst
        else:
            return []
                
        
        