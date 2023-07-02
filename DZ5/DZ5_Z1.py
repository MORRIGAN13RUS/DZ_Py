#Создайте функцию генератор чисел Фибоначчи


def fib(n):
    num1 = 0
    num2 = 1
    for i in range(n+1):
        if i==0:
            yield "0"
        elif i==1:
            yield "1"
        else:        
            num = num1+num2
            num1=num2
            num2=num
            yield num


for i, num in enumerate(fib (14)):
    print (f"{num}  ", end="")
