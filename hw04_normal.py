__author__ = "Гончаров Всеволод Сергеевич"

import re
import random
import os

runes = list(map(chr, range(ord('a'), ord('z') + 1)))
RUNES = list(map(chr, range(ord('A'), ord('Z') + 1)))
strRunes = ""
strRUNES = ""
for rune in runes:
    strRunes += rune
for rune in RUNES:
    strRUNES += rune

while True:
    print("Введи номер задачи (1-3) или 0 для выхода")
    key = int(input())

    # Задание-1:
    # Вывести символы в нижнем регистре, которые находятся вокруг
    # 1 или более символов в верхнем регистре.
    # Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
    # Решить задачу двумя способами: с помощью re и без.

    if key == 1:

        def find_with_re(line):
            pattern = re.compile('([' + strRunes + ']+)')
            return pattern.findall(line)


        def find_without_re(line):
            answer = []
            this_value = ""
            for rune in line:
                if rune in runes:
                    this_value += rune
                else:
                    if this_value:
                        answer.append(this_value)
                        this_value = ""
            return answer


        line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO' \
               'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK' \
               'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn' \
               'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa' \
               'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete' \
               'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ' \
               'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb' \
               'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC' \
               'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB' \
               'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT' \
               'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu' \
               'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB' \
               'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa' \
               'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ' \
               'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

        print(find_with_re(line))
        print(find_without_re(line))

    # Задание-2:
    # Вывести символы в верхнем регистре, слева от которых находятся
    # два символа в нижнем регистре, а справа - два символа в верхнем регистре.
    # Т.е. из строки
    # "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
    # нужно получить список строк: ['AY', 'NOGI', 'P']
    # Решить задачу двумя способами: с помощью re и без.

    if key == 2:

        def find_with_re(line):
            pattern = re.compile('[' + strRunes + ']{2}([' + strRUNES + ']+)[' + strRUNES + ']{2}')
            return pattern.findall(line)

        def find_without_re(line):
            line_list = []
            if line[:1] in runes:
                get_rune = True
                get_RUNE = False
            else:
                get_RUNE = True
                get_rune = False

            this_value = ""
            for rune in line:
                if rune in runes:
                    if get_rune:
                        this_value += rune
                    else:
                        line_list.append(this_value)
                        this_value = rune
                        get_rune = True
                        get_RUNE = False
                else:
                    if get_RUNE:
                        this_value += rune
                    else:
                        line_list.append(this_value)
                        this_value = rune
                        get_rune = False
                        get_RUNE = True

            valid_line_list = []
            get_two_rune = False
            for item in line_list:
                if item[:1] in runes:
                    get_two_rune = True if len(item) >= 2 else False
                else:
                    if len(item) >= 3 and get_two_rune:
                        valid_line_list.append(item)

            return [item[:-2] for item in valid_line_list]


        line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm' \
             'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV' \
             'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA' \
             'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV' \
             'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW' \
             'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC' \
             'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR' \
             'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm' \
             'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn' \
             'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS' \
             'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf' \
             'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH' \
             'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN' \
             'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ' \
             'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

        print(find_with_re(line_2))
        print(find_without_re(line_2))

    # Задание-3:
    # Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
    # произвольными целыми цифрами, в результате в файле должно быть
    # 2500-значное произвольное число.
    # Найдите и выведите самую длинную последовательность одинаковых цифр
    # в вышезаполненном файле.

    elif key == 3:

        def file_write():
            number_list = [random.randint(0, 9) for _ in range(2500)]
            path = os.path.join('data', 'numbers.txt')
            with open(path, 'w', encoding="UTF-8") as f:
                for number in number_list:
                    f.write(str(number))

        def file_read():
            path = os.path.join('data', 'numbers.txt')
            with open(path, 'r', encoding="UTF-8") as f:
                first_rune = True
                top_value = ""
                for rune in f.readline():
                    if first_rune:
                        this_value = rune
                        first_rune = False
                    else:
                        if rune == this_value[:1]:
                            this_value += rune
                        else:
                            if len(top_value) < len(this_value):
                                top_value = this_value
                            this_value = rune
            return top_value


        file_write()
        print("Файл записан")
        print(file_read())

    elif key == 0:
        break
    else:
        print("Ввел что-то не то, попробуй ещё раз")
