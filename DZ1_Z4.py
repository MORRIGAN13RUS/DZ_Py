# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
num= int(input("Введите число меньше 100 000 и больше 0: "))
tmp=0
while num <1 or num > 100000:
    num= int(input("Вы ввели неправильное число. Введите число заново: "))
for i in range(2,num):
    if num % i == 0:
        tmp=1
        break
if tmp==1:
    print("Данное число является составным")
else: 
    print("Данное число является простым")

