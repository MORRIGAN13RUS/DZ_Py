#Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. 
#Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла

way = "C:\GB\Python\gile.pdf"

def linc_tuple(l):
    b,c = l.rsplit('.', maxsplit=1)
    x,a = b.rsplit("\\", maxsplit=1)
    return(c,a,x)

print(linc_tuple(way))