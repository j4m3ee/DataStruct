def buble(l):
    for last in range(len(l)-1,-1,-1):
        swaped = False
        for i in range(last):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                swaped = True
        if not swaped:
            break

inp = [int(i) for i in input('Enter Input : ').split()]

buble(inp)
print(inp)