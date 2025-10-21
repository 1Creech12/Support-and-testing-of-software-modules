import timeit
import cProfile
import pstats
from multiprocessing import Pool


# Задание 1
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


# Задание 2
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# Задание 3
def factorial_partial(start_end):
    start, end = start_end
    result = 1
    for i in range(start, end + 1):
        result *= i
    return result


def factorial_parallel(n, workers=4):
    chunk = n // workers
    ranges = [(i * chunk + 1, (i + 1) * chunk) for i in range(workers - 1)]
    ranges.append(((workers - 1) * chunk + 1, n))
    with Pool(workers) as p:
        parts = p.map(factorial_partial, ranges)
    result = 1
    for j in parts:
        result *= j
    return result


# Функция для измерений
def measure_time(func, n, repeats=5):
    return timeit.timeit(lambda: func(n), number=repeats) / repeats


if __name__ == "__main__":
    numbers = [10, 20, 30, 100, 200]
    print("Тестирование производительности:\n")

    print(f"{'N':<10}{'Рекурсивный':<20}{'Итерационный':<20}")
    for n in numbers:
        t_rec = measure_time(factorial_recursive, n)
        t_it = measure_time(factorial_iterative, n)
        print(f"{n:<10}{t_rec:<20.8f}{t_it:<20.8f}")



    # Дополнительное задание
    print("\nПараллельная версия (n=10000):")
    t_par = measure_time(factorial_parallel, 10000, repeats=3)
    print(f"Среднее время выполнения: {t_par:.8f} сек")
