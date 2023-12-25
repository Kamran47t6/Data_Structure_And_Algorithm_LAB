class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

def insert(node,key):
     if node==None:
        return Node(key)
     if key<node.key:
        node.left=insert(node.left,key)
     elif key>node.key:
        node.right=insert(node.right,key)

     return node
def Inorder(root):
     if root!=None:
         Inorder(root.left)
         print(root.key)
         Inorder(root.right)

def PreOrder(root):
     if root!=None:
        print(root.key)
        PreOrder(root.left)
        PreOrder(root.right)
def PostOrder(root):
       if root!=None:
         PostOrder(root.left)
         PostOrder(root.right)
         print(root.key)
def printLeafNode(root):
    if root==None:
        return 0
    elif root.left:
        printLeafNode(root.left)
    elif root.right:
        printLeafNode(root.right)
    else:
        if root.left == root.right:
            print(root.key)
def printNonLeafNode(root):
    if root:
       if root.left or root.right:
          print(root.key)
       printNonLeafNode(root.left)
       printNonLeafNode(root.right)
    


root=None
root=insert(root,45)
insert(root,30)
insert(root,23)
insert(root,67)
insert(root,50)
insert(root,89)
Inorder(root)
print("Leaf Node:")
printLeafNode(root)
print("Non leaf Nodes:")
printNonLeafNode(root)