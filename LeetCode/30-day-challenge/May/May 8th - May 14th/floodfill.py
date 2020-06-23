class Solution:
    def floodFill(self, image, sr, sc, newColor):
        if image == []:
            return []
        
        color = image[sr][sc]
        row, col = len(image), len(image[0])
        visited = [[False for i in range(col)] for j in range(row)]
        
        fill(image, sr, sc, row, col, color, newColor, visited)
        
        return image
    
    
def fill(image, sr, sc, row, col, color, newColor, visited):
    if sr < 0 or sr >= row or sc < 0 or sc >= col:
        return
    
    if image[sr][sc] != color or visited[sr][sc]:
        return
    
    
    image[sr][sc] = newColor
    visited[sr][sc] = True
    
    fill(image, sr - 1, sc, row, col, color, newColor, visited)
    fill(image, sr + 1, sc, row, col, color, newColor, visited)
    fill(image, sr, sc - 1, row, col, color, newColor, visited)
    fill(image, sr, sc + 1, row, col, color, newColor, visited)


print(f'The Solution is {Solution().floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)}')
        