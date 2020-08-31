def match(op,cl):
    lsop = '([{'
    lscl = ')]}'
    return lsop.index(op) == lscl.index(cl)

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



text = str(input('Enter Input : '))
ls = list(text)
s = Stack()
error = 0

for i in text:
    if i in '([{':
        s.push(i)
    else:
        if i in ')]}':
            if s.size() > 0:
                if not match(s.pop(),i):
                    error = 1
            else:
                error = 2

if s.size() > 0:
    error = 3

print('Parentheses : Matched ! ! !') if error == 0  else print('Parentheses : Unmatched ! ! !')