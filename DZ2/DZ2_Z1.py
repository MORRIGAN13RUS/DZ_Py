# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата

number1 = int(input('Введите десятичное целое число: '))
number2 = ''
h = "0123456789abcdef"
 
print(hex(number1))
if number1 == 0:
    print('0')
else:
    while number1 > 0:
        number2 = h[number1 % 16] + number2
        number1 = number1 // 16
    print('0x', number2, sep='')