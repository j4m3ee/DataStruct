'''
ให้น้องรับ Linked List มา 2 ตัว จากนั้นนำ 2 Linked List มาต่อกัน โดย L2 จะมาต่อ L1 แบบกลับหลัง
'''
class node():
    def __init__(self,data = None):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = node()

    def __str__(self):
        return " ".join(str(i) for i in self.display())

    def reverse(self):
        return " ".join(str(i) for i in reversed(self.display()))

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

def makeLinkedList(List):
    Linked_list = LinkedList()
    for data in List:
        Linked_list.append(data)
    return Linked_list

def main():
    Input = input('Enter Input (L1,L2) : ').split()
    
    list01 = Input[0].split('->')
    list02 = Input[1].split('->')
    Linked_list_01 = makeLinkedList(list01)
    Linked_list_02 = makeLinkedList(list02)
    print('L1    :',Linked_list_01)
    print('L2    :',Linked_list_02)
    print('Merge :',Linked_list_01,Linked_list_02.reverse())
    
if __name__=='__main__':
    main()