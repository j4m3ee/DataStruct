class number:
    def __init__(self,num = None):
        self.num = num

    def __add__(self,other):
        return self if self.num > other.num else other

    def addnum(self,num):
        self.num = num
'''ls = list(map(str,input('Enter list : ').split()))
lsa = []
print(ls)
ls.reverse()
lsa.append(ls.copy())
print(lsa)'''
#lst = [int(a) for a in input('input : ').split(",")]
#print(lst)
n1 = number(int(input('Enter number : ')))
n2 = number(int(input('Enter number : ')))
print((n1.__add__(n2)).num)