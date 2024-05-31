"""
main.py
Основная программа
Программист: Степашкин А.А. гр.344
Проверил: Дмитриева Т.А
Дата написания: 07.05.2024
"""

import csv
import bibliography as bbl

books = []
with open('books.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        books.append(row)

menuItem = ''
while menuItem != '5':
    # Выбор пункта меню
    menuItem = bbl.menu()
    if menuItem == '1':
        bbl.dataOutput(books)
        print()
    # Добавление N записей
    elif menuItem == '2':
        bbl.addBook(books)
        print()
    # Удаление записи по ключу
    elif menuItem == '3':
        bbl.removeBook(books)
        print()
    # Поиск числа произведений и общего числа страниц русских, советских и зарубежных авторов
    elif menuItem == '4':
        bbl.searchInfo(books)
        print()
    # Завершение работы программы
    elif menuItem == '5':
        print(' Работа программы завершена '.center(40, '-'))
    else:
        print('Некорректный ввод, введите число от 1 до 6')    
