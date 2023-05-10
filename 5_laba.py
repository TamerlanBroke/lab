def lab5n1():
    list = [1,2,3,4,5]
    a = input("Введите число: ")
    for i in list:
        if int(a) in list:
            print("да")
            break
        else:
            print("нет")
            break


def lab5n2():
    list = ["1","1","2","2","5"]
    for i in range(len(list)-1):
        if list[i] == list[i+1]:
            print("Есть совпадения", list[i])


def lab5n3():
    list = ["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"]
    a = input("Введите колво дней: ")
    print("Ваши выходные дни:",list[7-int(a):])
    print("Оставшиеся дни:",list[:7-int(a)])


def lab5n4():
    k = 0
    list = ["Исхаков","Иванов","Чел","Чел1","Чел2","Чел3","Чел4","Чел5","Чел6","Чел7"]
    list1 = ["Чел8","Чел9","Чел10","Чел11","Чел12","Чел13","Чел14","Чел15","Чел16","Чел17","Чел18"]
    list2 = [list[0],list[1],list1[0],list1[9]]
    print(list)
    print(list1)
    print(list2)
    print(len(list2))
    list2 = tuple(sorted(list2))
    print(list2)
    for i in range(len(list2)):
        if list2[i] == "Иванов":
            k +=1

        else:
            print("Не встречается")
            break
    print("Встречается",k," раз")




lab5n1()
lab5n2()
lab5n3()
lab5n4()

