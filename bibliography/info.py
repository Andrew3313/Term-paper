"""
bibliography/info.py
Модуль, в котором реализована функция определения
национальности автора, процедура подсчета числа произведений
и общего числа страниц 
Программист: Степашкин А.А. гр.344
Проверил: Дмитриева Т.А
Дата написания: 07.05.2024
"""

def getNationality(author):
    """
    Функция определения национальности автора
    :return: nationality - национальность автора
    """
    russianAuthors = ["Пушкин", "Толстой", "Достоевский", "Чехов", "Лермонтов", "Бунин", "Пришвин", "Васильев", "Рубина", "Лукьяненко"]
    sovietAuthors = ["Горький", "Шолохов", "Маяковский", "Твардовский", "Ахматова", "Блок", "Высоцкий"]
    nationality = ''
    if author in russianAuthors:
        nationality += "Русский"
    elif author in sovietAuthors:
        nationality += "Советский"
    else:
        nationality += "Зарубежный"
    return nationality

def searchInfo(books):
    """
    Процедура подсчета числа произведений и общего числа страниц по национальностям
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