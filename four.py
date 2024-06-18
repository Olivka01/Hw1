from random import randint

def guess_number(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    low = 1    # Переменная для определения диапазона
    high = 100 # Переменная для определения диапазона
    count = 0  # Счетчик количества попыток

    while low <= high:
        count += 1  # Счет попыток
        mid = (low + high) // 2  # Среднее значение диапазона

        if mid == number:
            return count
        elif mid < number:
            low = mid + 1
        else:
            high = mid - 1

target_number = randint(1, 100)  # Задуманное число
print(guess_number(target_number))  # Запуск функции
