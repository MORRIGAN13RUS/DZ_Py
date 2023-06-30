# ДЗ к семинару 4, задание 1
# Напишите функцию для транспонирования матрицы


def transposing_matrix(matrix):
    return list(zip(*matrix))


if __name__ == '__main__':
    print(transposing_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))