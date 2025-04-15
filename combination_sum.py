class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        nums = set(candidates)
        
        # Make an entry for a solution at each number leading up to the solution
        solutions: list[list[int]] = [[] for _ in range(target + 1)]
        solutions[0] = [[]]

        for currtarget in range(1, target + 1):
            for num in candidates:
                if currtarget - num >= 0: # If the current try is greater than half of num
                    for comb in solutions[currtarget - num]:
                        if not comb or num >= comb[-1]:
                            solutions[currtarget].append(comb + [num])

        return solutions[target]
        # # A dictionaries with the cost/subtarget and set of values in nums needed to make up that cost
        # partials: dict[int: set] = {}
        # print(nums)

        # max_loops = target // min(nums) 

        # for outer in range(max_loops):
        #     for i in range(target):
                
        #         if i in nums:
        #             if i == target:
        #                 solutions.append({i})
        #                 break
                
        #             if target - i in nums:
        #                 partials.add({i: })
        #                 solutions.append({i, target - i})
                    
        # return [list(comb) for comb in solutions]

        





solution = Solution()
string = solution.combinationSum([2,3,6,7], 7)

print(string)