#จงเขียนฟังก์ชั่นสำหรับการ insert แบบ Binary Search Tree (BST) โดยที่ input ตัวแรกจะเป็น root เสมอและจงเขียนฟังก์ชั่นสำหรับการหาค่าที่ใกล้เคียง input ที่รับเข้ามาที่สุดที่อยู่ใน BST ที่ทำการ insert ครบแล้ว
# รูปแบบการรับ input จะแบ่งโดย '/'
# 1.ชุดของ BST ที่จะทำการ insert โดยตัวแรกจะเป็น root เสมอ
# 2.ค่าที่จะนำมาเปรียบเทียบกับค่าใน BST ที่ทำการ insert แล้ว

# รูปแบบ output 
# จะ printTree ทุกครั้งที่มีการ insert ค่าเข้าและเมื่อทำการ insert จบจะเรียกใช้ฟังก์ชั่น closestValue(root,value) และแสดงค่าที่ใกล้เคียงที่สุดจาก BST 
# *** ถ้าหากค่าที่รับเข้ามาเทียบมีอยู่ใน BST ให้ return ค่านั้นออกมาได้เลย และหากมีค่าที่อยู่ใกล้มากกว่า 1 จำนวนให้แสดงจำนวนที่มากที่สุดที่อยู่ใกล้ค่านั้น ***


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

def closestValue(node,n):
    a = node.data
    son = node.left if n < a else node.right
    if son == None:
        return a
    b = closestValue(son,n)
    return min((a,b), key=lambda x: abs(n-x))
            
if __name__ == "__main__":
    Data = input('Enter Input : ').split('/')
    cV = int(Data[1])
    t = BST()
    inp = [int(i) for i in Data[0].split()]
    for data in inp:
        root = t.insert(data)
        t.printTree(root)
        print('--------------------------------------------------')
    print('Closest value of {} : {}'.format(cV,closestValue(t.root,cV)))