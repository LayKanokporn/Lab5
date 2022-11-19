#Lab 5 Exercise.2.3 1630902656 Kanokporn Hudsree
class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None 
  
def inorder(root):
    if root is not None:
        inorder(root.left)
        print ("Node: ",root.key,"is child" ,end=" ")
        if root.parent == None:
            print("Parent : NULL")
        else:
            print("Parent  is : ", root.parent.key)
        inorder(root.right)
        
def insert(node, key):
  
    if node is None:
        return Node(key)
  
    if key < node.key:
        lchild = insert(node.left, key)
        node.left = lchild

        lchild.parent = node
    elif key > node.key:
        rchild = insert(node.right, key)
        node.right = rchild

        rchild.parent = node

    return node
  
def minValueNode(node):
    current = node
  
    while(current.left is not None):
        current = current.left
    return current
  
def deleteNode(root, key):
  
    # Base Case
    if root is None:
        return root
  
    if key < root.key:
        root.left = deleteNode(root.left, key)
  
    elif key > root.key:
        root.right = deleteNode(root.right, key)
  
    else:
  

        if root.left is None:
            temp = root.right
            root = None
            return temp
  
        elif root.right is None:
            temp = root.left
            root = None
            return temp
  
        temp = minValueNode(root.right)
  
        root.key = temp.key
  

        root.right = deleteNode(root.right, temp.key)
  
    return root
def maxDepth(node):
    if node is None:
        return 0
 
    else:
        # Compute the depth of each subtree
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)
 
        # Use the larger one
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1

def printLeafNodes(root: Node) -> None:
 

    # If node is null, return
    if (not root):
        return
 
    # If node is leaf node,
    # print its data
    if (not root.left and
        not root.right):
        print("leaf",root.key,
              end = " ")
        return

    if root.left:
        printLeafNodes(root.left)
 

    if root.right:
        printLeafNodes(root.right)
def CheckIfNodesAreSiblings(root, data_one,
                                  data_two):
    if (root == None):
        return False

    ans = False
     
    if (root.left != None and root.right != None):
        left = root.left.key
        right = root.right.key
         
        if (left == data_one and right == data_two):
            return True
        elif (left == data_two and right == data_one):
            return True
 
    # Check for left subtree
    if (root.left != None):
        ans = ans or CheckIfNodesAreSiblings(root.left,
                                       data_one,
                                       data_two)
                                        
    # Check for right subtree
    if (root.right != None):
        ans = ans or CheckIfNodesAreSiblings(root.right,
                                       data_one,
                                       data_two)
    return ans   

# Use the insert method to add nodes
root = Node(50)
root = insert(root,25)
root = insert(root,75)
root = insert(root,30)
root = insert(root,60)
root = insert(root,40)


inorder(root)
print("Height of tree is:",(maxDepth(root)))
printLeafNodes(root)

data_one = 60
data_two = 40

if (CheckIfNodesAreSiblings(root,data_one,data_two)):
    print("\n YES")
else:
    print("\n NO")
    
    

