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







