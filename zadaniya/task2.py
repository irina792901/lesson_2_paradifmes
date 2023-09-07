# Процедурное программирование
# Входные данные: список чисел
numbers = [12, 45, 78, 90, 56, 23, 67, 89]

# Функция для вычисления среднего значения
def average(numbers):
    summ = sum(numbers)
    count = len(numbers)

    if count == 0:
        return None

    average = summ / count
    return average

# Вычисление среднего значения с использованием функции
aver = average(numbers)

print(aver)
