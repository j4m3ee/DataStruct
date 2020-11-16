def insertion1(l):
    for i in range(1,len(l)):
        iEle = l[i]
        for j in range(i,-1,-1):
            if iEle<l[j-1] and j>0:
                l[j] = l[j-1]
            else:
                l[j] = iEle
                break
    
def insertion(l,n):
    if n<=1: 
        return
    insertion(l,n-1) 
    
    last = l[n-1] 
    j = n-2
      
    while (j>=0 and l[j]>last): 
        l[j+1] = l[j] 
        j = j-1
    print(last)
    l[j+1]=last 

# print("insert {} at index {} : [1, 2] [3, 4]".format(0,0))
# print('sorted')

if __name__ == "__main__":
    inp = [int(i) for i in input('Enter Input : ').split()]
    insertion1(inp)
    print(inp)
    insertion(inp,len(inp))
    print(inp)
