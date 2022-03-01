class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        def dfs(row, col):
            image[row][col] = newColor
            visited.add((row, col))
            
            for direction in DIR:
                new_r, new_c = row+direction[0], col+direction[1]
                if not in_bound(new_r,new_c) or (new_r, new_c) in visited or image[new_r][new_c] != origin_color:
                    continue
                dfs(new_r, new_c)
        in_bound = lambda row, col : 0 <= row < len(image) and 0 <= col < len(image[0])
        
        origin_color = image[sr][sc]
        image[sr][sc] = newColor
        DIR = [[0,1],[1,0],[-1,0],[0,-1]]
        visited =set([(sr,sc)])
        dfs(sr, sc)
        return image