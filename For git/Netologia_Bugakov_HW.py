def cook_book_complite():  # Можно было сделать фу-цию с аргуметом, где подавалось название файла
    with open("input.txt", "r", encoding="utf-8") as f:  # Но я решил читать из кокретного, удобно для тестов
        cook_book = {}
        line = f.readline()  # считываем строку с названием бюда
        while line:
            dish = line.strip()  # присваиваем переменную и очишаем от пробелов
            ingridients_number = int(f.readline().strip())  # считываем вторую строку(число)
            ingridient_list = []
            for _ in range(ingridients_number):  # цикл по кол-ву ингридиентов
                ingridient_name, quantity, measure = f.readline().strip().split(
                    ' | ')  # считываем строки разделенные знаком
                ingridient_dict = {}  # Создание и заполнение словаря
                ingridient_dict['ingridient_name'] = ingridient_name
                ingridient_dict['quantity'] = int(quantity)
                ingridient_dict['measure'] = measure
                ingridient_list.append(ingridient_dict)
            cook_book[dish] = ingridient_list  # кладем в словарь-меню наше блюдо
            f.readline()  # пропускаем пробельную строку
            line = f.readline()  # снова считываем строку с названием блюда

    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    print('')
    for shop_list_item in shop_list.values():
        print('{ingridient_name} {quantity} {measure}'.format(**shop_list_item))


def create_shop_list():
    person_count = int(input('Введите количество персон: '))
    dishes = input('Введите блюда через запятую: ').split(', ')
    cook_book = cook_book_complite()
    shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
    print_shop_list(shop_list)


create_shop_list()
