import json

def read_cook_book(file_name):
    with open(file_name) as f:
        cook_book = json.load(f)
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = read_cook_book('dishes.json')
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
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))

def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')

    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)

create_shop_list()

