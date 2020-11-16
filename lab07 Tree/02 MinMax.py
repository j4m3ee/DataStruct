'''
ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ และหาค่าที่น้อยและมากที่สุดของ Binary Search Tree
***** ห้ามใช้ Built-in Function เช่น min() , max() , sort() , sorted()
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

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

    def min(self):
        node = self.root
        if node.data == None:
            return node
        while True:
            if node.left == None: return node.data
            node = node.left

    def max(self):
        node = self.root
        if node.data == None:
            return node
        while True:
            if node.right == None: return node.data 
            node = node.right

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print('--------------------------------------------------')
print('Min :',T.min())
print('Max :',T.max())