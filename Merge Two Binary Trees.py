# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        
        mergeroot = TreeNode((root1.val if root1 else 0) + (root2.val if root2 else 0))

        mergeroot.left = self.mergeTrees(root1.left if root1 else None,root2.left if root2 else None)
        mergeroot.right = self.mergeTrees(root1.right if root1 else None,root2.right if root2 else None)
        return mergeroot

# 2
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
      
        if not root1:
            return root2
        if not root2:
            return root1
        
        mergeroot = TreeNode(root1.val + root2.val)

        mergeroot.left = self.mergeTrees(root1.left ,root2.left)
        mergeroot.right = self.mergeTrees(root1.right ,root2.right)
        return mergeroot

# 3
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root1:
            return root2
        if not root2:
            return root1
      
        root1.val += root2.val

        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1
