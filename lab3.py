def l3n1():
    n = int(input("Введите количество слов: "))
    result = ""
    for i in range(n):
        word = input("Введите слово: ")
        result += word + " "
    print(result)
l3n1()


def l3n2():
    result = ""
    while True:
        word = input("Введите слово: ")
        if word == "stop":
            break
        result += word + " "
    print(result)
l3n2()


def l3n3():
    result = ""
    while True:
        word = input("Введите слово: ")
        if word == "stop":
            break
        if "ф" in word:
            print("Ого! Это редкое слово!")
        else:
            print("Эх, это не очень редкое слово...")
l3n3()

def l3n4():
    import random

    print("Игра 'Математика для детей'")

    pravilbno = 0
    nepravilbno = 0

    while nepravilbno < 3:
        a = random.randint(1, 10) # randint возвращает случайное число из определенного диапазона
        b = random.randint(1, 10)
        primer = f"{a} + {b} = "
        user_answer = input(primer)
        if int(user_answer) == a + b:
            print("Правильно!")
            pravilbno += 1
        else:
            print("Ответ неверный")
            nepravilbno += 1

    print(f"Игра окончена. Правильных ответов: {pravilbno}")
l3n4()