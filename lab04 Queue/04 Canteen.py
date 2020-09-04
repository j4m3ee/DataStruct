class Queue:
    def __init__(self,list = None):
        self.list = list if list != None else []
    def isEmpty(self):
        return self.list == []
    def enQueue(self,item):
        for i in self.list[-1::-1]:
            if i[0] == item[0]:
                if self.list.index(i) == self.Size() -1:
                    break
                self.insert(self.list.index(i)+1,item)
                return
        self.list.append(item)
    def deQueue(self):
        return self.list.pop(0) if not self.isEmpty() else 'Empty'
    def Size(self):
        return len(self.list)
    def insert(self,index,item):
        self.list.insert(index,item)
        
lsInput = input('Enter Input : ').split('/')

Dict = dict()
for i in lsInput[0].split(','):
    i = i.split()
    Dict[i[1]] = Dict.get(i[1],i[0])

q = Queue()
for i in lsInput[1].split(','):
    i = i.split()
    if len(i) == 1:
        pop = q.deQueue()
        print(pop if pop == 'Empty' else int(pop[1]))
    else:
        i[0] = Dict[i[1]]
        q.enQueue(i)
        