import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)
    return len(all_data)

if __name__ == '__main__':
    # Файлы должны находиться в одной папке с этим скриптом
    # Названия файлов в формате "file 1.txt", "file 2.txt", ...
    filenames = [f'file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    print("Запускаем линейный вызов функции считывания строк в 4-х файлах")
    start_time = time.time()
    total_lines_linear = 0
    for filename in filenames:
        total_lines_linear += read_info(filename) # считаем количество прочитанных строк
    linear_time = time.time() - start_time # фиксируем время работы функции линейного вызова
    print(f"Линейный вызов: {linear_time:.3f} секунд")
    print(f"Всего строк прочитано (линейный): {total_lines_linear}")
    print()
    time.sleep(1)

    # Многопроцессный вызов
    print("Запускаем многопроцессный вызов функции считывания тех же строк в 4-х файлах")
    start_time = time.time()
    with Pool() as pool:
        total_lines_parallel = sum(pool.map(read_info, filenames))
    parallel_time = time.time() - start_time # фиксируем время работы функции многопроцессного вызова
    print(f"Многопроцессный вызов: {parallel_time:.3f} секунд")
    print(f"Всего строк прочитано (многопроцессный): {total_lines_parallel}")
    print()
    time.sleep(1)

    # Разница во времени
    time_difference = linear_time - parallel_time
    print(f"{time_difference:.3f} секунд составила разница во времени подсчета {total_lines_parallel} строк"
          f" последовательным и параллельным методами")