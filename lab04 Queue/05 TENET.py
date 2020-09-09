'''
เกม Color Crush คืออะไร : Color Crush จะเป็นเกมที่นำสีมาเรียงต่อกัน โดยสีจะหายไปก็ต่อเมื่อมีการเรียงสีเหมือนกันครบ 3 อัน 
เช่น  ABBBA  -> AA  เนื่องจาก B เรียงติดกัน 3 ตัวทำให้ระเบิดหายไปโดยที่สีจะมีทั้งหมด 26 สี และจะถูกแทนด้วย A - Z  
ถ้าหากมีการเรียงกันแบบ  ABBBAA -> Empty  เนื่องจาก  ถ้าหาก B ระเบิด  A(BBB)AA -> AAA จะเห็นว่า A ก็เรียงกันอีก 3 ตัว
ทำให้เกิดการระเบิดขึ้นอีกครั้งหนึ่ง  และถ้าหากมีการเรียงกันแบบ AAAA -> A เนื่องจากมีการเรียงกัน 3 ตัว  (AAA)A ทำให้เหลือ A 1 ตัว

เนื้อเรื่อง :  หลังจากที่กฤษฎาได้เล่นเกม Color Crush ก็ได้ไปเห็นโฆษณาว่า บริษัทที่ได้สร้าง Color Crush มีแผนการที่จะสร้างเกม 
Color Crush 2 ขึ้นมา กฤษฎาจึงได้สมัครเข้าไปร่วมทีมในการสร้างเกม Color Crush 2 ซึ่งเกมนี้จะมีกิมมิคที่แตกต่างออกไป คือการที่จะมี 2 ฝั่ง 
คือ ฝั่งปกติกับฝั่งโลกกระจก โดยฝั่งโลกกระจกจะเกิดการระเบิดก่อน ซึ่งการระเบิดของฝั่งโลกกระจกจะไม่ใช่ระเบิดแล้วหายไปเลย 
แต่จะเป็นระเบิดแล้วกลายเป็น ITEM ไว้สำหรับขัดขวางการระเบิดของฝั่งปกติ  หลังจากที่ฝั่งโลกกระจกเกิดการระเบิดครบแล้ว ก็จะเป็นคิวของฝั่งปกติ  
ซึ่งถ้าหากฝั่งปกติมีการเรียงกันของสีที่จะทำให้เกิดการระเบิด ในเสี้ยววินาทีนั้นก่อนที่จะเกิดการระเบิดของฝั่งปกติ  ITEM 
สำหรับขัดขวางการระเบิดของฝั่งโลกกระจก จะมาคั่นระหว่างระเบิดลูกที่ 2 กับ ลูกที่ 3 (อาจจะทำให้เกิดการระเบิดเหมือนเดิมได้ถ้าหาก 
ระเบิดนั้นเป็นสีเดียวกัน  แต่ถ้าเป็นคนละสีก็จะทำให้ไม่เกิดการระเบิดขึ้น)  โดยระเบิดอาจจะเกิดการระเบิดซ้อนๆกันเรื่อยๆได้จะเป็น Empty  
เช่น ถ้าหากฝั่งปกติมีระเบิดเรียงแบบนี้ AAAAA และฝั่งโลกกระจกมีระเบิดแบบนี้ AAA ถ้าหากฝั่งปกติระเบิดธรรมดา 1 ทีจะเหลือแค่ AA 
แต่ถ้าหากฝั่งโลกกระจกมาขัดขวาง จะกลายเป็น AA(A)AAAA ก็จะเกิดระเบิด 2 ทีทำให้ระเบิดฝั่งปกติเป็น Empty
'''

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
