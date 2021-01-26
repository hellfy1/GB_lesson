# task 1

class Data:
    def __init__(self, day_month_year):
        # self.day = day
        # self.month = month
        # self.year = year
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'All right'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('11 - 1 - 2001')
print(today)
print(Data.valid(11, 11, 2022))
print(today.valid(11, 13, 2011))
print(Data.extract('11 - 11 - 2011'))
print(today.extract('11 - 11 - 2020'))
print(Data.valid(1, 11, 2000))


# task 2

class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль недопустимо")


div = DivisionByNull(10, 100)
print(DivisionByNull.divide_by_null(10, 0))
print(DivisionByNull.divide_by_null(10, 0.1))
print(div.divide_by_null(100, 0))

# task 3

class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        # self.my_list = [int(i) for i in input('Введите значения через пробел ').split()]
        # val = int(input('Введите значения и нажимайте Enter - '))
        # self.my_list.append(val)
        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение - строка и булево")
                y_or_n = input(f'Попробовать еще раз? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'


try_except = Error(1)
print(try_except.my_input())

# task 4

class Storage:
    pass


class OfficeEquipment:
    vat = 0.13
    added_value = 2.0
    retail_rate = 1.3

    def __init__(
            self,
            eq_type: str,
            vendor: str,
            model: str,
            color: str,
            purchase_price: float,
    ):
        self.type = eq_type
        self.vendor = vendor
        self.model = model
        self.color = color

        self.purchase_price = purchase_price

        self.printable = True if self.type in ("printer", "xerox") else False
        self.scannable = True if self.type in ("scanner", "xerox") else False

    @property
    def retail_price(self):
        return self.wholesale_price * self.retail_rate

    @property
    def wholesale_price(self):
        return self.purchase_price * (1 + self.vat) * (1 + self.added_value)

    def __str__(self):
        return f"{self.type} {self.vendor} {self.model} ({self.color})"


class Printer(OfficeEquipment):
    printable = True
    scannable = False

    def __init__(self, *args):
        super().__init__('Принтер', *args)


class Scanner(OfficeEquipment):
    printable = False
    scannable = True

    def __init__(self, *args):
        super().__init__('scanner', *args)


class Xerox(OfficeEquipment):
    printable = True
    scannable = True

    def __init__(self, *args):
        super().__init__('xerox', *args)


if __name__ == '__main__':
    p1 = Printer("Epson", "XP-400", "white", 4000)
    print(p1)

# task 5

class StorageError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class AddStorageError(StorageError):
    def __init__(self, text):
        self.text = f"Невозможно добавить товар на склад:\n {text}"


class TransferStorageError(StorageError):
    def __init__(self, text):
        self.text = f"Ошибка прередачи оборудования:\n {text}"


class Storage:
    def __init__(self):
        self.__storage = []

    def add(self, item: "OfficeEquipment"):
        if not isinstance(item, OfficeEquipment):
            raise AddStorageError(f"{item} не оргтехника")

        self.__storage.append(item)

    def transfer(self, idx: int, department: str):
        if not isinstance(idx, int):
            raise TransferStorageError(f"Недопустимый тип '{type(item)}'")

        item: OfficeEquipment = self.__storage[idx]

        if item.department:
            raise TransferStorageError(f"Оборудование {item} уже закреплено за отделом {item.department}")

        item.department = department

    def filter_by(self, **kwargs):
        for idx, item in enumerate(self):
            a: OfficeEquipment = item
            if all([a.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield idx, item

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        return self.__storage[key]

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        del self.__storage[key]

    def __iter__(self):
        return self.__storage.__iter__()

    def __str__(self):
        return f"На складе сейчас {len(self.__storage)} устройств"


class OfficeEquipment:
    def __init__(
            self,
            eq_type: str,
            vendor: str,
            model: str,
    ):
        self.type = eq_type
        self.vendor = vendor
        self.model = model

        self.department = None

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)

    def __str__(self):
        return f"{self.type} {self.vendor} {self.model}"


class Printer(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('Принтер', *args)


class Scanner(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('scanner', *args)


class Xerox(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('xerox', *args)


if __name__ == '__main__':
    storage = Storage()
    storage.add(Printer("Epson", "XP-400"))
    storage.add(Scanner("OKI", "5367-AD"))
    storage.add(Xerox("Xerox", "F123"))
    print(storage)

    last_idx = None
    for idx, itm in storage.filter_by(department=None):
        print(idx, itm)
        last_idx = idx

    print("Передаем 1 устройство")
    storage.transfer(last_idx, 'Отдел ЯФ')

    for idx, itm in storage.filter_by(department=None):
        print(idx, itm)

    print(storage)
    print("Удаляем 1 устройство")
    del storage[last_idx]
    print(storage)

# task 6

class AppError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class AcceptStorageError(AppError):
    def __init__(self, text):
        self.text = f"Невозможно добавить товар на склад:\n {text}"


class TransferStorageError(AppError):
    def __init__(self, text):
        self.text = f"Ошибка прередачи оборудования:\n {text}"


AddStorageError = AcceptStorageError


class ValidateEquipmentError(AppError):
    pass


class Storage:
    def __init__(self):
        self.__storage = []

    def add(self, equipments):
        if not all([isinstance(equipment, OfficeEquipment) for equipment in equipments]):
            raise AddStorageError(f"Вы пытаетесь добавить на склад не оргтехнику")

        self.__storage.extend(equipments)

    def transfer(self, idx: int, department: str):
        if not isinstance(idx, int):
            raise TransferStorageError(f"Недопустимый тип '{type(item)}'")

        item: OfficeEquipment = self.__storage[idx]

        if item.department:
            raise TransferStorageError(f"Оборудование {item} уже закреплено за отделом {item.department}")

        item.department = department

    def filter_by(self, **kwargs):
        for id_, item in enumerate(self):
            if all([item.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield id_, item

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        return self.__storage[key]

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        del self.__storage[key]

    def __iter__(self):
        return self.__storage.__iter__()

    def __str__(self):
        return f"На складе сейчас {len(self.__storage)} устройств"


class OfficeEquipment:
    __required_props = ("eq_type", "vendor", "model")

    def __init__(self, eq_type: str = None, vendor: str = "", model: str = ""):
        self.type = eq_type
        self.vendor = vendor
        self.model = model

        self.department = None

    def __setattr__(self, key, value):
        if key in self.__required_props and not value:
            raise AttributeError(f"'{key}' должен иметь значение отличное от false")

        object.__setattr__(self, key, value)

    def __str__(self):
        return f"{self.type} {self.vendor} {self.model}"

    @staticmethod
    def validate(cnt):
        if not isinstance(cnt, int):
            ValidateEquipmentError(f"'{type(cnt)}'; количество инстансов должен быть типа 'int'")

    @classmethod
    def create(cls, cnt, **properties):
        cls.validate(cnt)
        return [cls(**properties) for _ in range(cnt)]


class Printer(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Printer', **kwargs)


class Scanner(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Scanner', **kwargs)


class Xerox(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Xerox', **kwargs)


if __name__ == '__main__':
    storage = Storage()
    storage.add(Printer.create(4, vendor="Epson", model="XP-400"))
    storage.add(Scanner.create(3, vendor="OKI", model="5367-AD"))
    storage.add(Scanner.create(2, vendor="OKI", model="5368-AD"))
    storage.add(Xerox.create(6, vendor="Xerox", model="F123"))
    print(storage)

    for idx, itm in storage.filter_by(department=None, vendor="OKI", model="5367-AD"):
        print(f"Резервируем {itm} в 'Отдел ЯФ'")
        storage.transfer(idx, 'Отдел ЯФ')

    for idx, itm in storage.filter_by(department=None):
        print(idx, f"{itm} не распределены по отделам")

    print(storage)
    print("Списываем 1 устройство")
    del storage[0]
    print(storage)

# task 7

class MyComplex:
    def __init__(self, real, imag=0):
        self.__complex = complex(real, imag)

    def __add__(self, other):
        if isinstance(other, MyComplex):
            other = other.__complex

        complex_ = self.__complex + other
        return MyComplex(complex_.real, int(complex_.imag))

    def __mul__(self, other):
        if isinstance(other, MyComplex):
            other = other.__complex

        complex_ = self.__complex * other
        return MyComplex(complex_.real, int(complex_.imag))

    def __str__(self):
        return self.__complex.__str__()


if __name__ == '__main__':
    c1 = MyComplex(2, -3)
    c2 = MyComplex(5)

    print(c1 + c2, complex(2, -3) + complex(5))
    print(c1 * c2, complex(2, -3) * complex(5))
