print('задача 1')

a = int(input('ціна в гривхня'))
while a < 0:
    print('ціна не може бути менше 0')
    a = int(input('ціна в гривхня'))

b = int(input('залишок ціни в копійках'))
while (b < 0)|(b >= 100):
    print('ціна в копійках може бути від 0 до 99')
    b = int(input('залишок ціни в копійках'))

n = int(input('скільки пиріжків бажаєте?'))
while n < 0:
    print('пиріжків не може бути менше 0')
    n = int(input('скільки пиріжків бажаєте?'))

a = a*100
totalCostCents = a*n + b*n
totalCostUAH = totalCostCents/100

print( 'загальна вартість ', n, 'пиріжків = ', totalCostCents, 'копійок')
print( 'загальна вартість ', n, 'пиріжків = ', totalCostUAH, 'грн')











