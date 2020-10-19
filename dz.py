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

day = input('Введите день')
month = input('Введите месяц')

if (day>=21 and day<=31 and month==3) or( month==4 and day>=1 and day<=19):

   print("Знак зодиака:Овен")

elif (day>=20 and day<=30 and month==4) or( month==5 and day>=1 and day<=20):

   print("Знак зодиака:Телец")

elif (day>=21 and day<=31 and month==5) or( month==6 and day>=1 and day<=21):

   print("Знак зодиака:Близнецы")

elif (day>=22 and day<=30 and month==6) or( month==7 and day>=1 and day<=22):

   print("Знак зодиака:Рак")

elif (day>=23 and day<=31 and month==7) or( month==8 and day>=1 and day<=22):

   print("Знак зодиака:Лев")

elif (day>=23 and day<=31 and month==8) or( month==9 and day>=1 and day<=22):

   print("Знак зодиака:Дева")

elif (day>=23 and day<=30 and month==9) or( month==10 and day>=1 and day<=23):

   print("Знак зодиака:Весы")

elif (day>=24 and day<=31 and month==10) or( month==11 and day>=1 and day<=22):

   print("Знак зодиака:Скорпион")

elif (day>=23 and day<=30 and month==11) or( month==12 and day>=1 and day<=21):

   print("Знак зодиака:Стрелец")

elif (day>=22 and day<=31 and month==12) or( month==1 and day>=1 and day<=20):

   print("Знак зодиака:Козерог")

elif (day>=21 and day<=31 and month==1) or( month==2 and day>=1 and day<=18):

   print("Знак зодиака:Водолей")

elif (day>=19 and day<=29 and month==2) or( month==3 and day>=1 and day<=20):

   print("Знак зодиака:Рыбы")

#четвертое задание








