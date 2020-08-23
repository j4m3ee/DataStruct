print('*** Converting hh.mm.ss to seconds ***')
h,m,s = input('Enter hh mm ss : ').split()
if int(m)>=60 or int(m)<0 :
    print('mm('+m+') is invalid!')
elif int(s)>=60 or int(s)<0 :
    print('ss('+s+') is invalid!')
else:
    sec = (int(h)*3600) + (int(m)*60) + int(s)
    print("{:02d}:{:02d}:{:02d} = {:,d} seconds".format(int(h),int(m),int(s),sec))


#mm(88) is invalid!