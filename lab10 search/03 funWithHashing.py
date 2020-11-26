'''

ให้น้องเขียน Hashing โดยมีการทำงานดังนี้

1. หา index ของ Table จากผลรวมของ ASCII จากค่า key จากนั้นนำมา mod ด้วยขนาดของ Table
2. หากเกิด Collision ให้ทำการขยับค่า index แบบ Quadratic Probing
3. ถ้าหากเกิด Collision จนถึงค่าที่กำหนดแล้ว ให้ทำการ Discard Data นั้นทิ้งทันที
4. หาก Table นั้นมี Data เต็มแล้วให้แสดงคำว่า This table is full !!!!!! หากเคยแสดงคำนี้ไปแล้วไม่ต้องแสดงอีก (แสดงเพียง 1 ครั้ง)

อธิบาย Input
แบ่ง Data เป็น 2 ชุดด้วย /
    -   ด้านซ้ายหมายถึง ขนาดของ Table และ MaxCollision ตามลำดับ
    -   ด้านขวาหมายถึง Data n ชุด โดย Data แต่ละชุดแบ่งด้วย comma โดยใน Data แต่ละชุดจะแบ่งเป็น key กับ value ตามลำดับ

'''

class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:

    def __init__(self,tb):
        self.tableSize, self.maxCollision = map(int,tb.split())
        self.table = [None] * self.tableSize

    def hashing(self,data):
        data,ascVal = data.split(),0
        for alp in list(data[0]):
            ascVal += ord(alp)
        ascVal %= self.tableSize
        count = 0
        while True:
            index = (ascVal + count ** 2) % self.tableSize
            if count == self.maxCollision:
                print('Max of collisionChain')
                return False
            if self.table[index] is None:
                self.table[index] = Data(data[0],data[1])
                if None not in self.table:
                    return True
                return False
            count += 1
            print("collision number {} at {}".format(count,index))


    def printTable(self):
        for i,data in enumerate(self.table):
            print(f'#{i + 1}\t{data}')
        print('---------------------------')



if __name__ == "__main__":
    print(' ***** Fun with hashing *****')
    inp,data = input('Enter Input : ').split('/')
    table = hash(inp)
    for i in data.split(','):
        chk = table.hashing(i)
        table.printTable()
        while(chk):
            print('This table is full !!!!!!')
            quit()                                                              