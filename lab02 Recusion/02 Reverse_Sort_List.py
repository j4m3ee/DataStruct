'''จงเขียนฟังก์ชั่นสำหรับการเรียงค่าใน List ของจำนวนเต็มโดยจะเรียงค่าจากมากไปน้อย
****ห้ามใช้ for/while และฟังก์ชั่นอื่นๆในการวนลูป ให้ใช้ recursion ในการเขียนเท่านั้น****'''

def sorted(n):
    if n == []:
        return []
    else :
        if len(n) == 1:
            return [n[-1]]
        elif n[0] > n[1]:
            return [n[0]]+sorted(n[1:])
        else :
            return

    
if __name__=='__main__':
    n = input('Enter your List : ').split(',')
    sorted(n)
