import numpy as np

number = np.random.randint(1, 101)
"""создание и сортировка списка из диапазона загаданного числа 
по возрастанию для функции бинарного поиска
"""
num = []
for i in range(1, 101):
    num.append(i)
num.sort()
print("Загадано число от 1 до 100")


def game_core_v3(num1, number1):      # функция отгадывающая число
    mid = len(num1) // 2
    low = 0
    high = len(num1) - 1
    count = 0

    while num1[mid] != number1 and low <= high:     # алгоритм бинарного поиска
        if number1 > num1[mid]:
            low = mid + 1
            count += 1
        else:
            high = mid - 1
            count += 1
        mid = (low + high) // 2
    print("загаданное число =", mid+1, "отгаданное за", count, "попыток")


# запуск поиска
game_core_v3(num, number)