import math
def odd_even(arr, s):
    ans = []
    if s == 'Even':
        for i in range(len(arr)):
            if (i+1)%2 == 0:
                ans.append(arr[i])
        return ans
    elif s == 'Odd':
        for i in range(len(arr)):
            if (i+1)%2 == 1:
                ans.append(arr[i])
        return ans
    else:
        return ans

print('*** Odd Even ***')
inputList = list(map(str,input('Enter Input : ').split(",")))
if inputList[0] == 'L' :
    ls = inputList[1].split()
elif inputList[0] == 'S':
    ls = []
    for i in inputList[1]:
        ls.append(i)
else:
    pass
ans = odd_even(ls,inputList[2])

if inputList[0] == 'L':
    print(ans)
elif inputList[0] == 'S':
    s = ''
    for i in ans:
        s += str(i)
    print(s)

