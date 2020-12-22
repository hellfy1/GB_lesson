# task 1

master = [11, True, (1, 2), "hello", {12: 24, 15: 26}, {17, 18, 19}]

def typeOf(list):
    i = 0
    while i < len(list):
        print(type(list[i]))
        i += 1

typeOf(master)

# task 2

def numberList():
    inputList = []
    while True:
        inputW = input("Введите элемент списка. Если хотите закончить ввод введите STOP ")
        if inputW != "STOP":
            inputList.append(inputW)
        else:
            for i, el in enumerate(inputList):
                if i % 2 == 0 and i != len(inputList) - 1:
                    inputList[i], inputList[i + 1] = inputList[i + 1], inputList[i]
            print(inputList)
            break

numberList()

# task 3

def get_months():
    mDict = {
        "1":  "Зима",
        "2":  "Зима",
        "3":  "Весна",
        "4":  "Весна",
        "5":  "Весна",
        "6":  "Лето",
        "7":  "Лето",
        "8":  "Лето",
        "9":  "Осень",
        "10": "Осень",
        "11": "Осень",
        "12": "Зима",
    }

    user_input = input("Введите число месяца ")
    print(f"Этот месяц относится к поре года: {mDict[user_input]}")

get_months()

# task 4

def split_man():
    user_input = input("Введите строки через пробел ")
    list_w = user_input.split()
    for i, el in enumerate(list_w):
        print(i, el)

split_man()

#task 5

def sort_list():
    input_list = []
    while True:
        input_w = input("Введите рейтинговую отметку. Если хотите закончить ввод введите STOP ")
        if input_w != "STOP":
            input_list.append(int(input_w))
        else:
            print(sorted(input_list, reverse=True))
            break

sort_list()

#task 6

def product():
    i = 1
    product_list = []
    anal = {}
    while True:
        room = i
        name = input("Введите название товара: ")
        cost = input("Введите цену товара ")
        number = input("Введите количество товара ")
        unit = input("Введите единицу измерения товара ")
        product_unit = (room, {"Название": name, "Цена": cost, "Количество": number, "ед.": unit})
        product_list.append(product_unit)
        i += 1
        confirm = input("Если хотите внести еще один товар напишите 'да'."
                        "Если же нужно остановиться напишите любой символ ")
        if confirm != 'да':
            print(product_list)
            break
    for opt in "Название", "Цена", "Количество", "ед.":
        anal[opt] = [p[1][opt] for p in product_list]
    print(anal)

product()
