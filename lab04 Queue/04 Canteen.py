'''
โรงอาหารของบริษัทแห่งหนึ่ง จะมีเจ้าหน้าที่คอยจัดแถวสำหรับการซื้ออาหาร โดยจะมีหลักการคือจะดูจากแผนกของพนักงานแต่ละคนว่าอยู่แผนกไหน 
ถ้าหากในแถวที่ต่ออยู่มีแผนกนั้น จะนำพนักงานคนนั้นแทรกไปด้านหลังของแผนกเดียวกัน ตัวอย่างเช่น
Front | 1 2 2 2 2 3 3 3 | Rear  จาก Queue ถ้าหากมีพนักงานแผนก1เข้ามา Queue จะกลายเป็น Front | 1 1 2 2 2 2 3 3 3 | Rear

Input :
จะแบ่งเป็น 2 ฝั่งแบ่งด้วย /   คือ ซ้าย : เป็นแผนกของพนักงานและIDของพนักงานแต่ละคน  ขวา : จะแบ่งเป็น 2 ส่วน คือ D กับ E
E < id >  ->   เป็นการนำพนักงานเข้า Queue
D  ->  เป็นการนำพนักงานคนหน้าสุดออกจากแถว โดยจะแสดงผลเป็น id ของพนักงานคนนั้น ถ้าหากไม่มีพนักงานในแถวจะทำการแสดงผลเป็น Empty
'''


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

#credit : https://github.com/radsadorn
        