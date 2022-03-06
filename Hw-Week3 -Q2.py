
x = int(input('bezan number x ra:'))
y = int(input('bezan number y ra:'))
z = int(input('bezan number z ra:'))

if x*x == y*y + z*z or y*y == x*x + z*z or z*z == x*x + y*y:
    print('Right')
else:
    print('Not Right')