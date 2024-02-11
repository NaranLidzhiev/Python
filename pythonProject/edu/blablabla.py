def birth_day(bd):
    while True:
        name = input("Enter a name ")
        if name == "":
            break

        if name in bd:
            print(name + " Родился/ась", bd[name])
        else:
            print("Ты не записал днюху")
            print("Записывай блять")
            bd[name] = input()
            print("Теперь не забудем")


birthdays = {'Алиса': 'Апр 1', 'Боб': 'Дек 12', 'Кэрол': 'Мар 4'}

birth_day(birthdays)