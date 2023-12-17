class Solution:
    # @param A : list of list of integers
    # @return an integer
    def checkPath(self, A):
        self.matrix = A
        self.rows, self.cols = len(A), len(A[0])
        self.visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        source_row, source_col = self.find_location(1)
        destination_row, destination_col = self.find_location(2)
        if source_row is None or source_col is None or destination_row is None or destination_col is None:
            return 0
        
        paths = lambda x, y: [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        self.visited[source_row][source_col] = True
        queue = [(source_row, source_col)]
        while queue:
            row, col = queue.pop(0)
            if self.matrix[row][col] == 2:
                return 1
            
            for adj_row, adj_col in paths(row, col):
                if self.valid_location(adj_row, adj_col):
                    if self.matrix[adj_row][adj_col] == 2:
                        return 1

                    self.visited[adj_row][adj_col] = True
                    queue.append((adj_row, adj_col))
        
        return 0
    
    
    def valid_location(self, row, col):
        return row >= 0 and row < self.rows and col >= 0 and col < self.cols and \
            not self.visited[row][col] and (self.matrix[row][col] == 3 or self.matrix[row][col] == 2)
        
    
    def find_location(self, val):
        for i in range(self.rows):
            col = self.matrix[i]
            if val in col:
                return i, col.index(val)
        
        return None, None
                
        
if __name__ == "__main__":
    A = [[1, 0], [0, 2]]
    print(Solution().checkPath(A))
    A = [[1, 3], [3, 2]]
    print(Solution().checkPath(A))