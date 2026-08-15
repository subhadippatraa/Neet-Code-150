# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def valid(self,root,mini,maxi)->bool:
        if root is None:
            return True
        
        if(root.val >=maxi or root.val<=mini):
            return False
        
        return self.valid(root.left,mini,root.val) and self.valid(root.right,root.val,maxi)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.valid(root,-1000000000 ,1000000000)
        