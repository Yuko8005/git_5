# завдання 2
# 3. Компанія з виробництва енергетичних напоїв провела опитування, згідно з яким
# близько 14% споживачів її продукції купують принаймні один напій на тиждень. 64% з
# таких покупців віддають перевагу цитрусовому напою. Програма повинна отримувати
# на вхід кількість опитаних, а на виході виводити кількість споживачів, що купують
# принаймні 1 напій на тиждень, а також кількість покупців, які віддають перевагу
# цитрусовим напоям.



# a - всі опитані
# b - ті що вживають енергенити принаймні один напій на тиждень
# c - ті що віддають перевагу цитрусовим напоям

a = 0
b = 0
c = 0



def get_the_next():
        global the_next
        the_next = input('це остання людина? : введіть так або ні')
        if the_next == 'так':
            global a, b
            ggg = ((b*100)/a)
            ccc = ((c*100)/b)
            print(f'близько {ggg}% споживачів її продукції купують принаймні один напій на тиждень\n{ccc}% з таких покупців віддають перевагу цитрусовому напою')
        elif the_next == 'ні':
            run_opros()
        else:
            print('введіть так або ні !!!!!!')
            get_the_next()




def run_opros():
    
    global a, b, c, question_1, question_2, question_3

    
    question_1 = input('ви вживаєте енергетичні напої ? \na) так  \nb) ні ')
    if question_1 == 'так':
        a +=1

        question_2 = input('ви вживаєте принаймні один напій на тиждень? \na)так \nb)ні ')

        if question_2 == 'так':
            b+=1

            question_3 = input('ви віддаєте перевагу цитрусовим напоям? \na)так \nb)ні ')

            if question_3 == 'так':
                c+=1
                get_the_next()


            elif question_3 == 'ні':
                
                get_the_next()

            else:
                print('hhh')

        elif question_2 == 'ні':
            get_the_next()

            

        else:
            print('rugan')

            
        

    elif question_1 == 'ні':
        get_the_next()
        a+=1
        
        
    else:
        print('введіть коректні дані')
        run_opros()

    
run_opros()

