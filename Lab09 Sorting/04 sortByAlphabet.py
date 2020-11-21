'''
ให้เรียงลำดับ input ที่รับเข้ามาจากน้อยไปมาก โดยเรียงลำดับจากตัวอักษรที่มีอยู่ในแต่ละ string โดยตัวอักษรจะมีแค่ a - z เท่านั้น และในแต่ละ string จะมี alphabet เพียงแค่ 1 ตัวเท่านั้น

****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง
'''

def insertion(data):
    for i in range(1, len(data)):
        tmp = data[i]
        for k in range(i, -1, -1):
            if tmp < data[k - 1] and k > 0:
                data[k] = data[k - 1]
            else:
                data[k] = tmp
                break
    return data

if __name__ == "__main__":
    inp = input('Enter Input : ').split()
    dict,ls = {},[]
    for i in inp:
        for w in list(i):
            if ord(w) >= 97 and ord(w) <= 122:
                dict[w] = dict.get(w,i)
                ls.append(w)
    ls = insertion(ls)
    print(' '.join([dict[key] for key in ls]))


