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





