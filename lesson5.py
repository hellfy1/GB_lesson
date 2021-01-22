# task 1

my_file = open("1task.txt", "w")

while True:
    input_data = input("Введите данные ")
    if input_data:
        input_data = input_data + "\n"
        my_file.writelines(input_data)
    else:
        break

# task 2

with open("2task.txt", "r") as file:
    row_content = file.readlines()
    count_content = []
    for line in row_content:
        line = line.split()
        count_content.append(len(line))

    print(f'Количество строк в файле: {len(row_content)}, количество букв в каждой строке соответственно: {count_content}')

# task 3

with open("3task.txt", "r") as file:
    content = file.readlines()
    total = []
    s = []
    for item in content:
        item = item.split()
        total.append(int(item[1]))
        if int(item[1]) < 20000:
            s.append(item[0])
    print(f"Сотрудники с окладом менее 20000 рублей: {s}, средний доход сотрудников составляет: {sum(total) / len(total)}")

# task 4

with open("4task.txt", "r") as file:
    translate = {"One": "odin", "Two": "dva", "Three": "tri", "Four": "chetyre"}
    content = file.readlines()
    w_content = []
    for item in content:
        item = item.split()
        if item[0] in translate:
            w_content.append(translate[item[0]] + " - " + item[2])

with open("4task-write.txt", "w") as file2:
    for item in w_content:
        file2.write(item + "\n")


# task 5

def total():
    with open('5task.txt', 'w') as file:
        line = input('Введите цифры через пробел \n')
        file.writelines(line)
        my_numb = line.split()

        print(sum(map(int, my_numb)))
total()

# task 6

sub = {}
with open("6task.txt", encoding='utf-8') as file:
    lines = file.readlines()

for line in lines:
    data = line.replace('(', ' ').split()

    sub[data[0][:-1]] = sum(
        int(i) for i in data if i.isdigit()
    )

print(sub)

# task 7

from json import dumps

results = [{}, {}]

with open("7task.txt", encoding='utf-8') as file:
    lines = file.readlines()

for line in lines:
    name, _, proceeds, expenses = line.split()
    results[0][name] = int(proceeds) - int(expenses)

results[1]['average_profit'] = round(
    sum(
        profit for _, profit in results[0].items() if profit > 0
    ) / len(results[0])
)

with open("7task.json", "w", encoding='utf-8') as file2:
    file2.write(dumps(results))

