# завдання перше 1. Спробуйте відформатувати текст, як показано на зображенні. Виділяти текст сірим
# фоном та рисувати контури таблиці не потрібно.
str_0 = "\n{0:<15} {1} {2} {3} {4} ".format('Постачальник', 'СПД', 'Петренко', 'Ігор', 'Володимирович')
print(str_0)
str_1 = "\t\t{0} {1} {2} {3}".format('49000', 'м.Дніпропетровськ,', 'вул.Садова, 18', 'оф.16(056) 913-14 15')
print(str_1)
str_2 = "\t\t{0} {1} {2} {3} {4}".format('Юр. адреса:', '49000', 'м.Дніпропетровськ,', 'вул.Європейська,', '149')
print(str_2)
str_3 = "\t\t{0} {1} {2} {3} {4}".format('Р/р', '260046785001', 'в АТ дніпропетровська філія АТ ', '"ІНДЕКС-БАНК" МФО', '307015')
print(str_3)
str_4 = "\t\t{0} {1} {2} {3} {4}".format('ІПН', '3164175001', '№ свідоцтва 286127', 'ЄДРПОУ', '3164175001' )
print(str_4)
str_5 = "\t\t{0} {1} {2}".format('www.elki.com.ua', 'e-mail:', 'info@elki.com.ua' )
print(str_5)
str_6 = "\n{0:<15} {1} {2} {3}".format('Одержувач', 'Гімназія', '№12', 'ім.М.Кравчука')
print(str_6)
str_7 = "{0:<15} {1}".format('Платник', 'той самий')
print(str_7)
str_8 = "{0:<15} {1} {2} {3}".format('Умова продажу', 'Рахунок № 442', 'від', '11.11.2010')
print(str_8)
str_9 = "\t\t\t\t{0} \n\t\t\t\t{1}".format('Видаткова накладна № 411', 'від 11 листопада 2010 р.')
print(str_9)

str_10 = "{0:^3} {1:^45} {2:^6} {3:^15} {4:^15} {5:^15}".format('№', 'Повна назва товару', 'Од.вим.', 'К-ть', 'Ціна без ПДВ', 'Сума без ПДВ') 
print(str_10)
str_10 = "{0:>3} {1:<45} {2:^6} {3:>15} {4:>15} {5:>15}".format('1', 'Гірлянда хвойна (срібна) 2,5м', 'шт', '5,00', '18,200', '91б00') 
print(str_10)
str_10 = "{0:>3} {1:<45} {2:^6} {3:>15} {4:>15} {5:>15}".format('1', 'Гірлянда хвойна (срібна) 2,5м', 'шт', '5,00', '18,200', '91б00') 
print(str_10)
str_10 = "{0:>3} {1:<45} {2:^6} {3:>15} {4:>15} {5:>15}".format('1', 'Гірлянда хвойна (срібна) 2,5м', 'шт', '5,00', '18,200', '91б00') 
print(str_10)
str_10 = "{0:>3} {1:<45} {2:^6} {3:>15} {4:>15} {5:>15}".format('1', 'Гірлянда хвойна (срібна) 2,5м', 'шт', '5,00', '18,200', '91б00') 
print(str_10)
str_10 = "{0:>3} {1:<45} {2:^6} {3:>15} {4:>15} {5:>15}".format('1', 'Гірлянда хвойна (срібна) 2,5м', 'шт', '5,00', '18,200', '91б00') 
print(str_10)
str_10 = "{0:>3} {1:<45} {2:^6} {3:>15} {4:>15} {5:>15}".format('1', 'Гірлянда хвойна (срібна) 2,5м', 'шт', '5,00', '18,200', '91б00') 
print(str_10)
str_10 = "{0:>3} {1:<45} {2:^6} {3:>15} {4:>15} {5:>15}".format('1', 'Гірлянда хвойна (срібна) 2,5м', 'шт', '5,00', '18,200', '91б00') 
print(str_10)
str_10 = "{0:>3} {1:<45} {2:^6} {3:>15} {4:>15} {5:>15}".format('1', 'Гірлянда хвойна (срібна) 2,5м', 'шт', '5,00', '18,200', '91б00') 
print(str_10)

str_11 = "\t\t\t\t\t\t\t\t\t{0:>16} {1:>15}".format('Разом без ПДВ:', '1028б55')
print(str_11)
str_11 = "\t\t\t\t\t\t\t\t\t{0:>16} {1:>15}".format('ПДВ:', '205.8')
print(str_11)
str_11 = "\t\t\t\t\t\t\t\t\t{0:>16} {1:>15}".format('Всього з ПДВ:', '1233,65')
print(str_11)

str_12 = "\n{0}\n{1}\n\n{2}".format('Всього на суму:', 'Одна тисяча двісті тридцять три гривні 65 копійок', 'ПДВ: 205,61')
print(str_12)

str_13 = "\n{0:<19} {1:<20} {2:<15} {3:<20}".format('Відвантажив(ла):', '_________________', 'Отримав(ла):', '__________________')
print(str_13)
str_13 = "\n\t\t\t\t{0:<15} {1:<15} {2:<15}\n\n".format('за дорю серії', '№', 'від')
print(str_13)


