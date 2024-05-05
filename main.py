import csv
import functions as f

books = []
with open('books.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        books.append(row)

menuItem = 0
while menuItem != 5:
    # Выбор пункта меню
    menuItem = f.menu()
    # Цикл, если выбран неверный пункт
    while menuItem not in range(1, 6):
        menuItem = int(input('Такого пункта в меню нет, введите повторно номер пункта: '))
        print()
    # Просмотр всех записей в базе данных
    if menuItem == 1:
        f.dataOutput(books)
        print()
    # Добавление N записей
    elif menuItem == 2:
        f.addBook(books)
        print()
    # Удаление записи по ключу
    elif menuItem == 3:
        f.removeBook(books)
        print()
    # Поиск числа произведений и общего числа страниц русских, советских и зарубежных авторов
    elif menuItem == 4:
        f.searchInfo(books)
        print()
# Завершение работы программы
print(' Работа программы завершена '.center(40, '-'))