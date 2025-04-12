class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        self.triangle = triangle
        
        n = len(triangle)

        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])


        return triangle[0][0]


    
    # Part of my first attempt when trying to use a greedy algorithm, it failed
    def recurse(self, colIndex: int, rowIndex: int, total: int):
        
        # Only for if there is a tiny triangle which can not be traversed
        if len(self.triangle) < colIndex + 2:
            return total

        # Reached the bottom, return the total plus the smallest element on the bottom
        if len(self.triangle) < colIndex + 3:
            return min(
                self.triangle[colIndex + 1][rowIndex],
                self.triangle[colIndex + 1][rowIndex + 1]
            ) + total 

        if self.triangle[colIndex + 1][rowIndex] <= self.triangle[colIndex + 1][rowIndex + 1]:
            nextRowIndex = rowIndex
            total += self.triangle[colIndex + 1][rowIndex]
        else:
            nextRowIndex = rowIndex + 1
            total += self.triangle[colIndex + 1][rowIndex + 1]
        return self.recurse(colIndex + 1, nextRowIndex, total)


triangle = [[-1],[2,3],[1,-1,-3]]

solution = Solution()
str = solution.minimumTotal(triangle)

print(str)