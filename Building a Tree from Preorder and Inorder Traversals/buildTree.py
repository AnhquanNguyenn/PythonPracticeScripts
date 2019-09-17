class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def buildTree(inOrder, preOrder, inStart, inEnd):
    if inStart > inEnd:
        return None
    
    # Choosing a node to start out at, from our preorder traversal from the preIndex 
    # and the incremented preIndex
    tNode = Node(preOrder[buildTree.preIndex])
    buildTree.preIndex += 1
    
    # if the node has no children then we we move onto the next node
    if inStart == inEnd:
        return tNode
    
    # finding the index of the node in inorder traversal
    inIndex = search(inOrder, inStart, inEnd, tNode.data)
    
    # Constructing the left and right subtrees
    tNode.left = buildTree(inOrder, preOrder, inStart, inIndex - 1)
    tNode.right = buildTree(inOrder, preOrder, inIndex + 1, inEnd) 
    
    return tNode


def search(array, start, end, value):
    for i in range(start, end + 1): 
        if array[i] == value:
            return i     

def printInorderTraversal(node):
    if node is None:
        return 
    
    # Recursively find the left child to print
    printInorderTraversal(node.left)
    
    # Print the parent data
    print(node.data, end='')
    
    # Recursively find the right child to print
    printInorderTraversal(node.right)
    
    
    
inOrder = ['d', 'b', 'e', 'a', 'f', 'c', 'g']
preOrder = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
buildTree.preIndex = 0
inStart = 0
inEnd = len(inOrder) - 1
root = buildTree(inOrder, preOrder, inStart, inEnd)
printInorderTraversal(root)
print('\n')

