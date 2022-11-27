try:
    str_1 = int(input())
    str_2 = int(input())
    division = str_1 / str_2
    print(division)
except ZeroDivisionError:
    print("ошибка ZeroDivisionError")
    print("введите числа заново")
    str_1 = int(input())
    str_2 = int(input())
except ValueError:
    print("были введины буквы")
finally:
    print("операция завершина")

