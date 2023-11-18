
def game_core_v3(number: int = 1) -> int:
    """Угадаем число методом бинарного поиска.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
    int: Число попыток
    """
    left, right = 1, 100
    count = 0
    while True:
        count += 1
        predict = (left + right) // 2
        if number == predict:
            return count
        if number > predict:
            left = predict
        elif number < predict:
            right = predict