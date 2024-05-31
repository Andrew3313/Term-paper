"""
bibliography/functions.py
Модуль процедур для работы с базой данных
Программист: Степашкин А.А. гр.344
Проверил: Дмитриева Т.А
Дата написания: 07.05.2024
"""

import csv

def addBook(books):
    """
    Процедура добавления книги в БД
    :return: Отсутствует
    """
    c = 0
    flag = True
    while flag:
        try:
            n = int(input("Сколько книг вы хотите добавить? Введите число: "))
            flag = False
        except ValueError:
            print("Ошибка: Введенное значение не является числом. Попробуйте еще раз.")
    while c < n:
        f = True
        author = input("Введите фамилию автора: ")
        title = input("Введите название книги: ")
        while f:
            try:
                pages = int(input("Введите количество страниц: "))
                f = False
            except ValueError:
                print("Ошибка: Введенное значение не является числом. Попробуйте еще раз.")
        newBook = {"Автор": author, "Название": title, "Число страниц": str(pages)}
        if newBook in books:
            print('Такая книга уже есть')
            c = n
        elif pages <= 0:
            print('Число страниц не может быть отрицательным или равняться нулю') 
            c = n   
        else:
            books.append(newBook)
            saveDB(books)
            c += 1
            print(f'Книга "{title}" автора "{author}" успешно добавлена в БД')
  
def removeBook(books):
    """
    Процедура удаления книги по Автору, названию и числу страниц
    :return: Отсутствует
    """
    author = input("Введите фамилию автора книги, которую нужно удалить: ")
    title = input("Введите название книги, которую нужно удалить: ")
    pages = input("Введите количество страниц книги, которую хотите удалить: ")
    key = (author, title, pages)
    found = False
    for i in range(len(books)):
        book = books[i]
        if (book['Автор'], book['Название'], book['Число страниц']) == key:
            del books[i]
            print(f"Книга '{title}' автора '{author}', содержащая '{pages}' страниц, успешно удалена из базы данных.")
            saveDB(books)
            found = True
            break
    if not found:
        print(f"Книга '{title}' автора '{author}', содержащая '{pages}' страниц, не найдена в базе данных.")
 
def saveDB(books):
    """
    Процедура сохранения обновленной базы данных в CSV-файл
    :return: Отсутствует
    """
    with open('books.csv', 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['Автор', 'Название', 'Число страниц']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(books) 