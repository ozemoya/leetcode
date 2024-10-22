# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        
        if key < root.val:
            # Search in the left subtree
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            # Search in the right subtree
            root.right = self.deleteNode(root.right, key)
        else:
            # Node to be deleted is found
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # Node with two children, find the in-order successor
            successor = self.minValueNode(root.right)
            root.val = successor.val
            # Delete the in-order successor
            root.right = self.deleteNode(root.right, successor.val)
        
        return root

    def minValueNode(self, node: TreeNode) -> TreeNode:
        current = node
        while current.left:
            current = current.left
        return current