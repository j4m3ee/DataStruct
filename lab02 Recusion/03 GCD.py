'''
เขียนโปรแกรมสำหรับหา หรม. ของเลข 2 ตัว
****ห้ามใช้คำสั่ง len, for, while, do while หรือ *****
หมายเหตุ ฟังก์ชันต้องมี parameter แค่เพียง 2 ตัว
'''

def gcd(a,b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a%b == 0:
        return b
    else:
        return gcd(b,a%b)


n = list(map(int, input("Enter Input : ").split()))

if n[0] == 0 and n[1] == 0:
    print('Error! must be not all zero.')
    exit()
g = gcd(min(n),max(n))
if g < 0 and n[0] < 0 and n[1] < 0:
    print('The gcd of {} and {} is : {}'.format(min(n),max(n),g*-1))
else:
    print('The gcd of {} and {} is : {}'.format(max(n),min(n),abs(g)))




