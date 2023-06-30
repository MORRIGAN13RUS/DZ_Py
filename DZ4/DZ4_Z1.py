# ДЗ к семинару 4, задание 1
# Напишите функцию для транспонирования матрицы



def transposing_matrix(matrix):
    return list(zip(*matrix))


if __name__ == '__main__':
    my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    my_list_2 = (transposing_matrix(my_list))
    print(*my_list,"\n",*my_list_2, sep="\n")