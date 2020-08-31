def chk_char(f2,f1,b1,b2):
    '''ans  = False
    if f1 == b1.lower() or f1 == b1.upper() and f2 == b2.lower() or f2 == b2.upper():
        ans = True'''
    return f1 == b1.lower() or f1 == b1.upper() and f2 == b2.lower() or f2 == b2.upper()

print('*** TorKham HanSaa ***')
ls = list(map(str,input('Enter Input : ').split(",")))
lsAns = []
for i,j in enumerate(ls): 
    
    if j[0] == 'P' and j[1] == ' ':
        if len(lsAns) is 0:
            lsAns.append(j[2:])
            print('\''+j[2:]+'\'','->',lsAns)
        elif chk_char(lsAns[-1][-1],lsAns[-1][-2],j[2],j[3]):
            lsAns.append(j[2:])
            print('\''+j[2:]+'\'','->',lsAns)
        else:
            print('\''+j[2:]+'\'','-> game over')
            exit(0)
            
    elif j[0] == 'R':
        lsAns = []
        print('game restarted')
    elif j[0] == 'X':
        exit(0)
    else:
        print('\''+j+'\'','is Invalid Input !!!')
        exit(0)
    