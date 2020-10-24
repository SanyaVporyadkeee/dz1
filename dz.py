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

# 3 задание

results = {
'vk': {'revenue': 103, 'cost': 98},
'yandex': {'revenue': 179, 'cost': 153},
'facebook': {'revenue': 103, 'cost': 110},
'adwords': {'revenue': 35, 'cost': 34},
'twitter': {'revenue': 11, 'cost': 24},
}
roi = 0
for key, value in results.items():
  roi = {'ROI' : round((value['revenue'] / value['cost'] - 1) * 100, 2)}
  results[key].update(roi)

print(results) 

#4 задание

stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}

max_val = max(stats.values())
for key, value in stats.items():
  if value == max_val:
    print(f'Максимальный объем продаж на рекламном канале: {key}')









