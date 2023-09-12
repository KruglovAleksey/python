n = int(input("Введите кол-во монеток: "))
Tails = 0
Heads = 0
from random import randint
for i in range(n):
    i = randint(0, 1)
    print(i, end= ' ')
    if i == 0:
        Tails += 1
    else: 
        Heads += 1
print()
if Tails > Heads:
    print(Heads)
else:
    print(Tails)