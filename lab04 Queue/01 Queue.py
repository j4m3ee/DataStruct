class Queue:
    def __init__(self,list = None):
        self.list = list if list != None else []
    def __str__(self):
        return String(self.list) if not self.isEmpty() else 'Empty'
    def isEmpty(self):
        return self.list == []
    def enQueue(self,item):
        self.list.append(item)
    def deQueue(self):
        return self.list.pop(0) if not self.isEmpty() else 'Empty'
    def Size(self):
        return len(self.list)

def String(ls):
    return ', '.join(str(data) for data in ls) 
    
ls = input('Enter Input : ').split(',')
q = Queue()
dq = Queue()
for i in ls:
    i = i.split()
    if i[0] == 'D':
        deQ = q.deQueue()
        if deQ != 'Empty':
            dq.enQueue(deQ)
            print(deQ,'<- ',end = '')
    else:
        q.enQueue(int(i[1]))
    print(q)
print(dq,':',q)
