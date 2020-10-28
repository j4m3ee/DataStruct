#ให้น้องๆรับ input เป็น postfix จากนั้นให้แปลงเป็น Expression Tree , Infix และ Prefix  โดย Operator จะมีแค่ + - * /

class Node:
    def __init__(self, data,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.data)

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def push(self,data):
        self.items.append(data)

    def pop(self):
        return self.items.pop() if not self.isEmpty() else None

    def peek(self):
        return self.items[-1]

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
            return self.root
        node = self.root
        while True:
            if node.data <= data:
                if node.right == None:
                    node.right = Node(data)
                    return self.root
                node = node.right
            else:
                if node.left == None:
                    node.left = Node(data)
                    return self.root
                node = node.left
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def inOrder(self,root):
        if root != None:
            if root.left is not None or root.right is not None: print('(',end='')
            self.inOrder(root.left)
            print(root.data,end = '')
            self.inOrder(root.right)
            if root.left is not None or root.right is not None: print(')',end='')
        
    def postOrder(self,root):
        if root != None:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.data,end = '')

    def preOrder(self,root):
        if root != None:
            print(root.data,end = '')
            self.preOrder(root.left)
            self.preOrder(root.right) 

inp = list(input('Enter Postfix : '))
expT = BST()
s = Stack()
for c in inp:
    if c in '+-*/':
        c1 = s.pop()
        c2 = s.pop()
        s.push(Node(c,c2,c1))
    else:
        s.push(Node(c)) 

print('Tree :')
expT_root = s.pop()
expT.printTree(expT_root)
print('--------------------------------------------------')
print('Infix :',end = ' ')
expT.inOrder(expT_root)
print()
print('Prefix :',end = ' ')
expT.preOrder(expT_root)
print()

