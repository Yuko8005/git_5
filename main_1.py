#  завдання перше
import math

x = 0
y = 0

def get_a():
    global x, y
    try:
        y = float(input('введіть катет '))
        x = float(input('введіть прилеглий кут'))

        if x < 90 and y>0:
            gip = y/math.cos(x)
            cat = y*math.tan(x)
            Per = y + cat + gip
            Ss = 1/2*y*cat
            fof = 180 - (x + 90)
            print(f'\nгіпотенуза = {gip} \nкатет = {cat} \nпериметр = {Per} \nплоща = {Ss} \nпротилежний кут = {fof}')

        elif x <= 0:
            print('кут не може бути від\'ємним !!!!!! \n введіть додатнє число !!!!!!!!!!')
            get_a()
        elif y <= 0:
            print('сторона не може бути від\'ємною !!!!!! \n введіть додатнє число !!!!!!!!!!')
            get_a()
        elif x > 90:
            print('прилеглий кут менше 90 градуів !!!!!!!!!!!!!')
            get_a()
                
    except:
        print('введіть число!!!')
        get_a()



get_a()



