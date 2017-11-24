import os


def find_path():
    """Находим путь до необходимых файлов
    Возвращает путь"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'migrations')


def find_all_files():
    """Находим папку Migrations и получаем список файлов.
    Возвращает список sql файлов."""
    path_to_files = find_path()
    sql_files = list(filter(lambda x: x.endswith('.sql'), os.listdir(path_to_files)))
    return sql_files


def get_string():
    """Получаем строку для поиска.
    Возвращает введенную пользователем строку"""
    return input('Введите строку для поиска:')


def find_string(user_file, user_string):
    """Работа с файлом. Чтение и поиск строки.
    Возвращает имя файла"""

    # Получаем содержимое файла
    with open(os.path.join(find_path(), user_file)) as f:
        file_content = f.read()

    # Если в файле есть данная строка - возвращаем имя файла
    if user_string.lower() in file_content.lower():
        return user_file


def print_result(found_files):
    """Вывод найденных файлов на печать"""
    print()
    for item in found_files:
        print(item)
    print('\nКоличество найденных файлов: {}\nДля завершения поиска - CTRL + C'.format(len(found_files)))
    print('-'*50, end='\n\n')


def find_matching_files(files_list):
    """Ищем все файлы с данной строкой"""

    # Получаем строку пользователя и ищем ее в файлах
    user_input = get_string()
    suitable_files = []
    for file in files_list:
        result = find_string(file, user_input)

        # Если процедура поиска вернула имя файла - добавляем в список совпадений
        if result is not None:
            suitable_files.append(result)

    # Печать найденных результатов
    print_result(suitable_files)

    # Продолжение поиска среди найденных файлов
    find_matching_files(suitable_files)


if __name__ == '__main__':

    # Получение списка файлов
    list_files = find_all_files()

    # Инициализация поиска среди файлов
    find_matching_files(list_files)
