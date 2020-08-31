from statistics import mode
print('*** Election ***')
num = int(input('Enter a number of voter(s) : '))
ls = list(map(int,input().strip().split()))[:num] 

for i,e in enumerate(ls):
    if e <= 0 or e > 20:
        ls[i] = -1
c = ls.count(-1)
for i in range(c):
    ls.remove(-1)

if len(ls) == 0:
    print('*** No Candidate Wins ***')
else:
    print(mode(ls))
