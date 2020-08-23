ls = list(map(int,input('Enter Your List : ').split()))
lsDemo = []
lsAns = []
if len(ls) >= 3:
    if ls[0] is 0 and ls[1] is 0 and ls[2] is 0:
        lsAns.append([0,0,0])
    else:
        for i in range(len(ls)):
            for j in range(len(ls)):
                for k in range(len(ls)):
                    if ls[i] + ls[j] + ls[k] is 0 and ls[i] < ls[j] < ls[k]:
                        lsAns.append([ls[i],ls[j],ls[k]])
    print(lsAns)    
else:
    print('Array Input Length Must More Than 2')
    
