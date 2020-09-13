'''
กฤษฎาได้มีไอเดียสุดบรรเจิดคือการสร้างโปรแกรม Text Editor แบบ VIM ขึ้นมาใช้งานเอง โดยโปรแกรมนี้จะมีอยู่แค่ 1 Mode 
คือ Command Mode (inputของเรานั่นแหละ) โดยจะมีคำสั่งอยู่ 5 แบบ คือ Insert (I) , Left (L) , Right (R) , Backspace (B) 
และ Delete (D) (โดยความสามารถของคำสั่งต่างๆจะอธิบายด้านล่าง) แต่กฤษฎาไม่มีความสามารถทางด้านการสร้างโปรแกรมเลย 
กฤษฎาจึงได้มาขอร้องน้องๆที่เรียนอยู่วิศวกรรมคอมพิวเตอร์ ให้ช่วยสร้างโปรแกรม Text Editor ที่กฤษฎาต้องการให้หน่อย 
โดยผลลัพธ์ให้แสดงออกมาเป็น word ที่เหลืออยู่จาก Command ที่เราใส่ลงไป พร้อมกับตำแหน่งของ Cursor

***** อธิบาย Input 5 แบบ *****
1.  I <word > :   เป็นการนำ word ลงไปใส่ในตำแหน่งของ Cursor ปัจจุบัน หลังจากใส่ word เสร็จ ตำแหน่งของ Cursor จะมาอยู่ด้านหลังของ word ที่ใส่ลงไป
2.  L         :   เป็นการเลื่อน Cursor จากตำแหน่งปัจจุบันไปทางด้านซ้าย 1 ตำแหน่ง หากอยู่ทางซ้ายสุดอยู่แล้วจะไม่เกิดผลอะไร
3.  R         :   เป็นการเลื่อน Cursor จากตำแหน่งปัจจุบันไปทางด้านขวา 1 ตำแหน่ง หากอยู่ทางขวาสุดอยู่แล้วจะไม่เกิดผลอะไร
4.  B         :   เป็นการลบ word 1 ตัวทางด้านซ้ายของ Cursor หากอยู่ทางซ้ายสุดอยู่แล้วจะไม่เกิดผลอะไร
5.  D         :   เป็นการลบ word 1 ตัวทางด้านขวาของ Cursor หากอยู่ทางขวาสุดอยู่แล้วจะไม่เกิดผลอะไร
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
        return " ".join(str(i) for i in self.display())

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

    def find(self,data):
        cur = self.head
        inx = 0
        while cur.next != None:
            cur = cur.next
            if cur.data == data:
                return inx
            inx += 1

    def shiftLeft(self):
        inx = self.find('|')
        if inx != 0 :
            self.erase(inx) 
            self.insert(inx - 1,'|')

    def shiftRight(self):
        inx = self.find('|')
        if inx != self.lenght()-1 :
            self.erase(inx) 
            self.insert(inx + 1,'|')

def main():
    Input = input('Enter Input : ').split(',')
    Linked_list = LinkedList()
    Linked_list.append('|')

    for i in Input:
        i = i.strip().split()
        if i[0] == 'I':
            Linked_list.insert(Linked_list.find('|'),i[1])
        elif i[0] == 'L':
            Linked_list.shiftLeft()
        elif i[0] == 'R':
            Linked_list.shiftRight()
        elif i[0] == 'B':
            inx = Linked_list.find('|')
            if inx != 0 : Linked_list.erase(inx-1)
        elif i[0] == 'D':
            inx = Linked_list.find('|')
            if inx != Linked_list.lenght()-1 : Linked_list.erase(inx+1)
    print(Linked_list)
            
if __name__=='__main__':
    main()