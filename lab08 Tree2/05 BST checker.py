#จงเขียนฟังก์ชัน สำหรับตรวจสอบว่า Tree นี้เป็น binary search tree หรือไม่
#โดยกำหนดให้ 0<=node.data<=100 และฟังก์ชั่นมีparameterมากที่สุด4ตัว

class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class Tree:
    def __init__(self): 
        self.root = None
        self.num = 0

    def insert(self, val):  
        if self.root == None:
            self.root = Node(val)
            self.num += 1
        else:
            h = height(self.root)
            max_node = pow(2,h+1)-1
            current = self.root
            if self.num+1 > max_node:
                while(current.left != None):
                    current = current.left
                current.left = Node(val)
                self.num+=1
            elif self.num+1 == max_node:
                while(current.right != None):
                    current = current.right
                current.right = Node(val)
                self.num+=1
            else:
                if self.num+1 <= max_node-((max_node-(pow(2,h)-1))/2):
                    insert_subtree(current.left,self.num - round(pow(2,h)/2),val)
                else:
                    insert_subtree(current.right,self.num - pow(2,h),val)
                self.num+=1

def insert_subtree(r,num,val):
    if r != None:
        h = height(r)
        max_node = pow(2,h+1)-1
        current = r
        if num+1 > max_node:
            while(current.left != None):
                current = current.left
            current.left = Node(val)
            return
        elif num+1 == max_node:
            while(current.right != None):
                current = current.right
            current.right = Node(val)
            return
        if num+1 <= max_node-((max_node-(pow(2,h)-1))/2):
            insert_subtree(current.left,num - round(pow(2,h)/2),val)
        else:
            insert_subtree(current.right,num - pow(2,h),val)
    else:
        return

def height(root):
    if root == None:
        return -1
    else:
        left = height(root.left)
        right = height(root.right)
        if left>right:
            return left + 1
        else:
            return right + 1              

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

def check_binary_search_tree_(root):
    return isBST(root,0,100)

def isBST(root,min,max):
    print(min,max)
    if root == None: return True
    if root.data < min or root.data > max: return False
    
    return isBST(root.left,min,root.data-1) and isBST(root.right,root.data+1,max)

tree = Tree()
data = input("Enter Input : ").split()
for e in data:
    tree.insert(int(e))
printTree90(tree.root)
print(check_binary_search_tree_(tree.root))