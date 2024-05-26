from prettytable import PrettyTable

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