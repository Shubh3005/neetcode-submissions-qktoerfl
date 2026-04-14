# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        
        def preorder(root):
            if not root: return ["n"]
            else:
                return [str(root.val)]+preorder(root.left)+preorder(root.right)
        print(",".join(preorder(root)))
        return ",".join(preorder(root))

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals= data.split(",")
        self.idx = 0
        def dfs():
            root = None
            if vals[self.idx]== 'n':
                self.idx+=1
            else:
                root = TreeNode(int(vals[self.idx]))
                self.idx +=1
                root.left=dfs()
                root.right=dfs()
            return root
        return dfs()