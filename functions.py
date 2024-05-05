import csv
from prettytable import PrettyTable

def menu():
    """
    Функция показа меню и выбора его пункта
    :return: menuItem - номер выбранного пункта
    """
    print(" МЕНЮ ".center(35, '-'))
    print("1 - Просмотр всех записей в базе данных\n"
          "2 - Добавление N записей\n"
          "3 - Удаление записи по ключу\n"
          "4 - Поиск необходимой информации\n"
          "5 - Завершение работы с базой данных\n")

    menuItem = int(input('Выберите пункт меню, написав его номер: '))
    print()
    return menuItem

def getNationality(author):
    """
    Функция определения национальности автора
    :return: nationality - национальность автора
    """
    russianAuthors = ["Пушкин", "Толстой", "Достоевский", "Чехов", "Лермонтов", "Бунин", "Пришвин"]
    sovietAuthors = ["Горький", "Шолохов", "Маяковский", "Твардовский", "Ахматова", "Блок", "Высоцкий"]
    nationality = ''
    if author in russianAuthors:
        nationality += "Русский"
    elif author in sovietAuthors:
        nationality += "Советский"
    else:
        nationality += "Зарубежный"
    return nationality

def dataOutput(books):
    """
    Функция вывода БД
    :return: Отсутствует
    """
    table = PrettyTable()
    table.field_names = ["Автор", "Название", "Число страниц"]
    for book in books:
        table.add_row([book['Автор'], book['Название'], book['Число страниц']])
    print("Содержимое базы данных:")
    print(table)
    print()

def addBook(books):
    """
    Функция добавления книги в БД
    :return: Отсутствует
    """
    n = int(input("Сколько книг вы хотите добавить? Введите число: "))
    c = 0
    while c < n:
        author = input("Введите фамилию автора: ")
        title = input("Введите название книги: ")
        pages = input("Введите количество страниц: ")
        newBook = {"Автор": author, "Название": title, "Число страниц": pages}
        if newBook in books:
            print('Такая книга уже есть')
            c = n
        elif int(pages) <= 0:
            print('Число страниц не может быть отрицательным или равняться нулю') 
            c = n   
        else:
            books.append(newBook)
            saveDB(books)
            c += 1
            print(f'Книга "{title}" автора "{author}" учпешно добавлена в БД')
                      
        
    # for _ in range(n):
    #     author = input("Введите фамилию автора: ")
    #     title = input("Введите название книги: ")
    #     pages = input("Введите количество страниц: ")
    #     newBook = {"Автор": author, "Название": title, "Число страниц": pages}
    #     if newBook in books:
    #         print('Такая книга уже есть')
    #     else:
    #         books.append(newBook)
    #         saveDB(books)          
        
def searchInfo(books):
    """
    Функция подсчета числа произведений и общего числа страниц по национальностям
    :return: Отсутствует
    """
    russianCount = 0
    russianPages = 0
    sovietCount = 0
    sovietPages = 0
    foreignCount = 0
    foreignPages = 0
    
    for book in books:
        author = book['Автор']
        pages = int(book['Число страниц'])
        nationality = getNationality(author)
        if nationality == "Русский":
            russianCount += 1
            russianPages += pages
        elif nationality == "Советский":
            sovietCount += 1
            sovietPages += pages
        else:
            foreignCount += 1
            foreignPages += pages

    print("Русские авторы:")
    print(f"Число произведений: {russianCount}")
    print(f"Общее число страниц: {russianPages}")
    print("\nСоветские авторы:")
    print(f"Число произведений: {sovietCount}")
    print(f"Общее число страниц: {sovietPages}")
    print("\nЗарубежные авторы:")
    print(f"Число произведений: {foreignCount}")
    print(f"Общее число страниц: {foreignPages}")
  
def removeBook(books):
    """
    Функция удаления книги по Автору и названию
    :return: none
    """
    author = input("Введите фамилию автора книги, которую нужно удалить: ")
    title = input("Введите название книги, которую нужно удалить: ")
    pages = input("Введите количество страниц книги, которую хотите удалить: ")
    key = (author, title, pages)
    for book in books:
        if (book['Автор'], book['Название'], book['Число страниц']) == key:
            books.remove(book)
            print(f"Книга '{title}' автора '{author}', содержащая '{pages}' страниц, успешно удалена из базы данных.")
            saveDB(books)
            return
    print(f"Книга '{title}' автора '{author}', содержащая '{pages}' страниц, не найдена в базе данных.")
 
def saveDB(books):
    """
    Функция сохранения обновленной базы данных в CSV-файл
    :return: Отсутствует
    """
    with open('books.csv', 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['Автор', 'Название', 'Число страниц']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(books) 