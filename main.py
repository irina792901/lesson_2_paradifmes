# Императивный код для нахождения суммы чисел до n
# def sum_up_to_n(n):
#     result = 0
#     for i in range(1, n + 1):
#         result += i
#     return result
#
#
# # -- Декларативный запрос для выборки имен и возрастов
# # SELECT name, age FROM users WHERE age > 25;
#
# # Декларативный код для нахождения суммы чисел до n с использованием функционального стиля
# def sum_up_to_n_declarative(n):
#     return sum(range(1, n + 1))

# Напишите программу, которая находит сумму всех четных чисел от 1 до 100
# с использованием императивного программирования (цикла).

# sum = 0
#
# for num in range(1, 101):
#     if num % 2 == 0:
#         sum += num
#
# print("Сумма равна : ", sum)
#
# # Напишите программу, которая находит сумму всех четных чисел от 1 до 100
# # с использованием декларативного программирования (цикла).
# even_numbers = [num for num in range(1, 101) if num % 2 == 0]
#
# sum_of_even_numbers = sum(even_numbers)
# print("Sum :", sum_of_even_numbers)

# Дан список чисел.
# Ваша задача - найти наибольшую возрастающую
# подпоследовательность в этом списке.

#
# def find_lis(numbers):
#     lis_lengths = [1] * len(numbers)
#
#     for i in range(1, len(numbers)):
#         for j in range(i):
#             if numbers[i] > numbers[j]:
#                 lis_lengths[i] = max(lis_lengths[i], lis_lengths[j] + 1)
#
#     max_length = max(lis_lengths)
#
#     lis = []
#     indx = lis_lengths.index(max_length)
#     lis.append(numbers[indx])
#     for i in range(indx - 1, -1, -1):
#         if numbers[i] < numbers[indx] and lis_lengths[i] == lis_lengths[indx] - 1:
#             lis.insert(0, numbers[i])
#             indx = i
#
#     return lis
#
#
numbers = [3, 4, -1, 0, 6, 2, 3]
#
# lis = find_lis(numbers)
#
# print(lis)

# start = 0
# number_up = []
#
# for i in range(0, len(numbers) - 1):
#     if numbers[i] < numbers[i + 1]:
#         stop = i + 1
#     else:
#         number_up.append(numbers[start:stop + 1])
#         start = i + 1
#
# number_up.append(numbers[start:stop + 1])
#
# max_len = len(number_up[0])
# max_i = 0
# for i in range(len(number_up)):
#     if len(number_up[i]) > max_len:
#         max_i = i
# print(number_up[max_i])
#
#






numbers = [3, 4, -1, 0, 6, 2, 3]

# Инициализация переменных
start = 0  # Индекс начала текущей подпоследовательности
number_up = []  # Список для хранения всех подпоследовательностей
stop = 0  # Индекс конца текущей подпоследовательности

# Проход по списку чисел
for i in range(0, len(numbers) - 1):
    if numbers[i] < numbers[i + 1]:  # Если текущее число меньше следующего
        stop = i + 1  # Увеличиваем индекс конца текущей подпоследовательности
    else:
        # Добавляем текущую подпоследовательность в список
        number_up.append(numbers[start:stop + 1])
        start = i + 1  # Обновляем индекс начала следующей подпоследовательности
        stop = i + 1

# Добавляем последнюю подпоследовательность в список
number_up.append(numbers[start:stop + 1])

max_len = len(number_up[0])  # Инициализация максимальной длины подпоследовательности
max_i = 0
# Проход по всем подпоследовательностям
for i in range(len(number_up)):
    if len(number_up[i]) > max_len:  # Если текущая подпоследовательность длиннее максимальной
        max_len = len(number_up[i])  # Обновляем максимальную длину
        max_i = i  # Запоминаем индекс текущей максимальной подпоследовательности

# Выводим на экран наибольшую подпоследовательность
print(number_up[max_i])

