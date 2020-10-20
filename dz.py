# 1 задание

def char(word):
  length = len(word)
  middle = round(length/2)
  print(middle)
  if length % 2 == 0:
    print(word[(middle - 1): (middle + 1)])
  else:
    print(word[middle])

char('tesyt')

#2 задание

user_input_sum = 0

while True:
    user_input = int(input('Введите число: '))
    
    if user_input != 0:
       user_input_sum += user_input
       pass
    else:
        print (f'Результат: {user_input_sum}')

#3 задание

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) == len(girls):
  result = zip(sorted(boys), sorted(girls))
  li = list(result)
  print('Идеальные пары: ')
  for element in li:
       print(f'{element[0]} и {element[1]}')
else:
  print('Не всем хватает пары')

#4 задание

countries_temperature = [
['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
['Germany', [57.2, 55.4, 59, 59, 53.6]],
['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]

def average_number(list):
  length = len(list)
  sum = 0
  for element in list:
    sum += element
  result = round(sum) / length
  return result

def f_to_c(number):
  return round((number - 32) * 5 / 9, 1)

for country in countries_temperature:
  print(f' {country[0]} - ' + str(f_to_c(average_number(country[1]))))





