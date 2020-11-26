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


#  !!!!! много непонятных моментов с else, без него return отрабатывает корректно во многих заданиях, но с ним возвращает исключительно else результат
# Задание 1
# Пункт 1. Пользователь по команде “p” может узнать владельца документа по его номеру
def find_name():
    number_of_doc = input()
    for i in documents:
            for key, value in i.items():
                if number_of_doc == value:
                    return (i['name'])
                # else:
                #     return 'Документ не найден в базе' !!!при раскомментировании в любом случае возвращает результат else, не ясно причина

# Пункт 2. Пользователь по команде “s” может по номеру документа узнать на какой полке он хранится
def find_shell(number_of_doc):
    for key, value in directories.items():
        if number_of_doc in value:
            return key
        # else: 
        #     return 'Документ не найден в базе'


# Пункт 3. Пользователь по команде “l” может увидеть полную информацию по всем документам
def show_info():
    for i in documents:
        print(f"№: {i['number']}, тип: {i['type']}, владелец: {i['name']}, номер полки: {find_shell(i['number'])}")

# Пункт 4. Пользователь по команде “as” может добавить новую полку

def add_shell():
    number_of_shell = input()
    if number_of_shell not in directories:
        directories[number_of_shell] = []
        return f'Полка добавлена. Текущий перечень полок: {list(directories.keys())}'
    else:
        return f'Такая полка уже существует. Текущий перечень полок: {list(directories.keys())}'
        # не понятно, как вывести значения


# Пункт 5. Пользователь по команде “ds” может удалить существующую полку из данных (только если она пустая)
def delete_shell():
    number_of_shell = input()
    if len(directories[number_of_shell]) < 1:
        del directories[number_of_shell]
        return f'Полка удалена. Текущий перечень полок: {list(directories.keys())}'
    else:
        return f'На полке есть документа, удалите их перед удалением полки. Текущий перечень полок: {list(directories.keys())}'
        # не понятно, как вывести значения

#Задание 2
# Пункт 1. Пользователь по команде “ad” может добавить новый документ в данные 
def add_doc():
    number_of_doc = input()
    type_of_doc = input()
    owner_of_doc = input()
    number_of_shell = input()
    d = {'type': type_of_doc, 'number': number_of_doc, 'name': owner_of_doc}
    documents.append(d)
    directories[number_of_shell] = number_of_doc
    print('Документ добавлен. Текущий список документов:')
    show_info()

#Пункт 2. Пользователь по команде “d” может удалить документ из данных 
def delete_doc():
    number_of_doc = input()
    for i in documents:
        if i['number'] == number_of_doc:
            documents.remove(i)

            
def add_v(d, shell, val):
    for key, value in d.items():
        if key == shell:
            value.append(val)

def delete_v(d, val):
    for key, value in d.items():
        for i in value:
            if i == val:
                value.remove(i)

def change_shell(dict_):
    number_of_doc = input()
    number_of_shell = input()
    delete_v(dict_, number_of_doc)
    add_v(dict_, number_of_shell, number_of_doc)
    show_info()


def ask():
    while True:
        n = input()
        if n == 'q':
            break
        elif n == 'p':
            print(find_name())
        elif n == 's':
            print(find_shell())
        elif n == 'l':
            print(show_info())
        elif n == 'as':
            print(add_shell())
        elif n == 'ds':
            print(delete_shell())
        elif n == 'ad':
            print(add_doc())
        elif n == 'd':
            print(delete_doc())
        else:
            print('команда не найдена')
# ask()