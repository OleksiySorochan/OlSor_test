import os

    # функція яка бере шлях дерикторю, та роздруковує окремо назви папків та файлів та кількість
def print_file_dir(path= os.getcwd()):  # по дефолту стоїть поточна директорія
    lst_p = os.listdir(path)
    lst_dir = []
    lst_file = []
    # проходжу циклом та розділяю файли та папки в два різних списка
    for i in lst_p:
        if os.path.isdir(f'{path}/{i}'):
            lst_dir.append(i)
        else:
            lst_file.append(i)
    # роздруковую
    print(*lst_dir, sep= '|')
    print(*lst_file, sep= ', ')
    print(f"files: {len(lst_file)}, directiry: {len(lst_dir)}")

print_file_dir()
# print_file_dir('C:\\Windows')


# не зовсім зрозумів по завданню як саме роздрукувати файли та папки, тому я папки окремо розрукував, та розділив "|"
# а файли окремо, та нижче розрукував кількість
# в завданні було роздрукувати файли і папки із поточної директоріїї, але я ще зробив можливість роздрукувати
# із іньшої директорії

