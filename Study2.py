# # Пример структурного программирования
#
# # Задача: Найти сумму всех чисел от 1 до N.
#
# # Ввод данных
# n = int(input("Введите число N: "))
#
# # Инициализация переменной для хранения суммы
# sum_of_numbers = 0
#
# # Вычисление суммы
# for i in range(1, n + 1):
#     sum_of_numbers += i
#
# # Вывод результата
# print(f"Сумма всех чисел от 1 до {n} равна {sum_of_numbers}")
#
#
# # Пример процедурного программирования
#
# # Задача: Найти сумму всех чисел от 1 до N.
#
# # Функция для вычисления суммы чисел
# def calculate_sum(n):
#     sum_of_numbers = 0
#     for i in range(1, n + 1):
#         sum_of_numbers += i
#     return sum_of_numbers
#
# # Функция для вывода результата
# def display_result(n, result):
#     print(f"Сумма всех чисел от 1 до {n} равна {result}")
#
# # Ввод данных
# n = int(input("Введите число N: "))
#
# # Вызов функций
# total_sum = calculate_sum(n)
# display_result(n, total_sum)
#
#
# Пример структурного программирования

# Входные данные: список студентов с оценками
# students = [
#     {"имя": "Анна", "оценки": [90, 85, 88]},
#     {"имя": "Петр", "оценки": [78, 92, 88]},
#     {"имя": "Мария", "оценки": [85, 87, 92]},
# ]
#
# # Инициализация переменных для суммы и среднего значения
# total_score = 0
# total_students = len(students)
#
# # Вычисление суммы оценок
# for student in students:
#     total_score += sum(student["оценки"])
#
# # Вычисление среднего балла
# average_score = total_score / (total_students * len(students[0]["оценки"]))
#
# # Вывод результата
# print(f"Средний балл студентов: {average_score:.2f}")
#

# Пример процедурного программирования

# Функция для вычисления среднего балла студента
def calculate_average(scores):
    return sum(scores) / len(scores)

# Функция для вычисления среднего балла всех студентов
def calculate_class_average(students):
    total_score = 0
    total_students = len(students)

    for student in students:
        total_score += calculate_average(student["оценки"])

    return total_score / total_students

# Входные данные: список студентов с оценками
students = [
    {"имя": "Анна", "оценки": [90, 85, 88]},
    {"имя": "Петр", "оценки": [78, 92, 88]},
    {"имя": "Мария", "оценки": [85, 87, 92]},
]

# Вычисление среднего балла
average_score = calculate_class_average(students)

# Вывод результата
print(f"Средний балл студентов: {average_score:.2f}")