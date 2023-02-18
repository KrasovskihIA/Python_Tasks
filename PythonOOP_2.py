"""
Перед вами стоит задача выделения файлов с определенными расширениями из списка файлов, например:

filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]
Для этого необходимо объявить класс FileAcceptor, объекты которого создаются командой:

acceptor = FileAcceptor(ext1, ..., extN)
где ext1, ..., extN - строки с допустимыми расширениями файлов, например: 'jpg', 'bmp', 'jpeg'.

После этого предполагается использовать объект acceptor в стандартной функции filter языка Python следующим образом:

filenames = list(filter(acceptor, filenames))
То есть, объект acceptor должен вызываться как функция:

acceptor(filename) 
и возвращать True, если файл с именем filename содержит расширения, указанные при создании acceptor, и False - в противном случае. Кроме того, с объектами класса FileAcceptor должен выполняться оператор:

acceptor12 = acceptor1 + acceptor2
Здесь формируется новый объект acceptor12 с уникальными расширениями первого и второго объектов. Например:

acceptor1 = FileAcceptor("jpg", "jpeg", "png")
acceptor2 = FileAcceptor("png", "bmp")
acceptor12 = acceptor1 + acceptor2    # ("jpg", "jpeg", "png", "bmp")
Пример использования класса (эти строчки в программе писать не нужно):

acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
filenames = list(filter(acceptor_images + acceptor_docs, filenames))
P.S. На экран в программе ничего выводить не нужно.
"""

class FileAcceptor:
    def __init__(self, *args):
        self.file_names = list(args)

    def __call__(self, filename):
        return filename[filename.rfind('.')+1:] in self.file_names
        
    def __add__(self, other):
        return FileAcceptor(*self.file_names + other.file_names)

filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]
acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
filenames = list(filter(acceptor_images + acceptor_docs, filenames))


"""
 В программе необходимо объявить классы для работы с кошельками в разных валютах:

MoneyR - для рублевых кошельков
MoneyD - для долларовых кошельков
MoneyE - для евро-кошельков
"""
class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cld, *args, **kwargs):
        return
    
    @classmethod
    def register(cls, money):
        money.cb = cls


class Money:
    EPS = 0.1
    type_money = None
            
    def __init__(self, volume=0, cb=None ):
        self.__volume = volume
        self.__cb = cb

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, other):
        self.__volume = other

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, other):
        self.__cb = other

    def get_volumes(self, other):
        if self.cb is None:
            raise ValueError("Error")

        if self.type_money is None:
            raise ValueError("Error")

        v1 = self.volume / self.cb.rates[self.type_money]
        v2 = other.volume / self.cb.rates[other.type_money]
        return v1, v2


    def __eq__(self, other):
        v1, v2 = self.get_volumes(other)
        return abs(v1 - v2) < self.EPS

    def __lt__(self, other):
        v1, v2 = self.get_volumes(other)
        return v1 < v2

    def __le__(self, other):
        v1, v2 = self.get_volumes(other)
        return v1 <= v2


class MoneyR(Money):
    type_money = "rub"

class MoneyD(Money):
    type_money = "dollar"

class MoneyE(Money):
    type_money = "euro"

"""
Необходимо объявить класс Body (тело), объекты которого создаются командой:

body = Body(name, ro, volume)
где name - название тела (строка); ro - плотность тела (число: вещественное или целочисленное); volume - объем тела  (число: вещественное или целочисленное).

Для объектов класса Body должны быть реализованы операторы сравнения:

body1 > body2  # True, если масса тела body1 больше массы тела body2
body1 == body2 # True, если масса тела body1 равна массе тела body2
body1 < 10     # True, если масса тела body1 меньше 10
body2 == 5     # True, если масса тела body2 равна 5
Масса тела вычисляется по формуле:

m = ro * volume

P.S. В программе только объявить класс, выводить на экран ничего не нужно.
"""
class Body:
    def __init__(self, name, ro, volume):
        self. name = name
        self.ro = ro
        self.volume = volume
        self.massa = self.ro * self.volume

    def __lt__(self, other):
        if isinstance(other, Body):
            return self.massa < other.massa
        else:
            return self.massa < other

    def __eq__(self, other):
        if isinstance(other, Body):
            return self.massa == other.massa
        else:
            return self.massa == other


"""
Объявите в программе класс с именем Box (ящик), объекты которого должны создаваться командой:

box = Box()
А сам класс иметь следующие методы:

add_thing(self, obj) - добавление предмета obj (объект другого класса Thing) в ящик;
get_things(self) - получение списка объектов ящика.

Для описания предметов необходимо объявить еще один класс Thing. Объекты этого класса должны создаваться командой:

obj = Thing(name, mass)
где name - название предмета (строка); mass - масса предмета (число: целое или вещественное).
Объекты класса Thing должны поддерживать операторы сравнения:

obj1 == obj2
obj1 != obj2
Предметы считаются равными, если у них одинаковые названия name (без учета регистра) и массы mass.

Также объекты класса Box должны поддерживать аналогичные операторы сравнения:

box1 == box2
box1 != box2
Ящики считаются равными, если одинаковы их содержимое (для каждого объекта класса Thing одного ящика и можно найти ровно один равный объект из второго ящика).
"""
class Box:
    def __init__(self):
        self.list_box = []

    def add_thing(self, obj):
        self.list_box.append(obj)

    def get_things(self):
        return self.list_box

    def __eq__(self, other: 'Box') -> bool:
        count = 0
        for b1 in self.list_box:
            for b2 in other.list_box:
                if b1.name == b2.name and b1.mass == b2.mass:
                    count += 1
        if count == len(self.list_box) and count == len(other.list_box):
            return True
        else:
            return False


class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return (self.name.lower() == other.name.lower()) and (self.mass == other.mass)


"""
Подвиг 4. Объявите в программе класс с именем Rect (прямоугольник), объекты которого создаются командой:

rect = Rect(x, y, width, height)
где x, y - координата верхнего левого угла (числа: целые или вещественные); width, height - ширина и высота прямоугольника (числа: целые или вещественные).

В этом классе определите магический метод, чтобы хэши объектов класса Rect с равными width, height были равны. Например:

r1 = Rect(10, 5, 100, 50)
r2 = Rect(-10, 4, 100, 50)

h1, h2 = hash(r1), hash(r2)   # h1 == h2
P.S. На экран ничего выводить не нужно, только объявить класс.
"""

class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __hash__(self) :
        return hash((self.width, self.height))


"""
Подвиг 6. Объявите класс с именем ShopItem (товар), объекты которого создаются командой:

item = ShopItem(name, weight, price)
где name - название товара (строка); weight - вес товара (число: целое или вещественное); price - цена товара (число: целое или вещественное).

Определите в этом классе магические методы:

__hash__() - чтобы товары с одинаковым названием (без учета регистра), весом и ценой имели бы равные хэши;
__eq__() - чтобы объекты с одинаковыми хэшами были равны.

Затем, из входного потока прочитайте строки командой:

lst_in = list(map(str.strip, sys.stdin.readlines()))
Строки имеют следующий формат:

название товара 1: вес_1 цена_1
...
название товара N: вес_N цена_N

Например:

Системный блок: 1500 75890.56
Монитор Samsung: 2000 34000
Клавиатура: 200.44 545
Монитор Samsung: 2000 34000

Как видите, товары в этом списке могут совпадать.

Необходимо для всех этих строчек сформировать соответствующие объекты класса ShopItem и добавить в словарь с именем shop_items. Ключами словаря должны выступать сами объекты, а значениями - список в формате:

[item, total]

где item - объект класса ShopItem; total - общее количество одинаковых объектов (с одинаковыми хэшами). Подумайте, как эффективно программно наполнять такой словарь, проходя по списку lst_in один раз.

P.S. На экран ничего выводить не нужно, только объявить класс и сформировать словарь.
"""
import sys

class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)

lst_in = list(map(str.strip, sys.stdin.readlines()))
shop_items = {}
for i in lst_in:
    text = i.split()
    text[-3] = text[-3].replace(':', '')
    item = ShopItem(' '.join(text[0:-2]), float(text[-2]), float(text[-1]))
    total = 1
    if item in shop_items:
        shop_items[item][1] += 1
    else:
        shop_items[item] = [item, total]
    

"""
Подвиг 7. Объявите класс с именем DataBase (база данных - БД), объекты которого создаются командой:

db = DataBase(path)
где path - путь к файлу с данными БД (строка).

Также в классе DataBase нужно объявить следующие методы:

write(self, record) - для добавления новой записи в БД, представленной объектом record;
read(self, pk) - чтение записи из БД (возвращает объект Record) по ее уникальному идентификатору pk (уникальное целое положительное число); запись ищется в значениях словаря (см. ниже)

Каждая запись БД должна описываться классом Record, а объекты этого класса создаваться командой:

record = Record(fio, descr, old)
где fio - ФИО некоторого человека (строка); descr - характеристика человека (строка); old - возраст человека (целое число).

В каждом объекте класса Record должны формироваться следующие локальные атрибуты:

pk - уникальный идентификатор записи (число: целое, положительное); формируется автоматически при создании каждого нового объекта;
fio - ФИО человека (строка);
descr - характеристика человека (строка);
old - возраст человека (целое число).

Реализовать для объектов класса Record вычисление хэша по атрибутам: fio и old (без учета регистра). Если они одинаковы для разных записей, то и хэши должны получаться равными. Также для объектов класса Record  с одинаковыми хэшами оператор == должен выдавать значение True, а с разными хэшами - False.

Хранить записи в БД следует в виде словаря dict_db (атрибут объекта db класса DataBase), ключами которого являются объекты класса Record, а значениями список из объектов с равными хэшами:

dict_db[rec1] = [rec1, rec2, ..., recN]

где rec1, rec2, ..., recN - объекты класса Record с одинаковыми хэшами.

Для наполнения БД прочитайте строки из входного потока с помощью команды:

lst_in = list(map(str.strip, sys.stdin.readlines()))
где каждая строка представлена в формате:

"ФИО; характеристика; возраст"
"""
import sys

class DataBase:
    def __init__(self, path):
        self.path = path
        self.dict_db = {}

    def write(self, record):
        self.dict_db.setdefault(record, [])
        self.dict_db[record].append(record)

    def read(self, pk):
        r = (x for row in self.dict_db.values() for x in row)
        obj = tuple(filter(lambda x: x.pk == pk, r))
        return obj[0] if len(obj) > 0 else None


class Record:
    record_count = 0

    def __init__(self, fio, descr, old):
        self.fio = fio
        self.descr = descr
        self.old = old
        self.pk = self.__count()

    @classmethod
    def __count(cls):
        cls.record_count += 1
        return cls.record_count

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other):
        return hash(self) == hash(other)


lst_in = list(map(str.strip, sys.stdin.readlines()))

db = DataBase("database.db")
for i in lst_in:
    args = list(map(str.strip, i.split(';')))
    args[-1] = int(args[-1])
    db.write(Record(*args))



"""
Подвиг 8. Из входного потока необходимо прочитать список строк командой:

lst_in = list(map(str.strip, sys.stdin.readlines()))
Каждая строка содержит информацию об учебном пособии в формате:

"Название; автор; год издания"

Например:

Python; Балакирев С.М.; 2020
Python ООП; Балакирев С.М.; 2021
Python ООП; Балакирев С.М.; 2022
Python; Балакирев С.М.; 2021

Необходимо каждую из этих строк представить объектом класса BookStudy, которые создаются командой:

bs = BookStudy(name, author, year)
где name - название пособия (строка); author - автор пособия (строка); year - год издания (целое число). Такие же публичные локальные атрибуты должны быть в объектах класса BookStudy.

Для каждого объекта реализовать вычисление хэша по двум атрибутам: name и author (без учета регистра).

Сформировать список lst_bs из объектов класса BookStudy на основе прочитанных строк (списка lst_in). После этого определить число книг с уникальными хэшами. Это число сохранить через переменную unique_books (целое число).

P.S. На экран ничего выводить не нужно.
"""
import sys

class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))

    def __eq__(self, other):
        return hash(self) == hash(other)

lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_bs = list(map(lambda x: BookStudy(*x.split('; ')), lst_in))

unique_books = len(set(lst_bs))

"""
Объявите класс с именем Dimensions, объекты которого создаются командой:

d = Dimensions(a, b, c)
где a, b, c - положительные числа (целые или вещественные), описывающие габариты некоторого тела: высота, ширина и глубина.

Каждый объект класса Dimensions должен иметь аналогичные публичные атрибуты a, b, c (с соответствующими числовыми значениями). Также для каждого объекта должен вычисляться хэш на основе всех трех габаритов: a, b, c.

С помощью функции input() прочитайте из входного потока строку, записанную в формате:

"a1 b1 c1; a2 b2 c2; ... ;aN bN cN"

Например:

"1 2 3; 4 5 6.78; 1 2 3; 0 1 2.5"

Если какой-либо габарит оказывается отрицательным значением или равен нулю, то при создании объектов должна генерироваться ошибка командой:

raise ValueError("габаритные размеры должны быть положительными числами")
Сформируйте на основе прочитанной строки список lst_dims из объектов класса Dimensions. После этого отсортируйте этот список по возрастанию (неубыванию) хэшей этих объектов так, чтобы объекты с равными хэшами стояли друг за другом.

P.S. На экран ничего выводить не нужно.
"""

class Dimensions:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, name, value):
        if value <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        object.__setattr__(self, name, value)

    def __hash__(self):
        return hash((self.a, self.b, self.c))

    
s_inp = input()
lst_dims = sorted([Dimensions(*map(float, elem.split())) for elem in s_inp.split('; ')], key=hash)