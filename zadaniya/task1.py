# У вас есть список чисел, и вам нужно вычислить среднее значение этого списка чисел.

# Входные данные: список чисел
numbers = [12, 45, 78, 90, 56, 23, 67, 89]
# Инициализация переменных для суммы и количества чисел
summ = 0
count = 0
# Вычисление суммы чисел и их количества
for number in numbers:
    summ += number
    count += 1
# Вычисление среднего значения
average = summ / count

print(average)
