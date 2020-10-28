#ให้น้องรับ input เป็น list กับ k และจากนั้นให้สร้าง Binary Search Tree จาก list ที่รับเข้ามา และหาว่าใน Binary Search Tree นั้นมีกี่ Node ที่มีค่าน้อยกว่าหรือเท่ากับ k

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

    def lessThanOrEqual(self,node,num):
        if node == None: return 0
        n = self.lessThanOrEqual(node.left,num)
        if node.data > num: return n
        n += self.lessThanOrEqual(node.right,num)
        if node.data <= num: n += 1
        return n
        



T = BST()
n = input('Enter Input : ').split('/')
num = int(n[1])
inp = [int(i) for i in n[0].split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print('--------------------------------------------------')
print(T.lessThanOrEqual(root,num))