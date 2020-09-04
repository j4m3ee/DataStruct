class Queue:
    def __init__(self,list = None):
        self.list = list if list != None else []
    def isEmpty(self):
        return self.list == []
    def enQueue(self,item):
        index = -1
        for i in self.list:
            if i[0] == item[0]:
                pass
        self.list.append(item)
    def deQueue(self):
        return self.list.pop(0) if not self.isEmpty() else 'Empty'
    def Size(self):
        return len(self.list)
    def insert(self,index,item):
        self.list.insert(index,item)
        
lsInput = input('Enter Input : ').split('/')
lsData = lsInput[0].split(',')
lsWork = lsInput[1].split(',')
q = Queue()
for i in lsWork:
    i = i.split()
    if i[0] == 'E':
        q.enQueue(i[1])
    elif i[0] == 'D':
        print(q.deQueue())
