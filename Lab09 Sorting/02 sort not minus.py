def buble(l):
    for last in range(len(l)-1,-1,-1):
        swaped = False
        for i in range(last):
            a1,a2 = i,i+1
            if l[a1] < 0 and l[a2] < 0:
                continue
            if l[a2] < 0:
                a2 += 1
                if a2 > last: break
            if l[a1] > l[a2]:
                l[a1], l[a2] = l[a2], l[a1]
                swaped = True
        if not swaped: break
            
if __name__ == "__main__":
    inp = [int(i) for i in input('Enter Input : ').split()]
    buble(inp)
    print(' '.join(str(i) for i in inp))