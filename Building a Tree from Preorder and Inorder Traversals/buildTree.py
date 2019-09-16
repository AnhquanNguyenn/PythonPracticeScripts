class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def buildTree(root, inorder, preorder):
    
