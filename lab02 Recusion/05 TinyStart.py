'''
นักศึกษาจะได้รับ Input เป็น list<int> ของดาวเคราะห์น้อย
สำหรับดาวเคราะห์น้อยแต่ละดวงนั้น ค่าสัมบูรณ์ จะแสดงขนาดของมัน และเครื่องหมายแสดงถึงทิศทางของมัน (ถ้าเลขเป็นบวกแสดงว่าวิ่งไปทางขวา ,ลบทางซ้าย) โดยที่ดาวเคราะห์น้อยแต่ละดวงเคลื่อนที่ด้วยความเร็วเท่ากัน

ค้นหาสถานะของดาวเคราะห์น้อยหลังจากการชนกันทั้งหมด

1.หากดาวเคราะห์น้อยสองดวงมาพบกันดวงที่เล็กกว่าจะระเบิด

2.ถ้าทั้งสองมีขนาดเท่ากันทั้งคู่จะระเบิด

3.ดาวเคราะห์น้อยสองดวงที่เคลื่อนที่ไปในทิศทางเดียวกันจะไม่มีวันพบกัน

****ห้ามใช้คำสั่ง for, while, do while*****

หมายเหตุ ฟังก์ชันมี parameter ได้ไม่เกิน 2 ตัว

code from : https://github.com/Qiral
'''

def asteroid_collision(asts):
    if len(asts) <= 1:
        return asts

    temp = asteroid_collision(asts[1:])
    
    if len(temp) != 0 and asts[0] > 0 and temp[0] < 0:
        if asts[0] > abs(temp[0]):
            return asteroid_collision([asts[0]] + temp[1:])
        elif asts[0] == abs(temp[0]):
            return temp[1:] if len(temp) > 1 else []
        else:
            return temp
    else:
        return [asts[0]] + temp

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x))