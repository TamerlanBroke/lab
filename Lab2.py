def l2n1():
    pas1 = input('Введите пароль:')

    numeric = False
    upper = False
    lower = False
    spec = False

    for char in pas1:
        if char.isnumeric():
            numeric = True
        elif char.islower():
            lower = True
        elif char.isupper():
            upper = True
        elif char in "@#$%&?!":
            spec = True
    if len(pas1) >= 6 and numeric and upper and lower and spec:
        print('Пароль подходит')
    else:
        print('Усложните пароль')
    pas2 = input('Введите пароль:')
    while pas1 != pas2:
        print('Пароли не совпадают')
        pas2 = input('Попробуйте снова')
    print('Пароли совпадают')


def l2n2():
    des = int(input('Введите номер вашего места вагоне:'))
    print()
    if des >= 36:
        print('Ваше место - боковое.')
    elif des % 2:
        print('Ваше места в купе внизу')
    else:
        print('Ваше место в купе наверху ')


l2n2()


def l2n3():
    year = int(input('Введите год:'))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print('год', year, 'високосным')
    else:
        print('год', year, 'невисокосный')


l2n3()


def l2n4():
    color1 = input("Введите первый цвет: ")
    color2 = input("Введите второй цвет: ")
    if (color1 == "красный" or color2 == "красный") and (color1 == "синий" or color2 == "синий"):
        print("фиолетовый")
    elif (color1 == "красный" or color2 == "красный") and (color1 == "желтый" or color2 == "желтый"):
        print("оранжевый")
    elif (color1 == "синий" or color2 == "синий") and (color1 == "желтый" or color2 == "желтый"):
        print("зеленый")
    elif color1 == color2 and (color1 == "синий" or color1 == "красный" or color1 == "желтый"):
        print(color1)
    else:
        print("Ошибка в выборе цветов")


l2n4()
