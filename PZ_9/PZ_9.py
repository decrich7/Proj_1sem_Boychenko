def create_dict(string):
    list_from_str = string.split()
    dict_from_list = {f'{list_from_str[0]}': list_from_str[1:6], f'{list_from_str[6]}': list_from_str[7:]}
    return f'Максимальное число продаж апельсинов: {max(dict_from_list["апельсины"])}\n' \
           f'Максимальное число продаж яблок: {max(dict_from_list["яблоки"])}'


print(create_dict('апельсины 45 991 63 100 12 яблоки 13 47 26 0 16'))