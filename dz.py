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


def find_shell(doc_num):
    for key, value in directories.items():
        if doc_num in value:
            return key
    
def find_name(doc_num):
    for i in documents:
        for key, value in i.items():
            if doc_num == value:
                return i['name']
            else:
                return 'Документ не найден в базе'


def show_info():
    for i in documents:
        print(f"№: {i['number']}, тип: {i['type']}, владелец: {i['name']}, номер полки: {find_shell(i['number'])}")


def add_shell():
    number_of_shell = input()
    if number_of_shell not in directories:
        directories[number_of_shell] = []
        print(f'Полка добавлена. Текущий перечень полок: {list(directories.keys())}')
    else:
        print(f'Такая полка уже существует. Текущий перечень полок: {list(directories.keys())}')


def delete_shell():
    number_of_shell = input()
    if len(directories[number_of_shell]) < 1:
        del directories[number_of_shell]
        print(f'Полка удалена. Текущий перечень полок: {list(directories.keys())}')
    else:
        print(f'На полке есть документа, удалите их перед удалением полки. Текущий перечень полок: {list(directories.keys())}')


def ask():
    while True:
        n = input()
        if n == 'q':
            break
        if n == 'p':
            p = input()
            find_name(p)
        if n == 's':
            s = input()
            find_shell(s)
        if n == 'l':
            show_info()
        if n == 'as':
            add_shell()
        if n == 'ds':
            delete_shell()
ask()








