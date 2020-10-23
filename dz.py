# 1 задание

ids = {'user1': [213, 213, 213, 15, 213],
        'user2': [54, 54, 119, 119, 119],
        'user3': [213, 98, 98, 35]}

ids_set = list(ids.values())
res = set()
for elem in ids_set:
  for el in elem:
    res.add(el)
print(res)

# 2 задание

queries = [
'смотреть сериалы онлайн',
'новости спорта',
'афиша кино',
'курс доллара',
'сериалы этим летом',
'курс по питону',
'сериалы про спорт',
]

new_list = []

for elem in queries:
  new_list.append(len(elem.split(' ')))

sum_3 = new_list.count(3)
sum_2 = new_list.count(2)
percent_3 = round((sum_3/len(new_list)) * 100, 2)
percent_2 = round((sum_2/len(new_list)) * 100, 2)

print(f'Поисковых запросов, содержащих 2 слов(а): {percent_2} %\nПоисковых запросов, содержащих 3 слов(а): {percent_3} %')







