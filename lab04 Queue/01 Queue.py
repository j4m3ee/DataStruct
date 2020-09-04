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
    s = ''
    for i in ls:
        if ls.index(i) != 0 and ls.index(i) != len(ls):
            s += ', '
        s += str(i)
    return s
    
ls = input('Enter Input : ').split(',')
q = Queue()
trash = []
for i in ls:
    i = i.split()
    if i[0] == 'E':
        q.enQueue(i[1])
        print(q)
    elif i[0] == 'D':
        if not q.isEmpty():
            trash.append(q.deQueue())
            print(trash[-1],'<-',q)
        elif q.isEmpty():
            print(q.deQueue())
if len(trash) != 0:
    print(String(trash),':',q)
