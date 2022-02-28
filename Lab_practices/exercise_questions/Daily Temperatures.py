class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures)
        stack = []
        result = [0] * size 
        for i in range(size):
            if not stack:
                stack.append((temperatures[i], i))
            else:
                while stack and stack[-1][0] < temperatures[i]:
                    value, index = stack.pop()
                    result[index] = i - index
                stack.append((temperatures[i], i))
        return result