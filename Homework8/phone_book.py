# Показывает содержимое справочника
def show_data():
    with open('text.txt', 'r', encoding='utf-8') as file:
        book = file.read()
    return book


# Добавление контакта в справочник
def new_data():
    with open('text.txt', 'a', encoding='utf-8') as file:
        file.write(input('\nВведите данные для контакта:\n') + '\n\n')


# Поиск в справочнике
def find_data():
    with open('text.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        temp = input('Кого хотите найти? Введите данные: ')
        for i in book:
            if temp in i:
                print(i)


# Удаление данных
def delete_contact(name):
    with open("text.txt", "r", encoding="utf-8") as file:
        contacts = file.readlines()
    with open("text.txt", "w", encoding="utf-8") as file:
        for contact in contacts:
            if name not in contact:
                file.write(contact)


# Изменение данных
def change_contact(new_data, old_data):
    with open("text.txt", "r", encoding="utf-8") as file:
        contacts = file.readlines()
    with open("text.txt", "w", encoding="utf-8") as file:
        for contact in contacts:
            if old_data in contact:
                file.write(new_data + "\n")
            else:
                file.write(contact)


while True:
    mode = input('Выберите режим работы справочника\n'
                 + '0 - Поиск, 1 - Увидеть содержимое справочника, '
                   '2 - Добавить новый контакт, 3 - Удалить, 4 - Изменить, 5 - Выйти: ')
    if mode == '1':
        print(show_data())
    elif mode == '0':
        find_data()
    elif mode == '2':
        new_data()
    elif mode == '3':
        name = input('Кого нужно удалить? Введите данные: ')
        delete_contact(name)
    elif mode == '4':
        old_data = input('Введите данные, которые нужно изменить: ')
        new_data = input('Введите новые данные: ')
        change_contact(new_data, old_data)
    elif mode == '5':
        break
    else:
        print('Некорректный ввод. Попробуйте снова.')
