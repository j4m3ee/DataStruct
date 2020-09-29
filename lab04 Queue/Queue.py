class Queue:
    def __init__(self,list = None):
        self.list = list if list != None else []
    def __str__(self):
        return ''.join(str(i) for i in self.list)
    def isEmpty(self):
        return self.list == []
    def enQueue(self,item):
        self.list.append(item)
    def deQueue(self):
        return self.list.pop(0) if not self.isEmpty() else 'Empty'
    def pop(self):
        return self.list.pop() if not self.isEmpty() else 'Empty'
    def Size(self):
        return len(self.list)
    def insert(self,index,item):
        self.list.insert(index,item)
    def peek(self):
        return self.list[-1]