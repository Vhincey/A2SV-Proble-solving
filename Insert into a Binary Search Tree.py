# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        newroot = TreeNode()

        if not root:
            root = newroot
            newroot.val = val
            return root
        
        if val > root.val:
            if root.right is None:
                root.right = newroot
                newroot.val = val   
            self.insertIntoBST(root.right, val)

        elif val < root.val:
            if root.left is None:
                root.left = newroot
                newroot.val = val
            self.insertIntoBST(root.left, val)
            
        return root
