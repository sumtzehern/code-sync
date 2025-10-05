class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) == 0:
            return []

        res = []
        level = []
        self.dfs(res, level, nums, 0)

        return res

    # helper function to explore every single path
    def dfs(self, res, level, nums, index):
        # Base case: done explore every element
        if index == len(nums):
            res.append(list(level)) # shallow copy
            return

        # case1: add
        level.append(nums[index])
        self.dfs(res, level, nums, index + 1)
        level.pop()

        self.dfs(res, level, nums, index + 1)

'''
Question: Given int arr unique elemenet, reuturn all possible subet

- solution can be in any order
- set must not contain duplicate subet
- input: list[]
- output: list[list[]]
- all number are unique
- assume the input not null, or empty

HIghLevel: dfs to backtrack and explore all possible subset, and add it into the res
Detail:

Base case:
finish exploring the element, add to res and stop
index == len(list), return

subproblem
                                []
                            /          \
                            1           []
                        /     \       /     \
                    1, 2       1     2      []
                /      \    /    \ /  \   /   \
            1,2,3     1,2  1,3   1  2,3 2 3   []
case1: add
    append(arr[i])
    dfs(i+1)
    dfs.delete previous element

case2: not add
        dfs(i+1)

tc: o(2^n)
sc: o(N)
'''