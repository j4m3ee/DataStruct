Str = input('Enter String : ')
ls = []
for i in range(len(Str)):
    ls.append(Str[i])
j = 0
mapls = []
for i in ls:
    have = True
    for j in mapls:
        if i is j:
            have = False
    if have is True:
        mapls.append(i)

lsAns = []
for i in ls:
    for j,k in enumerate(mapls):
        if i is k:
            lsAns.append(j)
            break

print(lsAns)