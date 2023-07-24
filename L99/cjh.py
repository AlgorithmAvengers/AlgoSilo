# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # tree를 inorder로 정리하기 위한 array
        self.arr = []

        # tree를 inorder로 traversal하기 위한 함수
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.arr.append(node)
            inorder(node.right)
        
        # tree inorder traversal
        inorder(root)

        # tree 내부의 숫자를 오름차순으로 정리
        sort = sorted(leaf.val for leaf in self.arr)

        # 오름차순으로 정리한 값을 inorder tree에 넣어주기
        for i in range(len(sort)):
            self.arr[i].val = sort[i]