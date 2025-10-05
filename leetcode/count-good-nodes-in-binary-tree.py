# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # if not root: # empty node
        #     return 0
        if not root.left and not root.right: # one node
            return 1

        good_nodes = [0]
        cur_max = root.val

        self.dfs(good_nodes, root, cur_max)

        return good_nodes[0]
    
    def dfs(self, good_nodes, root, cur_max):
        # base case: when reached end
        if not root:
            return 0

        # check if they are good nodes
        if root.val >= cur_max:
            good_nodes[0] += 1

        # update good nodes
        cur_max = max(cur_max, root.val)

        # dfs to the right and left
        self.dfs(good_nodes, root.left, cur_max)
        self.dfs(good_nodes, root.right, cur_max)

        return good_nodes[0]