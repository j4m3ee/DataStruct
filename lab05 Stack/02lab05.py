class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

Input = list(map(str,input('Enter Input : ').split(',')))
ls = []
for i in Input:
    ls.append(list(map(int,i.split())))
s = Stack()

for i in ls:
    if s.isEmpty():
        s.push(i)
    else:
        while True:
            if  s.size() > 0 :
                if i[0] > s.peek()[0]:
                    print(s.pop()[1])
                else:
                    break
            else:
                break
        s.push(i)

