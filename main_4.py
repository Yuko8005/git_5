# завдання 2// номер 10
import math

a = int(input('введіть довжинусторони '))
n = int(input('введіть кількість кутів '))
nn = 180/n
d = math.cos(nn) / math.sin(nn)
s = d*(n*a**2/4)
print(f'площа многокутника = {s}см**2')