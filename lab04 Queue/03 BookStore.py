'''
กฤษฎาได้มาทำงานพิเศษในช่วงปิดเทอมที่ร้านหนังสือการ์ตูนแห่งหนึ่ง  โดยเจ้าของร้านได้สั่งให้กฤษฎามาจัดหนังสือการ์ตูน Attack On Titan 
เพื่อที่จะวางขายในวันรุ่งขึ้น  โดยกฤษฎาได้จัดหนังสือไปเรื่อยๆจนรู้สึกเบื่อหน่าย  จึงได้คิดเกมสนุกๆขึ้นมานั่นคือ  ในชั้นหนังสือจะมีแค่ด้านหน้า
กับด้านหลังที่จะใส่หนังสือเข้าไปได้เรื่อยๆ และจะนำหนังสือออกได้แค่ด้านหน้า และใส่หนังสือเพิ่มได้แค่ด้านหลัง  โดยเมื่อเล่นเกมนี้ไปเรื่อยๆ 
กฤษฎาก็ลืมว่าในชั้นหนังสือนั้นมีหนังสือซ้ำกันหรือไม่  กฤษฎาเลยอยากให้คุณเขียนโปรแกรม Python เพื่อมาช่วยกฤษฎาคิดว่ามีหนังสือซ้ำกันในชั้นนั้นหรือไม่

Input :
จะแบ่งเป็น 2 ฝั่งแบ่งด้วย /   คือ ซ้าย : เป็นหนังสือที่มีอยู่ในชั้นอยู่แล้ว  ขวา : จะแบ่งเป็น 2 ส่วน คือ D กับ E
D           -> เป้นการนำหนังสือด้านหน้าออกจากชั้น
E <value>   -> เป็นการนำหนังสือ Attack On Titan เล่มที่ value เข้าชั้นหนังสือจากด้านหลัง
'''

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
    def chkDuplicate(self):
        if len(self.list) == len(set(self.list)):
            return 'NO Duplicate'
        else:
            return 'Duplicate'
        
lsInput = input('Enter Input : ').split('/')
lsData = lsInput[0].split()
lsWork = lsInput[1].split(',')
q = Queue(lsData)
for i in lsWork:
    i = i.split()
    if i[0] == 'E':
        q.enQueue(i[1])
    elif i[0] == 'D':
        q.deQueue()
print(q.chkDuplicate())
        
