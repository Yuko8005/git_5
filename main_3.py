# завдання 2// № 6
a=0
SSs=0

def num():
    global a, SSs
    try:
        a = int(input('ffffffffff '))
        SSs = (a*(a+1))/2 if a>1 else 'введіть число більше 1!!!!!!!!!!!!!!!' 
        print(SSs)
        num()
        
        
        
    except:
        print('введіть число!!!!!!!!')
        num()

num()