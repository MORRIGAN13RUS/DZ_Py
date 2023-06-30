#  Задание 8 к семинару 4
# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.


def my_func():
    g_dict = globals()
    print (g_dict)
    for key, value in g_dict.items():
        if not key.startswith('_') and key.endswith('s') and key != 's':
            g_dict[key[:-1]] = value
            g_dict[key] = None


if __name__ == '__main__':
    s = 'строка'
    alfas, alfa = 1, 10
    betas, beta = 2, 10
    deltas, delta = 3, 10
    
    my_func()
    print(s)
    print(f'alfas, alfa = {alfas}, {alfa}')
    print(f'betas, beta = {betas}, {beta}')
    print(f'deltas, delta = {deltas}, {delta}')