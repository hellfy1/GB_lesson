# task 1

a = int(input("Введите первое число "))
b = int(input("Введите второе число "))
def res(a, b):
    if a == 0 or b == 0:
        return print("Деление на ноль недопустимо")
    else:
        return print(a / b)

res(a, b)

# task 2

name = input("Введите ваше имя ")
surname = input("Введите вашу фамилию ")
birth_year = input("Введите год вашего рождения ")
city = input("Введите город вашего проживания ")
email = input("Введите ваш email адресс ")
phone = input("Введите ваш номер телефона ")

def user_info(*args):
    res_str = ""
    for i in args:
        res_str += i + " "
    print(res_str)

user_info(name, surname, birth_year, city, email, phone)

# task 3

def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.remove(min(my_list))
    return my_list

print(my_func(8,3,4))

#task 4

variant 1

def my_func(a, b):
    return a ** b

print(my_func(7, -2))

#variant 2

def my_func(a, b):
    x = a
    for i in range((-b) - 1):
        a *= x
    a = 1 / a
    print(a)

my_func(8, -3)

# task 5

def action_sum():
    total_sum    = 0
    break_symbol = "S"
    action       = True

    while action:
        user_input = input(f"Введите числа. Если хотите остановиться, введите {break_symbol}: ").split()
        for num in user_input:
            if num == break_symbol:
                action = False
                break
            total_sum += int(num)
        print("Sum: ", total_sum)

action_sum()

# task 6

#Нет, я конечно прошу прощения, но задание максимально интересное.
#Как я понимаю, мы строки изучали, соответственно можно пользоваться встроенными функциями

#С учетом встроенных функций выглядит это конечно кринжово, так как первая функция повторяет встроенную
#Однозначно, можно делать и иначе, чтобы вы поставили мне максимальную оценку я поясню: в первой функции, которая должна
#приводить к строке, можно просто по индексу аппером увеличить первую букву (но это теряет смысл, ибо есть capitalize)
#Так что я не знаю, как правильно нужно было сделать это задание, но вот держите решение
#По факту, первая функция здесь ненужна вообще, это довольно забавно
def int_func(str):
    return str.capitalize()

def in_upper():
    user_input = input("Введите слова через пробел и с маленькой буквы: ").split(" ")
    new_list = [int_func(word) for word in user_input]
    print(" ".join(new_list))

in_upper()
