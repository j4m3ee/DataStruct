print('*** Fun with Drawing ***')
n = int(input('Enter input : '))

print('.'*(n-1) 
        + '*' 
        + '.'*(((n-1)*2)-1)
        + '*'
        + '.'*(n-1))

for i in range(n-1,1,-1):
    print('.'*(i-1) 
        + '*' 
        + '+'*(((n-i)*2)-1) 
        + '*'
        + '.'*(((i-1)*2)-1)
        + '*'
        + '+'*(((n-i)*2)-1) 
        + '*'
        + '.'*(i-1))

print('*' 
        + '+'*(((n-1)*2)-1) 
        + '*'
        + '+'*(((n-1)*2)-1)  
        + '*')

a = ((((n-1)*2)-1)*2)-1
for i in range(1,(n*2)-2):
    print('.'*i
        + '*'
        + '+'*(a-((i-1)*2))
        + '*'
        + '.'*i)

print('.'*((n*2)-2)
        + '*'
        + '.'*((n*2)-2))

    