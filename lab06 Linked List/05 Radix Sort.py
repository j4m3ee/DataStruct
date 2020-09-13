'''
ให้น้องๆใช้ Linked List (เขียนเป็น class)  ในการทำ Radix Sort  (มีอยู่ในสไลด์เรียน 2 หน้าสุดท้าย)  ในรูปแบบน้อยไปมาก

โดยผลลัพธ์ให้ออกมาเป็นการทำ Radix Sort แบบจำนวนรอบน้อยที่สุด และแสดงผลในแต่ละรอบว่าได้ผลลัพธ์เป็นอย่างไร  
3 บรรทัดสุดท้ายจะเป็น ( จำนวนรอบที่น้อยที่สุด , Data ก่อนทำ Radix Sort และ Data หลังทำ Radix Sort )
'''
class node():
    def __init__(self,data = None):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList():
    def __init__(self):
        self.head = node()

    def __str__(self):
        return " -> ".join(str(i) for i in self.display())

    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        new_node.prev = cur
        cur.next = new_node

    def isEmpty(self):
        return self.head.next == None

    def display(self):
        elems = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elems.append(cur.data)
        return elems
    
    def insert(self,index,data):
        if index > self.lenght() or index < 0:
            return None
        elif index == 0:
            self.appendHead(data)
            return self.display()
        elif index == self.lenght():
            self.append(data)
            return self.display()
        cur_idx = 1
        cur_node = self.head
        new_node = node(data)
        while True:
            cur_node = cur_node.next
            if cur_idx == index : 
                new_node.next = cur_node.next
                cur_node.next = new_node
                return new_node.data
            cur_idx += 1
    
    def appendHead(self,data):
        new_node = node(data)
        new_node.next = self.head.next
        new_head = node()
        new_head.next = new_node
        new_node.prev = new_head
        self.head = new_head

    def lenght(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def erase(self,index):
        if index >= self.lenght():
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx +=1 
    
    def isSort(self):
        val = True
        cur = self.head
        while cur.next != None:
            last_node = cur
            cur = cur.next
            if last_node.data > cur.data: val =  False
        return val

def getDigit(pos,data):
    tool = pow(10,pos-1)
    num = int(data/tool)
    return num%10

def main():
    Input = input('Enter Input : ').split()
    List = LinkedList()
    
    print('------------------------------------------------------------')
    print('Round : ')

    print('0',':')
        
    print('------------------------------------------------------------')
    
    print('0',' Time(s)')
    print('Before Radix Sort :',' -> '.join(Input))
    print('After  Radix Sort :',List)
    print(max(Input))
    

if __name__=='__main__':
    main()