# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return mirror(left.left, right.right) and mirror(left.right, right.left)
        return mirror(root, root)

# 2
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = deque([root.left, root.right])
        
        while queue:
            left = queue.popleft()
            right = queue.popleft()
            
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        
        return True
            
