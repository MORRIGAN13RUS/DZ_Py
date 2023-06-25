# Пользователь вводит строку текста.
# Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.

s = input("Введите строку текста: ")

def f1 (s):
    s = s.replace(' ','')
    my_set = set(s)
    my_dict = dict()
    for i in my_set:
        count = 0
        for j in s:
            if i==j:
                count +=1
        my_dict[i]=count
    print (my_dict)

def f2 (s):
    s = s.replace(' ','')
    my_set = set(s)
    my_dict = dict()
    for i in my_set:
        count = s.count(i)      
        my_dict[i]=count
    print (my_dict)

f1(s)
f2(s)

