'''
เขียนโปรแกรมแก้ปัญหา หอคอยแห่งฮานอย โดยเราจะมีแทงไม้อยู่3แท่งคือ A B C และรับ input เป็นจำนวนแผ่นไม้ที่วางซ้อนกันให้แสดงลำดับการย้ายแผ่นไม้ทั้งหมดจากแท่ง A 
ไปยัง แท่งC โดยแผ่นไม้ที่มีขนาดเล็กกว่าจะอยู่ข้างบนแผ่นไม้ที่มีขนาดใหม่กว่าเสมอ(ห้ามวางแผ่นเล็กกว่าไว้ข้างล่าง)

****ห้ามใช้คำสั่ง for, while, do while*****

หมายเหตุ ทุกฟังก์ชันต้องมี parameter มากที่สุดไม่เกิน 5 ตัว

คำแนะนำ ให้สร้างฟังก์ชันสำหรับแสดงผล แยกต่างหาก และใช้ list ในการเก็บข้อมูลของแท่งไม้แต่ละแท่ง
และให้ระวังเรื่องการสลับ list ให้ดีๆ

หากมีข้อสงสัยเกี่ยวกับ หอคอยแห่งฮานอย สามารถสอบถาม TA เพิ่มเติม หรือ ลองเล่นได้ที่ https://www.mathsisfun.com/games/towerofhanoi.html

code from : https://github.com/eXitHere
'''
def TowerOfHanoi(round , source, dest, aux):
   if round>0: 
      TowerOfHanoi(round-1, source, aux, dest) 
      pole_lst[aux-1].append(pole_lst[source-1].pop())
      print("move",round,"from ",chr(ord('A')+source-1), "to", chr(ord('A')+aux-1))
      print('|  |  |')
      print_pole(n,pole_lst[0],pole_lst[1],pole_lst[2])
      TowerOfHanoi(round-1, dest, source, aux)

def print_pole(n,p1,p2,p3):
   if n != 0:
      if len(p1) >= n:
         print(p1[n-1],end = '  ')
      else:
         print('| ',   end = ' ')
      if len(p2) >= n:
         print(p2[n-1],end = '  ')
      else:
         print('| ',   end = ' ')
      if len(p3) >= n:
         print(p3[n-1],end = '  ')
      else:
         print('| ',   end = ' ')
      print()
      print_pole(n-1,p1,p2,p3)
   else:
      return 

def init(n):
    if n == 0:
        return []
    return [n] + init(n-1)

n = int(input("Enter Input : "))

pole_lst = [[],[],[]]
pole_lst[0] = init(n)
print('|  |  |')
print_pole(n,pole_lst[0],pole_lst[1],pole_lst[2])

TowerOfHanoi(n,1,2,3) 