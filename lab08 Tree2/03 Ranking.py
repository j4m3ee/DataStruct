# จงเขียนฟังก์ชั่นในการหา Rank ของ input ที่รับเข้ามา โดย Rank คือการแบ่งเป็นชั้นๆตามข้อมูลของ BST 
# โดยจะเริ่มจากค่าที่น้อยกว่าค่าใน BST ที่น้อยที่สุดจะมีค่า Rank = 0 และค่าที่อยู่ตั้งแต่ค่าที่น้อยที่สุดจน
# ถึงตัวถัดไปจะมีค่า Rank +=1 ไปเรื่อยๆจนถึงชั้นของตัวสุดท้ายหรือตัวมากสุด


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

    def rank(self,n):
        a = 0
        for i in self.inOrder(self.root):
            if n < i: return a
            a += 1
        return a


    
    def inOrder(self,root):
        return (self.inOrder(root.left) + [root.data] + self.inOrder(root.right)) if root else []


            
if __name__ == "__main__":
    Data = input('Enter Input : ').split('/')
    cV = int(Data[1])
    t = BST()
    inp = [int(i) for i in Data[0].split()]
    for data in inp:
        root = t.insert(data)
    t.printTree(root)
    print('--------------------------------------------------')
    print('Rank of {} : {}'.format(cV,t.rank(cV)))