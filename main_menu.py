def menu() -> int:
    main_menu = '''Главное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Создать контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход'''
    print(main_menu)
    while True:
        select = input('Выберите пункт меню: ')
        if select.isdigit() and 0 < int(select) < 9:
            return int(select)
        print('Введите число в контексте меню')


def show_context_menu():
    file_opened = False                       # Допилил флаг, для того, чтобы сначала юзер открывал файл, перед работой.
    while True:
        select = menu()
        if not file_opened and select != 1:
            print('Сначала откройте файл!')
            continue
        match select:
            case 1:
                open_file()
                file_opened = True
            case 2:
                save_file()
            case 3:
                show_contacts(phone_book)
            case 4:
                create_contact()
            case 5:
                result = search_contact()
                show_contacts(result)
            case 6:
                change_contact()
            case 7:
                delete_contact()
            case 8:
                print('До свидания! До новых встреч!')
                break
        print('*' * 200)


def open_file():                                                          # Тут сделал with open (сократил немного кода)
    with open(path, 'r', encoding='UTF-8') as data:
        data = data.readlines()
    for contact in data:
        nc = contact.strip().split(':')
        phone_book[int(nc[0])] = {'name': nc[1], 'phone': nc[2], 'comment': nc[3]}
    sorted(phone_book.items())
    print('\nТелефонный справочник успешно загружен')


def save_file():                                          # Тут сделал сортировку в переменной new при сохранении в файл
    new_data = []
    count = 1
    for _, cnt in sorted(phone_book.items()):
        new = ':'.join([str(count), cnt.get('name'), cnt.get('phone'), cnt.get('comment')])
        new_data.append(new)
        count += 1
    new_data = '\n'.join(new_data)
    with open(path, 'w', encoding='UTF-8') as data:
        data.write(new_data)
    print('Телефонный справочник успешно сохранен!')


def show_contacts(book: dict[int, dict]):
    print('*' * 200)
    for i, cnt in book.items():
        print(f"{i:>3}: {cnt.get('name'):<30} {cnt.get('phone'):<20} {cnt.get('comment'):<20}")


def create_contact():
    uid = max(list(phone_book.keys())) + 1
    name = input('Введите имя контакта: ')
    phone = input('Введите телефон контакта: ')
    comment = input('Введите комментарий к контакту: ')
    phone_book[uid] = {'name': name, 'phone': phone, 'comment': comment}
    print(f'Контакт {name} успешно добавлен в справочник!')
    print('*' * 200 + '/n')


def search_contact():
    result = {}
    word = input('Введите слово по которому будет осуществляться поиск: ')
    for i, cnt in phone_book.items():
        if word.lower() in ''.join(list(cnt.values())).lower():
            result[i] = cnt
    return result


def change_contact():                                                                 # Запилил функцию замены контакта
    show_contacts(phone_book)
    usr_id = int(input('Введите id контакта, который будем менять: '))
    if usr_id in phone_book:
        phone_book[usr_id]['name'] = input('Введите имя: ')
        phone_book[usr_id]['phone'] = input('Введите номер телефона: ')
        phone_book[usr_id]['comment'] = input('Введите комментарий: ')
    else:
        print('Контакт с указанным id не найден.')
    print('\nКонтакт успешно изменён!')


def delete_contact():                                                                       # Запилил функцию удаления
    show_contacts(phone_book)
    usr_id = int(input('Введите id контакта, который будем удалять: '))
    if usr_id in phone_book:
        phone_book.pop(usr_id)
        print('\nКонтакт успешно удален!')
    else:
        print('Такого id нет в справочнике')


phone_book = {}
path: str = 'phone_book.txt'
show_context_menu()

