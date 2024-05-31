"""
bibliography/dataOutput.py
Модуль, в котором реализована процедура вывода БД
Программист: Степашкин А.А. гр.344
Проверил: Дмитриева Т.А
Дата написания: 07.05.2024
"""

from prettytable import PrettyTable

def dataOutput(books):
    """
    Процедура вывода БД
    :return: Отсутствует
    """
    table = PrettyTable()
    table.field_names = ["Автор", "Название", "Число страниц"]
    for book in books:
        table.add_row([book['Автор'], book['Название'], book['Число страниц']])
    print("Содержимое базы данных:")
    print(table)
    print()