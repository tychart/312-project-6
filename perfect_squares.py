import math

class Solution:
    def __init__(self):
        squares = 0
    
    def numSquares(self, n: int) -> int:
        self.squares = self.genSquares(n)
        total = 0

        matrix = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        for i in range(n):
            for j in range(n):
                

        # for i in range(n):
        #     for j in range(n):
        #         if i == 0:
        #             matrix[i][j] = 0
        #         elif j == 0:
        #             matrix[i][j] = 0
        #         elif i == j:
        #             matrix[i][j] = 1
        #         else:
        #             matrix[i][j] = min(
        #                 matrix[i][j - 1], 
        #                 matrix[i - squares[j]][j] + 1,
        #                 matrix[i][j - 1] + 1
        #             )

        # while n > 0:
        #     for x in self.squares:
        #         if x <= n:
        #             n -= x
        #             total += 1
        #             break
        # return total
    
    # def recurse(self, squares)
        
    

    def genSquares(self, n: int) -> list[int]:
        out_list = []
        for i in range(1, math.floor(math.sqrt(n)) + 1):
            out_list.append(i * i)
        out_list.reverse()
        return out_list


solution = Solution()
print(solution.numSquares(12))  # Output: 3