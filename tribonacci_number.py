class Solution:
    def tribonacci(self, n: int) -> int:
        seq = [0, 1, 1]
        curr_pos = 3

        while curr_pos <= n:
            seq.append(seq[curr_pos - 3] + seq[curr_pos - 2] + seq[curr_pos - 1])
            curr_pos += 1
        return seq[n]
    
solution = Solution()
str = solution.tribonacci(25)
print(str)