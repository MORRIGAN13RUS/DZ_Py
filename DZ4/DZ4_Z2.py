# ДЗ к семинару 4, задание 2
# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.


def my_function(**kwargs):
    my_dict = dict()
    for key, val in kwargs.items():
        if isinstance(val, (list, dict, set, bytearray)):
            my_dict[str(val)] = key
        else:
            my_dict[val] = key
    return my_dict


if __name__ == '__main__':
    dict_my = my_function(int_=5, float_=0.1, str_="строка", bool_=True, tuple_=(1, 2, 3,), list_=[4, 5, 6], set_={7, 8, 9})
    print(dict_my)