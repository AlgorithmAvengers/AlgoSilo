# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.box = set()
    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            self.box.add(root.val)
            self.inorder(root.right)
    def fixorder(self, root):
        if root is not None:
            self.fixorder(root.left)
            root.val = self.box.__next__()
            self.fixorder(root.right)
    
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.inorder(root)
        # print(sorted(self.box))
        self.box = iter(sorted(self.box))
        self.fixorder(root)