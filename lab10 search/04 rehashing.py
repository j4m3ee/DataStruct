'''
ให้น้องๆเขียนการทำ Rehashing ด้วยเงื่อนไขดังนี้
1. Table เต็มถึงระดับที่กำหนด ( Threshold (%) )
2. เมื่อเกิดการ Collision ถึงจำนวนที่กำหนด

หากเกิดการ Rehashing ให้ทำการขยาย Table เป็นค่า prime ถัดไปที่มากกว่าเดิม 2 เท่า เช่น หาก Table ตอนแรกมีขนาด 4 และเกิดการ Rehashing  ตัว Table ใหม่จะมีขนาดเป็น 11 เนื่องจาก 2 เท่าของ 4 คือ 8  และค่า prime ที่มากกว่า 8 และใกล้ 8 มากที่สุดคือ 11

การ Hash หากเกิดการ Collision ให้ใช้ Quadratic Probing ในการแก้ปัญหา Collision

อธิบาย Input
แบ่ง Data เป็น 2 ชุดด้วย /
    -   ด้านซ้ายหมายถึง ขนาดของ Table , MaxCollision และ Threshold (สูงสุด 100 %) ตามลำดับ
    -   ด้านขวาหมายถึง Data n ชุด โดย Data แต่ละชุดแบ่งด้วย spacebar และ Data แต่ละตัวเป็นจำนวนเต็มศูนย์หรือบวกเท่านั้น และไม่มี Data ซ้ำกันเด็ดขาด
'''

class Rehash:
    def __init__(self,data):
        tmp = data.split()
        self.table_size = int(tmp[0])
        self.max_colision = int(tmp[1])
        self.trashold = int(tmp[2])

        self.table = [None] * self.table_size
        self.data = []

        print('Initial Table :')
        self.printTable()

    def hashing(self,data):
        if data not in self.data:
            print('Add : {}'.format(data))
            self.data += [data]

        count = 0
        while count <= self.max_colision:
            index = (data + count ** 2) % self.table_size
            if self.table[index] is None:
                self.table[index] = data
                if((self.table_size - self.table.count(None)) / self.table_size * 100 > self.trashold):
                    print('****** Data over threshold - Rehash !!! ******')
                    self.rehashing()
                return
            count += 1
            print(f"collision number {count} at {index}")
            if count == self.max_colision:
                print('****** Max collision - Rehash !!! ******')
                self.rehashing()
                return

    def rehashing(self):
        tmp = self.table_size * 2
        while True:
            div = 2
            chk = False
            while div < tmp ** 0.5:
                if tmp % div == 0:
                    chk = True
                    break
                div += 1
            if not chk:
                break
            tmp += 1

        self.table = [None] * tmp
        self.table_size = tmp

        for data in self.data:
            self.hashing(data)


    def printTable(self):
        for i,data in enumerate(self.table):
            print(f'#{i + 1}\t{data}')
        print('----------------------------------------')


if __name__ == "__main__":
    print(' ***** Rehashing *****')
    tb, data = input('Enter Input : ').split('/')

    table = Rehash(tb)
    for i in data.split():
        table.hashing(int(i))
        table.printTable()