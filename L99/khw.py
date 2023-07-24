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
        stack = []
        now =root
        last = None
        check = None

        while stack or now:
            while now:
                stack.append(now)
                now = now.left
            now = stack.pop()

            if last:
                if last.val > now.val:
                    if check:
                        check[1] = now
                        break
                    else:
                        check = [last, now]
            last = now
            now = now.right
        check[0].val, check[1].val = check[1].val, check[0].val
