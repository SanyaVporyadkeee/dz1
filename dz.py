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







