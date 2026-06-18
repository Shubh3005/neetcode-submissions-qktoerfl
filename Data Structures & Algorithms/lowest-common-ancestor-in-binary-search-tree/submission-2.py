# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sameTree(self, root, p, q):
        if root is None:
            return 0
        return (root.val in (p.val,q.val)) + self.sameTree(root.left,p,q) + self.sameTree(root.right, p, q)


        

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.left  and self.sameTree(root.left,p,q) ==2:
            return self.lowestCommonAncestor(root.left,p,q)
        if root and self.sameTree(root.right,p,q) ==2:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root