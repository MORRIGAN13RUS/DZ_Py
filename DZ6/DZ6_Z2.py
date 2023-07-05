# Известно, что на доске 8×8 
# можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана 
# расстановка 8 ферзей на доске, определите, есть ли среди них пара 
# бьющих друг друга. Программа получает на вход восемь пар чисел, каждое 
# число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга 
# верните истину, а если бьют - ложь.
# Напишите функцию в шахматный модуль. Используйте генератор случайных 
# чисел для случайной расстановки ферзей в задаче выше. Проверяйте 
# различный случайные варианты и выведите 4 успешных расстановки.


from random import randint as rnd


def check_8_queens(coordinates : list) -> bool:
    x, y = zip(*coordinates)
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                return False
    return True


def input_coordinates() -> list:
    return [list(map(int, input(f'Координаты {i + 1} ферзя (x.y): ').split("."))) 
            for i in range(8)]


def random_coordinates() -> list:
    coordinates = [[rnd(1, 9), rnd(1, 9)]]
    while len(coordinates) < 8:
        tmp = [rnd(1, 9), rnd(1, 9)]
        flag = True
        for i in range(len(coordinates)):
            if tmp == coordinates[i]:
                flag = False
        if flag:
            coordinates.append(tmp)
    return coordinates

def random_True_coordinates() -> list:
    return list(zip(get_list(),get_list()))

def get_list ()  -> list:
    l = [rnd(1,9)]
    while len(l) < 8:
        tmp = rnd(1, 9)
        flag = True
        for i in range(len(l)):
            if tmp == l[i]:
                flag = False
        if flag:
            l.append(tmp)
    return l


if __name__ == '__main__':
    
    count = 0
    for _ in range (10000):
        if count == 4:
            break
        list_tmp = random_True_coordinates()
        if check_8_queens(list_tmp):
            count +=1
            print(list_tmp)

