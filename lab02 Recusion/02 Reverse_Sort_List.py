'''จงเขียนฟังก์ชั่นสำหรับการเรียงค่าใน List ของจำนวนเต็มโดยจะเรียงค่าจากมากไปน้อย
****ห้ามใช้ for/while และฟังก์ชั่นอื่นๆในการวนลูป ให้ใช้ recursion ในการเขียนเท่านั้น****'''

def quick_sort(l):
    if len(l) <= 1:
        return l
    else:
        return quick_sort([e for e in l[1:] if int(e) >= int(l[0])]) + [l[0]] + quick_sort([e for e in l[1:] if int(e) < int(l[0])])

if __name__=='__main__':
    n = input('Enter your List : ').split(',')
    print('List after Sorted : ['+', '.join(quick_sort(n))+']')
