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
text = '3240'
try:
    print(text[-2])
except IndexError:
    print('0')
