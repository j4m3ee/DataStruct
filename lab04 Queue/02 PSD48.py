class Queue:
    def __init__(self,list = None):
        self.list = list if list != None else []
    def isEmpty(self):
        return self.list == []
    def enQueue(self,item):
        self.list.append(item)
    def deQueue(self):
        return self.list.pop(0) if not self.isEmpty() else 'Empty'
    def Size(self):
        return len(self.list)
    def insert(self,index,item):
        self.list.insert(index,item)
    
ls = input('Enter Input : ').split(',')
q = Queue()
indexES = 0
for i in ls:
    i = i.split()
    if i[0] == 'EN':
        q.enQueue(i[1])
    elif i[0] == 'ES':
        q.insert(indexES,i[1])
        indexES += 1
    elif i[0] == 'D':
        if indexES != 0:
            indexES -= 1
        print(q.deQueue())
        
