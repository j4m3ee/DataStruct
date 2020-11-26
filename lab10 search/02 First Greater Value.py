'''
ให้น้องเขียนโปรแกรมหาค่าที่น้อยที่สุดที่มากกว่าค่าที่ต้องการจะหา ถ้าหากไม่มีให้แสดงว่า No First Greater Value โดยตัวเลขของทั้ง 2 list รับประกันว่าไม่เกิน 1000000

***** อธิบาย Test Case 2:
Left : [3, 2, 7, 6, 8]         Right : [5, 6, 12]
1. หาค่าที่น้อยที่สุดที่มากกว่า 5 จาก list (Left) จะได้เป็น 6
2. หาค่าที่น้อยที่สุดที่มากกว่า 6 จาก list (Left) จะได้เป็น 7
3. หาค่าที่น้อยที่สุดที่มากกว่า 12 จาก list (Left) จะเห็นว่าไม่มีค่าที่มากกว่า 12 จะแสดงเป็น No First Greater Value
'''

def binary_search(first,last,ls,val):
    mid = (first+last) // 2

    if last < first:
        if first == len(ls):
            return 'No First Greater Value'
        return ls[first]

    if val < ls[mid]:
        return binary_search(first,mid-1,ls,val)
    elif val > ls[mid]:
        return binary_search(mid + 1,last,ls,val)
    else:
        if ls[mid] is not ls[-1]:
            return ls[mid + 1]
        return 'No First Greater Value'


if __name__ == "__main__":
    inp = input('Enter Input : ').split('/')
    ls1 = [int(i) for i in inp[0].split()]
    ls2 = [int(i) for i in inp[1].split()]
    for i in ls2:
        print(binary_search(0,len(ls1)-1,sorted(ls1),i))