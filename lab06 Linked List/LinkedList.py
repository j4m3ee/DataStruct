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

    def isEmpty(self):
        return self.head.next == None

    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

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
    
    def display(self):
        elems = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elems.append(cur.data)
        return elems

    def get(self,index):
        if index >= self.lenght():
            print ("ERROR: 'get' index out of range!")
            return None
        cur_idx=0
        cur_node=self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index : return cur_node.data
            cur_idx += 1

    def erase(self,index):
        if index >= self.lenght():
            print ("ERROR: 'erase' index out of range!")
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

    def peek(self):
        cur = self.head
        while cur.next != None:
            cur = cur.next
        return cur.data

    def pop(self):
        cur = self.head
        while True:
            last_node = cur
            cur = cur.next
            if cur.next == None:
                last_node.next = None
                return cur.data

    def popHead(self):
        newHead = node()
        popItem = self.head.next.data
        newHead.next = self.head.next.next
        self.head = newHead
        return popItem

    def remove(self,data):
        cur = self.head
        while cur.next != None:
            last_node = cur
            cur = cur.next
            if cur.data == data:
                last_node.next = cur.next if cur.next != None else None
                return cur

test = linked_list()
test.append(23)
test.append(13)
test.append(34)
test.append(3)
print(test)
test.remove(3)
print(test)



        
                
