__author__ = "Гончаров Всеволод Сергеевич"

import random

while True:
    print("Введи номер задачи (1-3) или 0 для выхода")
    key = int(input())

    # Все задачи текущего блока решите с помощью генераторов списков!

    # Задание-1:
    # Дан список, заполненный произвольными целыми числами.
    # Получить новый список, элементы которого будут
    # квадратами элементов исходного списка
    # [1, 2, 4, 0] --> [1, 4, 16, 0]

    if key == 1:

        first_list = [random.randint(-10, 10) for _ in range(10)]
        second_list = [item ** 2 for item in first_list]
        print("Было так {}\nСтало так{}".format(first_list, second_list))

    # Задание-2:
    # Даны два списка фруктов.
    # Получить список фруктов, присутствующих в обоих исходных списках.

    elif key == 2:

        first_list = []
        second_list = []
        third_list = []
        print("Сейчас мы будем генерировать 2 списка фруктов")
        for i in range(2):
            print("Сколько элементов будет в {} списке?".format(i+1))
            list_len = int(input())
            for j in range(list_len):
                print("Добавь {} фрукт для {} списка".format(j+1, i+1))
                if i == 0:
                    first_list.append(input())
                else:
                    second_list.append(input())

        third_list = [item for item in first_list if item in second_list]
        print(third_list)

    # Задание-3:
    # Дан список, заполненный произвольными числами.
    # Получить список из элементов исходного, удовлетворяющих следующим условиям:
    # + Элемент кратен 3
    # + Элемент положительный
    # + Элемент не кратен 4

    elif key == 3:

        first_list = [random.randint(-10, 10) for _ in range(10)]

        second_list = [item for item in first_list if item % 3 == 0 and item != 0]
        third_list = [item for item in first_list if item > 0]
        fourth_list = [item for item in first_list if item % 4 != 0]

        print("Оригинал: {}\nЭлементы кратные 3: {}\nПоложительные элементы: {}\nЭлементы не кратные 4: {}".
              format(first_list, second_list, third_list, fourth_list))

    elif key == 0:
        break
    else:
        print("Ввел что-то не то, попробуй ещё раз")
