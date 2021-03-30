documents = [
{'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
{'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
{'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
'1': ['2207 876234', '11-2'],
'2': ['10006'],
'3': []
}



# поиск имени по номеру документа
def find_name():
    number_of_document = input()
    res = 'Документ не найден в базе'
    for document in documents:
        if document['number'] == number_of_document:
            res = document['name']
    return res

# поиск полки по номеру документа
def find_shell():
    number_of_document = input()
    res = 'Документ не найден в базе'
    for k, v in directories.items():
        if number_of_document in v:
            res = f'Документ хранится на полке: {k}'
    return res

# показать информацию
def show_info():
    res = ''
    for di in documents:
        for k, v in directories.items():
            if di['number'] in v:
                res += f'№: {di["number"]}, тип: {di["type"]}, владелец: {di["name"]}, полка хранения: {k}\n'
    return res

# добавить новую полку
def add_shell():
    res = 'Такая полка уже существует. Текущий перечень полок: 1, 2, 3.'
    number_of_shell = input()
    if number_of_shell not in directories:
        directories.setdefault(number_of_shell, [])
        res = f'Полка добавлена. Текущий перечень полок: 1, 2, 3, {number_of_shell}.'
    return res

# удаление полки
def delete_shell():
    number_of_shell = input()
    res = 'На полке есть документа, удалите их перед удалением полки. Текущий перечень полок: 1, 2, 3.'
    if number_of_shell not in directories:
        res = 'Такой полки не существует. Текущий перечень полок: 1, 2, 3.'
    elif directories[number_of_shell] == []:
        del directories[number_of_shell]
        res = 'Полка удалена. Текущий перечень полок: 1, 2.'
    return res

while True:
    command = input()
    if command == 'q':
        break
    elif command == 'p':
        print(find_name())
    elif command == 's':
        print(find_shell())
    elif command == 'l':
        print(show_info())
    elif command == 'as':
        print(add_shell())
    elif command == 'ds':
        print(delete_shell())