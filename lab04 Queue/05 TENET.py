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

def main():
    red,blue = input('Enter Input (Red, Blue) : ').split()
    red = list(red)
    blue = list(blue)
    print(red,blue)

if __name__ == "__main__":
    main()
