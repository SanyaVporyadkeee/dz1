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





