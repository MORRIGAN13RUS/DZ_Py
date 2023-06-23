# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

from math import gcd
from fractions import Fraction

rac_num_1 = input('Введите первую дробь вида a/b: ')
list_rac_num_1 = rac_num_1.split('/')
a_1 = int(list_rac_num_1[0])
b_1=int(list_rac_num_1[1])

rac_num_2 = input('Введите вторую дробь вида a/b: ')
list_rac_num_2 = rac_num_2.split('/')
a_2 = int(list_rac_num_2[0])
b_2 = int(list_rac_num_2[1])

def sum_rac_num (a_1 , b_1, a_2, b_2):
    res1 = a_1 * b_2 + a_2 * b_1
    res2 = b_1 * b_2
    n = gcd(res1, res2)
    print(rac_num_1, '+', rac_num_2, '=', res1//n, '/', res2//n, sep='')

def mult_rac_num (a_1 , b_1, a_2, b_2):
    res1 = a_1 * a_2
    res2 = b_1 * b_2
    n = gcd(res1, res2)
    print(rac_num_1, '*', rac_num_2, '=', res1//n, '/', res2//n, sep='')

def fraction_check (rac_num_1,rac_num_2):
    x = Fraction(rac_num_1)
    y = Fraction(rac_num_2)
    print('С помощью модуля fraction:', x + y, x * y)
 
sum_rac_num (a_1 , b_1, a_2, b_2)
mult_rac_num (a_1 , b_1, a_2, b_2)
fraction_check (rac_num_1,rac_num_2)