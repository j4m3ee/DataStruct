'''
เขียน function insertion sort เพื่อเรียงข้อมูลใน list จากน้อยไปมาก โดยใช้ recursive

และแสดงขั้นตอนของ insertion sort ตามตัวอย่าง

***ห้ามใช้ คำสั่งloopต่างๆ เช่น for ,while หรือ Built-in Function ที่เกี่ยวกับ Sort เช่น .sort***

*** ยกเว้นให้ใช้  for ได้แค่ขั้นตอนรับ input เท่านั้น ***
'''

def get_index(lst,curr,data):
    if curr > 0 and lst[curr-1] > data:
        lst[curr] = lst[curr-1]
        return get_index(lst,curr-1,data)
    else:
        return curr

def insertion(l,s=0,n=0,p=0):
    if n == 0: 
        n = len(l)
    data = l[s]

    index = get_index(l,s,data)
    l[index] = data
    p += 1
    
    if p > 1:
        if len(l[p:]) != 0:
            print("insert {} at index {} : {} {}".format(data,index,l[:p],l[p:]))
        else:
            print("insert {} at index {} : {}".format(data,index,l[:p]))

    if s+1 < n:
        insertion(l,s+1,n,p)

if __name__ == "__main__":
    inp = [int(i) for i in input('Enter Input : ').split()]
    insertion(inp)
    print("sorted")
    print(inp)
