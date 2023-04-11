def add_clients():
    file = open('Guide.txt', 'a', encoding='UTF-8')
    data1 = input('Введите ФИО: ')
    data2 = input('Номер телефона: ')
    data3 = input('Место работы: ')
    data = '\n' + data1 + '; ' + data2 + '; ' + data3
    print(data)
    file.write(data)
    file.close()

def read_cont():
    file = open('Guide.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    file.close()
    for contact in data:
        print(contact)
    read_cont()

def find_cont():
    file = open('Guide.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    file.close()
    search_cont = input('Введите для поиска информацию: ')
    for cont in data:
        if search_cont.lower() in cont.lower():
            print(cont)
    find_cont()

def change_cont():
    phone_book = []
    file = open('Guide.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    file.close()
    i = 0
    for contact in data:
        new_contact = contact.strip().split(';')
        new_contact = {'id': i,
                    'name':new_contact[0],
                    'phone':new_contact[1],
                    'comment':new_contact[2]}
        phone_book.append(new_contact)
        i +=1
    print(phone_book)
    elem = int(input('Введите id: '))
    print(phone_book[elem])
    change_cont()

def delete_person(name):
    persons = read_data()
    with open("Guide.txt", "w", encoding="utf8" ) as file:
        for person in persons:
            if name != person:
                file.write(person)

def change_person(new_name, old_name):
    persons = read_data()
    with open("Guide.txt", "w", encoding="utf8" ) as file:
        for person in persons:
            if  old_name != person:
                file.write(person)
            else:
                file.write(new_name + "\n")

while True:
    mode = input('Выберите режим работы справочника' + '\n'
                  +'0-поиск, 1-чтение файла, 2-добавление в файл, 3-удаление, 4-замена, 5-выход: ')
    if mode == '1':
        print(add_clients())
    elif mode == '0':
        change_cont()
    elif mode == '2':
        find_cont()
    elif mode == '3':
        name = input('кого удаляем?: ')
        delete_person(name)
    elif mode == '4':
        old_name = input('кого хотим переименовать?: ')
        new_name = input('как хотим его назвать?: ')
        change_person(new_name,old_name)
    elif mode == '5':
        break
    else:
        print('No mode')
