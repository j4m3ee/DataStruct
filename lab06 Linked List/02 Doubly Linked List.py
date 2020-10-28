'''
ให้เขียนคลาสของ Doubly Linked List ซึ่งมีเมท็อดดังนี้

1. def __init__(self): สำหรับสร้าง linked list
2. def __str__(self): return string แสดง ค่าใน linked list
3. def str_reverse(self): return string แสดง ค่าใน linked list จากหลังมาหน้า
4. def isEmpty(self): return list นั้นว่างหรือไม่
5. def append(self, data): add node ที่มี data เป็น parameter ข้างท้าย linked list
6. def insert(self, index, data): insert data ใน index ที่กำหนด
7. def remove(self, data): remove & return node ที่มี data

 - การแทรกในที่นี้ จะเป็นการนำข้อมูลใหม่ที่ต้องการมาใส่แทนที่ตำแหน่งของข้อมูลเดิมและย้ายข้อมูลเดิมไปต่อหลังข้อมูลใหม่ 

คำแนะนำเพิ่มเติม เพื่อความง่ายในการเขียนโค้ดและไม่ต้องเขียนspecial caseเยอะๆ ให้ลองใช้ Dummy Node ดูนะครับ(หากสงสัยการใช้งาน Dummy Node สอบถามพี่ๆTA หรือ https://youtu.be/XgUIjTQ1HjA )

โดยรูปแบบ Input มีดังนี้
1. append     ->  A
2. add_before -> Ab
3. insert     ->   I
4. remove     ->  R
'''

class node():
    def __init__(self,data = None):
        self.data = data
        self.next = None
        self.prev = None

class doublyLinkedList():
    def __init__(self):
        self.head = node()

    def __str__(self):
        if self.isEmpty(): return "linked list : "
        return "linked list : "+"->".join(str(i) for i in self.display())

    def reverse(self):
        if self.isEmpty(): return "reverse : "
        return "reverse : "+"->".join(str(i) for i in reversed(self.display()))

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
    
    def remove(self,data):
        cur = self.head
        inx = 0
        while cur.next != None:
            last_node = cur
            cur = cur.next
            if cur.data == data:
                last_node.next = cur.next if cur.next != None else None
                return inx
            inx += 1

def main():
    Input = input('Enter Input : ').split(',')
    Linked_list = doublyLinkedList()

    for i in Input:
        i = i.strip().split()
        if i[0] == 'Ab':
            Linked_list.appendHead(int(i[1]))
        elif i[0] == 'A':
            Linked_list.append(int(i[1]))
        elif i[0] == 'I':
            ins = i[1].split(':')
            if  Linked_list.insert(int(ins[0]),int(ins[1])) != None:
                print('index = {} and data = {}'.format(int(ins[0]),int(ins[1])))
            else:
                print ("Data cannot be added")            
        elif i[0] == 'R':
            data = Linked_list.remove(int(i[1]))
            print('removed : {} from index : {}'.format(i[1],data) if data != None else 'Not Found!')
        print(Linked_list)
        print(Linked_list.reverse())
            
if __name__=='__main__':
    main()