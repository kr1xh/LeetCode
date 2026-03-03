# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        inorder_index = {value: idx for idx, value in enumerate(inorder)}
        self.post_idx = len(postorder) - 1
        
        def helper(left: int, right: int):
            if left > right:
                return None
            
            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            
            root = TreeNode(root_val)
            index = inorder_index[root_val]
            
            root.right = helper(index + 1, right)
            root.left = helper(left, index - 1)
            
            return root
        
        return helper(0, len(inorder) - 1)