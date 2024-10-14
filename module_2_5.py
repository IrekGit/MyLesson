# Напишите функцию get_matrix с тремя параметрами n, m и value,
# которая будет создавать матрицу(вложенный список) размерами n строк и m столбцов,
# заполненную значениями value и возвращать эту матрицу в качестве результата работы.

def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([value] * m)
    return(matrix)

my_matrix_1 = get_matrix(2,3,4)
my_matrix_2 = get_matrix(3,2,1)
print(my_matrix_1)
print(my_matrix_2)