# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        self.longest = 0
        
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            left_path = right_path = 0
            
            if node.left and node.left.val == node.val:
                left_path = left + 1
            
            if node.right and node.right.val == node.val:
                right_path = right + 1
            
            self.longest = max(self.longest, left_path + right_path)
            
            return max(left_path, right_path)
        
        dfs(root)
        return self.longest