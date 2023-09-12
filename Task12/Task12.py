s = int(input("Сумма чисел равна: "))
p = int(input("Произведение чисел равно: "))

# x*x - s*x + p = 0

Diskr = (s * s) + (- 4 * p)
if Diskr > 0:
    x1 = (s + Diskr**(0.5))/2
    x2 = (s - Diskr**(0.5))/2
    print(f'Загаданные числа: {int(x1)}, {int(x2)}') 
elif Diskr == 0:
    x1 = s / 2
    print(f'Загаданные числа: {int(x1)}, {int(x1)}')  
else:
    print('Таких чисел нет') 
