# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён

from random import randint as rnd, choices as chs
from string import ascii_lowercase as asc, digits as dig
import os


def files_gen(ext:str,files:int=42 , min_name:int=6, max_name:int=30, \
      min_bytes:int=256, max_bytes:int=4096) -> None:
    count = 0
    while count < files:
        name = ''.join(chs(asc + dig, k=rnd(min_name,max_name + 1)))
        data = bytes(rnd(0, 255) for _ in range(rnd(min_bytes, max_bytes)))
        if not f'{name}.{ext}' in os.listdir():
            count +=1
            with open(f'{name}.{ext}', 'wb') as f:
                f.write(data)
            


def files_todir_gen(*args) -> None:
    dir = args[-1]
    if not dir in os.listdir():
        os.mkdir(dir)
        os.chdir(dir)
    else:
        os.chdir(dir)
        
    for i in range(0, len(args) - 1, 2):
        files_gen(args[i], args[i + 1])
    os.chdir("..")

if __name__ == '__main__':
    files_todir_gen('txt',3, 'Alfa')
    files_todir_gen('avi', 3, 'Alfa')
    files_todir_gen('jpg', 3, 'Alfa')