"""Угадай число"""


import numpy as np


def game_core_v3(number: int = 1) -> int:
    # Счетчик попыток угадывания числа
    # Зададим первоначальные параметры макс, мин, поставим счетчик на 0 и
    # зададим первое предполагаемое число
    max_v = 100
    min_v = 1
    count = 0
    predict = int(np.mean(max_v + min_v))
    
    while number != predict:
        # Цикл будет работать, пока мы не угадаем число
        count += 1
        if predict > number:
            max_v = predict
            predict = (max_v + min_v) // 2
        elif predict < number:
            min_v = predict
            predict = (max_v + min_v) // 2
    return count
    # Возвращаем количество затраченных попыток на угадывание

def score_game(game_core_v3) -> int:
    # Посчитаем за сколько в среднем за 10000 раз угадывает алгоритм
    count_ls= []
    # Создадим пустой список для результатов
    # np.random.seed(1) #Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1,101, size = (10000))
    
    for number in random_array:
        count_ls.append(game_core_v3(number))
    
    score = int(np.mean(count_ls))
    return print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")


if __name__=='__main__':
    
    score_game(game_core_v3)

