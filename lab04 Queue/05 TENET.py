class Queue:
    def __init__(self,list = None):
        self.list = list if list != None else []
    def __str__(self):
        return ''.join(str(i) for i in self.list)
    def isEmpty(self):
        return self.list == []
    def enQueue(self,item):
        self.list.append(item)
    def deQueue(self):
        return self.list.pop(0) if not self.isEmpty() else 'Empty'
    def pop(self):
        return self.list.pop() if not self.isEmpty() else 'Empty'
    def Size(self):
        return len(self.list)
    def insert(self,index,item):
        self.list.insert(index,item)
    def peek(self):
        return self.list[-1],self.list[-2]


def main():
    red,blue = input('Enter Input (Red, Blue) : ').split()
    red = list(red)
    blue = list(blue)

    #team Blue
    bq,rbomb,freeze = Queue(),[],0
    for data in list(reversed(blue)):
        rbomb.append(data)
        if len(rbomb) > 2:
            if rbomb[-1] == rbomb[-2] == rbomb[-3]:
                bq.enQueue(data)
                freeze += 1
                for _ in range(3):
                    rbomb.pop()
    #team Red
    rq,heat,miss = Queue(),0,0
    for data in red:
        r = 0
        while True:
            r += 1
            if rq.Size() < 2:
                rq.enQueue(data) if r == 1 else ''
                break
            else:
                p1,p2 = rq.peek()
                if data == p1 == p2:
                    if not bq.isEmpty():
                        block = bq.deQueue()
                        if block == data:
                            rq.pop()
                            rq.pop()
                            rq.enQueue(data) if r == 1 else ''
                            miss += 1
                        else:
                            rq.enQueue(block)
                            rq.enQueue(data) if r == 1 else ''
                    else:
                        heat += 1
                        rq.pop()
                        rq.pop()
                else:
                    rq.enQueue(data) if r == 1 else ''
                    break

    output(rq,rbomb,heat,freeze,miss)

def output(red,blue,heat,freeze,miss):
    print('Red Team :')
    print(red.Size())
    print(''.join(str(data) for data in reversed(red.list)) if not red.isEmpty() else 'Empty')
    print('{} Explosive(s) ! ! ! (HEAT)'.format(heat))
    if miss != 0:
        print('Blue Team Made (a) Mistake(s) {} Bomb(s)'.format(miss))
    print('----------TENETTENET----------')
    print(': maeT eulB')
    print(len(blue))
    print(''.join(str(data) for data in reversed(blue)) if len(blue) != 0 else 'ytpmE')
    print('(EZEERF) ! ! ! (s)evisolpxE',freeze)


if __name__ == "__main__":
    main()
