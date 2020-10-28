#ให้น้องรับ input เข้ามาและสร้าง Binary Search Tree ต่อมาให้แสดงผลแบบ Preorder , Inorder , Postorder และ Breadth First Search ตามลำดับ

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class Stack:
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item == []

    def size(self):
        return len(self.item)

    def push(self,data):
        self.item.append(data)

    def pop(self):
        return self.item.pop() if not self.isEmpty() else None

class Queue:
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item == []

    def size(self):
        return len(self.item)

    def enQ(self,data):
        self.item.append(data)

    def deQ(self):
        return self.item.pop(0) if not self.isEmpty() else None


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

    def breadthFirst(self):
        ls = []
        q = Queue()
        q.enQ(self.root)
        while not q.isEmpty():
            n = q.deQ()
            ls.append(n.data)
            if n.left is not None:
                q.enQ(n.left)
            if n.right is not None:
                q.enQ(n.right)
        return ls

    def inOrder(self,root):
        return (self.inOrder(root.left) + [root.data] + self.inOrder(root.right)) if root else []
        
    def postOrder(self,root):
        return (self.postOrder(root.left) + self.postOrder(root.right) + [root.data] ) if root else []

    def preOrder(self,root):
        return ([root.data] + self.preOrder(root.left) + self.preOrder(root.right)) if root else []


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
print('Preorder :',' '.join(str(i) for i in T.preOrder(root)))
print('Inorder :',' '.join(str(i) for i in T.inOrder(root)))
print('Postorder :',' '.join(str(i) for i in T.postOrder(root)))
print('Breadth :',' '.join(str(i) for i in T.breadthFirst()))

