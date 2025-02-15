"""Угадай число"""

import numpy as np

def random_predict(number:int=1) -> int:
    # рандомно угадывает число
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) #предполагаемое число
        # предпологаемое число 
        
        if number == predict_number:
            break 
    return (count)
# print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) ->int:
    
    count_ls=[]
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000)) #массив из 1000 рандомных чисел
    
    for number in random_array:
        count_ls.append(random_predict(number)) 
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


if __name__=='__main__':
# RUN
    score_game(random_predict)