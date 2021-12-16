class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = "([{"
        closing = ")]}"
        for i in range(len(s)):
            if s[i] in '({[':
                stack.append(s[i])
            else:
                if(stack):
                    indexP = stack[-1]
                    if opening.index(indexP) == closing.index(s[i]):
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return False if len(stack) else True