#первая задача
phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
phrase_2 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'

if len(phrase_1) > len(phrase_2):
    print('1 длиннее фразы 2')
elif len(phrase_1) < len(phrase_2):
    print('2 длиннее фразы 1')
else:
    print('Фразы равной длины')

#вторая задача

def leap_year(year):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print('Високосный')
    else:
        print('Обычный')

leap_year(2019)
leap_year(2020)
#третья задача






