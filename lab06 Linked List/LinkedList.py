class node:
    def __init__(self,data=None,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class linked_list:
    def __init__(self):
        self.head = node()
        self.tail = node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def __str__(self):
        if self.isEmpty(): return "List is empty"
        return "link list : "+"->".join(str(i) for i in self.display())

    def isEmpty(self):
        return self.head.next == self.tail

    def append(self,data):
        new_node = node(data , self.tail , self.tail.prev)
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        return new_node.data

    def appendHead(self,data):
        new_node = node(data , self.head.next , self.head)
        self.head.next.prev = new_node
        self.head.next = new_node
        return new_node.data

    def lenght(self):
        cur = self.head
        total = 0
        while cur.next != self.tail:
            total += 1
            cur = cur.next
        return total
    
    def display(self):
        elems = []
        cur = self.head
        while cur.next != self.tail:
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
        if index >= self.lenght(): return "ERROR: 'erase' index out of range!"
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                cur_node.next.prev = last_node
                return cur_node.data
            cur_idx +=1 

    def peek(self):
        return self.tail.prev.data

    def pop(self):
        cur = self.head
        while True:
            last_node = cur
            cur = cur.next
            if cur.next == self.tail:
                last_node.next = self.tail
                self.tail.prev = last_node
                return cur.data

    def popHead(self):
        cur = self.head
        popItem = cur.next.data
        cur.next = cur.next.next
        return popItem

    def remove(self,data):
        cur = self.head
        while cur.next != None:
            last_node = cur
            cur = cur.next
            if cur.data == data:
                last_node.next = cur.next if cur.next != None else self.tail
                if cur.next != None: cur.next.prev = last_node
                else: self.tail.prev = last_node  
                return cur.data

    def insert(self,index,data):
        if index > self.lenght() or index < 0: return "Data cannot be added"
        cur_idx = 0
        cur_node = self.head
        while True:   
            if cur_idx == index :
                new_node = node(data,cur_node.next,cur_node)
                cur_node.next = new_node
                return new_node.data
            cur_node = cur_node.next
            cur_idx += 1

    def compare(self,other):
        if self.lenght() != other.lenght():
            return False
        else:
            cur_self,cur_other=self.head,other.head
            while cur_self.next != None:
                cur_self,cur_other=cur_self.next,cur_other.next
                if cur_self.data != cur_other.data:
                    return False
            return True

test = linked_list()
test.append(23)
test.append(13)
test.append(56)
test.append(34)
test.append(39)
test.append(3)
print(test)
test.remove(3)
print(test)
print("Size",test.lenght())
print("Pop Head",test.popHead())
print(test)
print("Pop",test.pop())
print(test)
print("Insert",test.insert(1,99))
print(test)
print("Remove",test.remove(99))
print(test)
print("Erase",test.erase(2))
print(test)
print("Peek",test.peek())
print(test)
print("Append head",test.appendHead(69))
print(test)



        
                
