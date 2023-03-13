import random


def monty_hall_no_changing_choice(experiments_number):
    """Подсчет винрейта из n опытов, если не менять дверь в парадоксе Монти-Холла."""
    m = 0                   # количество благоприятных исходов (выигрыши)
    n = experiments_number  # количество опытов; можно увеличить, так будет видно лучше
    
    # исследование
    for i in range(n):
        luckily_door_idx = random.randint(0, 2)       # номер выигрышной двери
        first_chosen_door_idx = random.randint(0, 2)  # номер выбранной двери

        # при не смене выбора, если изначально угадали, то выиграли
        m = m + 1 if luckily_door_idx == first_chosen_door_idx else m

    # возврат результатов
    return float(m) / n


def monty_hall_with_changing_choice(experiments_number):
    """Подсчет винрейта из n опытов, если поменять дверь в парадоксе Монти-Холла."""
    m = 0                   # количество благоприятных исходов (выигрыши)
    n = experiments_number  # количество опытов; можно увеличить, так будет видно лучше
    
    # исследование
    for i in range(n):
        luckily_door_idx = random.randint(0, 2)       # номер выигрышной двери
        first_chosen_door_idx = random.randint(0, 2)  # номер выбранной двери

        # при смене выбора, если изначально не угадали, то выиграли
        m = m if luckily_door_idx == first_chosen_door_idx else m + 1

    # возврат результатов
    return float(m) / n


def main():
    print(' Из 10 опытов')
    print('Не меняя выбора:', monty_hall_no_changing_choice(10))
    print('Меняя выбор:    ', monty_hall_with_changing_choice(10))
    print()

    print(' Из 100 опытов')
    print('Не меняя выбора:', monty_hall_no_changing_choice(100))
    print('Меняя выбор:    ', monty_hall_with_changing_choice(100))
    print()
    
    print(' Из 1000 опытов')
    print('Не меняя выбора:', monty_hall_no_changing_choice(1000))
    print('Меняя выбор:    ', monty_hall_with_changing_choice(1000))

if __name__ == '__main__':
    main()

