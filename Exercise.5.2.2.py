#Lab 5 Exercise.2.2 1630902656 Kanokporn Hudsree
class newNode:

    # เขียนเป็นคลาส newNode เพื่อเก็บข้อมูลโหนดของ new
    def __init__(self, data):
        self.key = data # data สำหรับเก็บค่าข้อมูลที่กำหนดในช่วงของการสร้างต้นไม้
        self.left = None # left สำหรับเก็บค่าตำแหน่งโหนดทางซ้าย โดยกำหนดค่าเริ่มต้นเป็น None
        self.right = self.parent = None 

def insert(root, key):

    newnode = newNode(key)
    x = root
    y = None

    while (x != None):
        y = x
        if (key < x.key):
            x = x.left 
        else:
            x = x.right 

    if (y == None):
        y = newnode

    elif (key < y.key):
        y.left = newnode
    # น้อยกว่าย้ายไปทางซ้าย

    else:
        y.right = newnode
    # มากกว่าย้ายไปทางขวา

    return y

def Inorder(root):

    if (root == None):
        return
    else:
        Inorder(root.left)
        print(root.key, end=" ")
        Inorder(root.right)
       #การทำงานของแบบ in-order แตกต่างออกไป คือ L >> N >> R 
       
def minValueNode(node):
    current = node
  
    # loop down to find the leftmost leaf
    while(current.left is not None):
        current = current.left
  
    return current
  
# Given a binary search tree and a key, this function
# delete the key and returns the new root       

def deleteNode(root, key):
  
    if root is None:
        return root

    if key < root.key:
        root.left = deleteNode(root.left, key)
  
    elif(key > root.key):
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

# Driver Code
if __name__ == '__main__':

    root = None
    root = insert(root, 50)
    insert(root, 25)
    insert(root, 75)
    insert(root, 30)
    insert(root, 60)
    insert(root, 40)


print ("Inorder traversal of the given tree")
Inorder(root)
  
root = deleteNode(root, 30)
root = deleteNode(root, 75)
root = deleteNode(root, 40)

print ("Inorder traversal of the delete tree")
Inorder(root)



