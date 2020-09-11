'''
สร้าง method insert ในคลาส LinkedList เพื่อแทรกข้อมูลลงใน index ที่กำหนดของ linked list และ return ผลลัพธ์ตามตัวอย่าง 
โดยคลาส LinkedList จะประกอบไปด้วย

1. def __init__(self): สำหรับสร้าง linked list
2. def __str__(self): return string แสดง ค่าใน linked list
3. def isEmpty(self): return list นั้นว่างหรือไม่
4. def append(self, data): เพิ่ม data ต่อท้าย linked list
5. def insert(self, index, data): insert data ใน index ที่กำหนด

โดยการแทรกในที่นี้ จะเป็นการนำข้อมูลใหม่ที่ต้องการมาใส่แทนที่ตำแหน่งของข้อมูลเดิมและย้ายข้อมูลเดิมไปต่อหลังข้อมูลใหม่ 
'''
class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    def __str__(self):
        if self.isEmpty(): return "List is empty"
        return "link list : "+"->".join(str(i) for i in self.display())

    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
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
            #print ("Data cannot be added")
            return None
        elif index == 0:
            self.appendHead(data)
            return self.display()
        elif index == self.lenght():
            self.append(data)
            return self.display()
        cur_idx=1
        cur_node=self.head
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
        self.head = new_head

    def lenght(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

def main():
    Input = input('Enter Input : ').split(',')
    Linked_list = linked_list()

    for i in Input:
        i = i.strip().split()
        if i == []:
            print(linked_list())
        elif len(i) > 1 and len(i[0]) == 1:
            for data in i:
                Linked_list.append(int(data))
            print(Linked_list)
        elif len(i[0]) > 1:
            ins = i[0].split(':')
            if  Linked_list.insert(int(ins[0]),int(ins[1])) != None:
                print('index = {} and data = {}'.format(int(ins[0]),int(ins[1])))
                print(Linked_list)
            else:
                print ("Data cannot be added")
                print(Linked_list)
            
if __name__=='__main__':
    main()