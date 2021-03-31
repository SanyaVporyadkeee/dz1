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

#отобразить данные корректно
def make_li_seq(li):
    a = ''
    for i in li:
        if i == li[-1]:
            a += f'{i}.'
        else:
            a += f'{i}, '
    return a

# добавить новую полку
def add_shell():
    res = f'Такая полка уже существует. Текущий перечень полок: {make_li_seq(list(directories.keys()))}'
    number_of_shell = input()
    if number_of_shell not in directories:
        directories.setdefault(number_of_shell, [])
        res = f'Полка добавлена. Текущий перечень полок: {make_li_seq(list(directories.keys()))}'
    return res

# удаление полки
def delete_shell():
    number_of_shell = input()
    res = f'На полке есть документа, удалите их перед удалением полки. Текущий перечень полок: {make_li_seq(list(directories.keys()))}'
    if number_of_shell not in directories:
        res = f'Такой полки не существует. Текущий перечень полок: {make_li_seq(list(directories.keys()))}'
    elif directories[number_of_shell] == []:
        del directories[number_of_shell]
        res = f'Полка удалена. Текущий перечень полок: {make_li_seq(list(directories.keys()))}'
    return res


#добавить новый документ
def add_new_doc():
    res = f'Такой полки не существует. Добавьте полку командой as.\nТекущий список документов:\n{show_info()}'
    number_of_doc = input()
    type_of_doc = input()
    owner_of_doc = input()
    number_of_shell = input()
    di = {'type': number_of_doc, 'number': type_of_doc, 'name': owner_of_doc}
    if number_of_shell in directories:
        documents.append(di)
        directories.setdefault(number_of_shell, []).append(number_of_doc)
        res = f'Документ добавлен. Текущий список документов:\n{show_info()}'
    return res

#удалить документ из директории
def del_from_dir(number_of_doc):
    for k, v in directories.items():
        if number_of_doc in v:
            v.remove(number_of_doc)
        

# удалить документ из документов
def del_from_docs():
    number_of_doc = input()
    for i in documents:
        if i['number'] == number_of_doc:
            documents.remove(i)
            del_from_dir(number_of_doc)
            res = f'Документ удален.\nТекущий список документов:\n{show_info()}'
        else:
            res = f'Документ не найден в базе.\nТекущий список документов:\n{show_info()}'
    return res

def change_shell():
    res = f'Такой полки не существует.\nТекущий перечень полок:\n{make_li_seq(list(directories.keys()))}'
    number_of_doc = input()
    number_of_shell = input()
    del_from_dir(number_of_doc)
    if number_of_shell in directories:
        directories.setdefault(number_of_shell, []).append(number_of_doc)
        res = f'Документ перемещен. Текущий список документов:\n{show_info()}'
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
    elif command == 'd':
        print(del_from_docs())
    elif command == 'm':
        print(change_shell())