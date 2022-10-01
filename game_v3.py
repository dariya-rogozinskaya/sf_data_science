"""Игра угадай число компьютер с компьютером"""
import numpy as np
def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 1
    number_guessed_lesser = 0
    number_guessed_larger = 101
    predict_number = 50

    while predict_number != number:
        count += 1
        # предполагаемое число
        if predict_number < number:
           number_guessed_lesser = predict_number
        else: number_guessed_larger = predict_number
        predict_number = (number_guessed_larger - number_guessed_lesser)//2 + number_guessed_lesser
        print(f"number_guessed_larger {number_guessed_larger}")
        print(f"number_guessed_lesser {number_guessed_lesser}")
        print(f"predict_number {predict_number}")
        print(f"number {number}")
    return count
print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    n=0
    for number in random_array:
        n += 1
        print (f"Занесли число {number}, {n} раз прошёл цикл")
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)