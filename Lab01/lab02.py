print(' *** Wind classification ***')
x = float(input('Enter wind speed (km/h) : '))
h = 'Wind classification is '
if x > 0 and x <= 51.99:
    print(h+'Breeze.')
elif x >= 52 and x <= 55.99:
    print(h+'Depression.')
elif x>= 56 and x <= 101.99:
    print(h+'Tropical Storm.')
elif x >=102 and x <= 208.99:
    print(h+ 'Typhoon.')
elif x >= 209:
    print(h+'Super Typhoon.')

