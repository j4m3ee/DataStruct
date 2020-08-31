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
         return self.items[len(self.items)-1],self.items[len(self.items)-2]

     def size(self):
         return len(self.items)

ls = list(map(str,input('Enter Input : ').split()))
s = Stack()
combo = 0

for i in ls:
    if s.isEmpty():
        s.push(i)
    else:
        while True:
            #print('Loop :',s.items)    
            if  s.size() >= 2:
                p1,p2 = s.peek()
                #print(i,':',p2,p1)
                if i == p1 and i == p2:
                    s.pop()
                    s.pop()
                    combo += 1
                    break
                else:
                    s.push(i)
                    break
            else:
                s.push(i)
                break
print(len(s.items))
ans = reversed(s.items)
print('Empty' if s.size() == 0 else ''.join(ans))
if combo > 1:
    print("Combo : {} ! ! !".format(combo)) 
                
    
