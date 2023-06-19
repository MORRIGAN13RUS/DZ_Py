# Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.
number = int(input("Сколько рядов  елки? "))
plus = 1
space = number - 1
for i in range(1, number+1):
    print(' ' * space, end='')
    space -= 1
    print('+' * plus)
    plus +=2