class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:

        def dfs(node, path_sum):

            if not node:
                return None

            path_sum += node.val

            if not node.left and not node.right: # Leaf node
                if path_sum < limit:
                    return None
                return node

            node.left = dfs(node.left, path_sum) # Process children first
            node.right = dfs(node.right, path_sum)

            if not node.left and not node.right:
                return None

            return node

        return dfs(root, 0)