class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        initial = 0
        size = len(height)-1
        area = 0
        while initial< size:
            
            h = min(height[initial], height[size])
            area = max(area, h*(size - initial))
            
            if height[initial]<height[size]:
                initial += 1
            else:
                size -= 1
        return area
            