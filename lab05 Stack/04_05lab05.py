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

ls = list(map(str,input('Enter Input : ').split(',')))
tree = Stack()
canSee = Stack()

for i in ls:
    i = i.split()
    if i[0] == 'A':
        tree.push(int(i[1]))
    elif i[0] == 'B':
        s = Stack()
        for _ in range(tree.size()):
            s.push(tree.pop())
        for _ in range(s.size()):
            item = s.pop()
            if canSee.isEmpty() or canSee.peek() > item:
                tree.push(item)
                canSee.push(item)
            elif canSee.peek() < item:
                while not canSee.isEmpty() and canSee.peek() < item:
                    canSee.pop()
                tree.push(item)
                canSee.push(item)
        print(canSee.size())
        canSee = Stack()
    elif i[0] == 'S':
        s = Stack()
        for _ in range(tree.size()):
            item = tree.pop()
            s.push(item - 1 if item % 2 == 0 else item + 2)
        for _ in range(s.size()):
            tree.push(s.pop())


 

            