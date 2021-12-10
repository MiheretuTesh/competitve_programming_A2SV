class Solution(object):
    def reorganizeString(self, string):
        """
        :type s: str
        :rtype: str
        """
        s = list(string);
        count = 1
        elementIndex = 0
        length = len(s)
        for i in range(0, length-2):
            if(s[i]==s[i+1]):
                count += 1
                elementIndex = i+1
                print(elementIndex)
            else:
                count = 1
                continue
        if(count==2 and elementIndex<length-1):
            s[elementIndex], s[elementIndex+1] = s[elementIndex+1], s[elementIndex]
            
        return "".join(s)

        
        

soln = Solution()
print(soln.reorganizeString("aabba"))