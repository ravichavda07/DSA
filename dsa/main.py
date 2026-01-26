class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.data = value
        
def insert(root,value):
    if(root == None):
        return Node(value)
    if(root.data == value):
        return root
    if(root.data > value):
        root.left = insert(root.left,value)
    else:
        root.right = insert(root.right,value)
    return root

def inorder(root):
    if(root != None):
        inorder(root.left)
        print(root.data, end="->")
        inorder(root.right)

root = insert(None,20)
root = insert(root,15)
root = insert(root,30)
root = insert(root,40)
root = insert(root,12)
root = insert(root,18)
root = insert(root,25)
inorder(root)