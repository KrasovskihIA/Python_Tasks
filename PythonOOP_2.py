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

"""
Объявите класс с именем Triangle, объекты которого создаются командой:

tr = Triangle(a, b, c)
где a, b, c - длины сторон треугольника (числа: целые или вещественные). В классе Triangle объявите следующие дескрипторы данных:

a, b, c - для записи и считывания длин сторон треугольника.

При записи нового значения нужно проверять, что присваивается положительное число (целое или вещественное). Иначе, генерируется исключение командой:

raise ValueError("длины сторон треугольника должны быть положительными числами")
Также нужно проверять, что все три стороны a, b, c могут образовывать стороны треугольника. То есть, должны выполняться условия:

a < b+c; b < a+c; c < a+b

Иначе генерируется исключение командой:

raise ValueError("с указанными длинами нельзя образовать треугольник")
Наконец, с объектами класса Triangle должны выполняться функции:

len(tr) - возвращает периметр треугольника, приведенный к целому значению с помощью функции int();
tr() - возвращает площадь треугольника (можно вычислить по формуле Герона: s = sqrt(p * (p-a) * (p-b) * (p-c)), где p - полупериметр треугольника).

P.S. На экран ничего выводить не нужно, только объявить класс Triangle.
"""
class PosotoveValue:           
    def __set_name__(self, owner, name):
        self.name = "_" + name
 
    def __get__(self, instance, owner):
        return getattr(instance, self.name, None)
 
    def __set__(self, instance, value):
        if value <= 0 or type(value) not in (int, float):
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        setattr(instance, self.name, value)


class Triangle:
    a = PosotoveValue()
    b = PosotoveValue()
    c = PosotoveValue()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def __is_triangle(a, b, c):
        if a and b and c:
            return a < b+c and b < a+c and c < a+b
        return True

    def __setattr__(self, key, value):
        if (key == 'a' and not self.__is_triangle(value, self.b, self.c)) or (key == 'b' and not self.__is_triangle(self.a, value, self.c)) or (key == 'c' and not self.__is_triangle(self.a, self.b, value)):
            raise ValueError("с указанными длинами нельзя образовать треугольник")

        object.__setattr__(self, key, value)


    def __len__(self):
        return int(self.a + self.b + self.c)


    def __call__(self):
        a, b, c =self.a, self.b, self.c
        if not (a and b and c):
            return

        p = 0.5 * (a + b + c)
        return (p * (p-a) * (p-b) * (p-c))**0.5

"""
Подвиг 4. Объявите в программе класс Player (игрок), объекты которого создаются командой:

player = Player(name, old, score)
где name - имя игрока (строка); old - возраст игрока (целое число); score - набранные очки в игре (целое число). В каждом объекте класса Player должны создаваться аналогичные локальные атрибуты: name, old, score.

С объектами класса Player должна работать функция:

bool(player)
которая возвращает True, если число очков больше нуля, и False - в противном случае.

С помощью команды:

lst_in = list(map(str.strip, sys.stdin.readlines()))
считываются строки из входного потока в список строк lst_in. Каждая строка записана в формате:

"имя; возраст; очки"

Например:

Балакирев; 34; 2048
Mediel; 27; 0
Влад; 18; 9012
Nina P; 33; 0

Каждую строку списка lst_in необходимо представить в виде объекта класса Player с соответствующими данными. И из этих объектов сформировать список players.

Отфильтруйте этот список (создайте новый: players_filtered), оставив всех игроков с числом очков больше нуля. Используйте для этого стандартную функцию filter() совместно с функцией bool() языка Python. 

P.S. На экран ничего выводить не нужно.
"""
import sys

class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = int(score)

    def __bool__(self):
        return self.score > 0 


lst_in = list(map(str.strip, sys.stdin.readlines()))
players = list(map(lambda x: Player(*x.split('; ')), lst_in))

for x in players:
    if not bool(x):
        players.remove(x)

players_filtered = list(filter(bool, players))

"""
Подвиг 5. Объявите в программе класс MailBox (почтовый ящик), объекты которого создаются командой:

mail = MailBox()
Каждый объект этого класса должен содержать локальный публичный атрибут:

inbox_list - список из принятых писем.

Также в классе MailBox должен присутствовать метод:

receive(self) - прием новых писем

Этот метод должен читать данные из входного потока командой:

lst_in = list(map(str.strip, sys.stdin.readlines()))
В результате формируется список lst_in из строк. Каждая строка записана в формате:

"от кого; заголовок; текст письма"

Например:

sc_lib@list.ru; От Балакирева; Успехов в IT!
mail@list.ru; Выгодное предложение; Вам одобрен кредит.
mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить.

Каждая строчка списка lst_in должна быть представлена объектом класса MailItem, объекты которого создаются командой:

item = MailItem(mail_from, title, content)
где mail_from - email отправителя (строка); title - заголовок письма (строка), content - содержимое письма (строка). В каждом объекте класса MailItem должны формироваться соответствующие локальные атрибуты (с именами: mail_from, title, content). И дополнительно атрибут is_read (прочитано ли) с начальным значением False.

В классе MailItem должен быть реализован метод:

set_read(self, fl_read) - для отметки, что письмо прочитано (метод должен устанавливать атрибут is_read = fl_read, если True, то письмо прочитано, если False, то не прочитано).

С каждым объектом класса MailItem должна работать функция:

bool(item)
которая возвращает True для прочитанного письма и False для непрочитанного.

Вызовите метод:

mail.receive()
Отметьте первое и последнее письмо в списке mail.inbox_list, как прочитанное (используйте для этого метод set_read). Затем, сформируйте в программе список (глобальный) с именем inbox_list_filtered из прочитанных писем, используя стандартную функцию filter() совместно с функцией bool() языка Python.

P.S. На экран ничего выводить не нужно.


"""
import sys

class MailBox:
    def __init__(self):
        self.inbox_list = []

    def receive(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        self.inbox_list = list(map(lambda x: MailItem(*x.split('; ')), lst_in))

class MailItem:
    def __init__(self, mail_from, title, content):
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False

    def set_read(self, fl_read):
            self.is_read = fl_read

    def __bool__(self):
        return self.is_read == True

mail = MailBox()
mail.receive()
mail.inbox_list[0].set_read(True)
mail.inbox_list[-1].set_read(True)
inbox_list_filtered = list(filter(bool, mail.inbox_list))

"""
Объявите класс Line, объекты которого создаются командой:

line = Line(x1, y1, x2, y2)
где x1, y1, x2, y2 - координаты начала линии (x1, y1) и координаты конца линии (x2, y2). Могут быть произвольными числами. В объектах класса Line должны создаваться соответствующие локальные атрибуты с именами x1, y1, x2, y2.

В классе Line определить магический метод __len__() так, чтобы функция:

bool(line)
возвращала False, если длина линии меньше 1.

P.S. На экран ничего выводить не нужно. Только объявить класс.
"""
class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __len__(self):
        return ((self.x2 - self.x1)^2 + (self.y2 - self.y1)^2)**0.5 > 1


"""
Подвиг 7. Объявите класс Ellipse (эллипс), объекты которого создаются командами:

el1 = Ellipse()  # без создания локальных атрибутов x1, y1, x2, y2
el2 = Ellipse(x1, y1, x2, y2)
где x1, y1 - координаты (числа) левого верхнего угла; x2, y2 - координаты (числа) нижнего правого угла. Первая команда создает объект класса Ellipse без локальных атрибутов x1, y1, x2, y2. Вторая команда создает объект с локальными атрибутами x1, y1, x2, y2 и соответствующими переданными значениями.

В классе Ellipse объявите магический метод __bool__(), который бы возвращал True, если все локальные атрибуты x1, y1, x2, y2 существуют и False - в противном случае.

Также в классе Ellipse нужно реализовать метод:

get_coords() - для получения кортежа текущих координат объекта.

Если координаты отсутствуют (нет локальных атрибутов x1, y1, x2, y2), то метод get_coords() должен генерировать исключение командой:

raise AttributeError('нет координат для извлечения')
Сформируйте в программе список с именем lst_geom, содержащий четыре объекта класса Ellipse. Два объекта должны быть созданы командой 

Ellipse()
и еще два - командой:

Ellipse(x1, y1, x2, y2)
Переберите список в цикле и вызовите метод get_coords() только для объектов, имеющих координаты x1, y1, x2, y2. (Помните, что для этого был определен магический метод __bool__()).

P.S. На экран ничего выводить не нужно.
"""
class Ellipse:
    def __init__(self, x1=None, y1=None, x2=None, y2=None):
        if x1 != None:
            self.x1 = x1
        if y1 != None:
            self.y1 = y1
        if x2 != None:
            self.x2 = x2
        if y2 != None:
            self.y2 = y2

    def __bool__(self):
        return len(self.__dict__) == 4

    def get_coords(self):
        if bool(self):
            return (self.x1, self.y1, self.x2, self.y2)
        else:
            raise AttributeError('нет координат для извлечения')

lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 1, 2, 2), Ellipse(1, 1, 2, 2)]
for i in lst_geom:
    if i:
        i.get_coords()

"""
Объявите в программе класс Vector, объекты которого создаются командой:

v = Vector(x1, x2, x3,..., xN)
где x1, x2, x3,..., xN - координаты вектора (числа: целые или вещественные).

С каждым объектом класса Vector должны выполняться операторы:

v1 + v2 # суммирование соответствующих координат векторов
v1 - v2 # вычитание соответствующих координат векторов
v1 * v2 # умножение соответствующих координат векторов

v1 += 10 # прибавление ко всем координатам вектора числа 10
v1 -= 10 # вычитание из всех координат вектора числа 10
v1 += v2
v2 -= v1

v1 == v2 # True, если соответствующие координаты векторов равны
v1 != v2 # True, если хотя бы одна пара координат векторов не совпадает
При реализации бинарных операторов +, -, * следует создавать новые объекты класса Vector с новыми (вычисленными) координатами. При реализации операторов +=, -= координаты меняются в текущем объекте, не создавая новый.

Если число координат (размерность) векторов v1 и v2 не совпадает, то при операторах +, -, * должно генерироваться исключение командой:

raise ArithmeticError('размерности векторов не совпадают')
P.S. В программе на экран выводить ничего не нужно, только объявить класс.
"""
import numpy

class Vector:
    def __init__(self, *args, **kwargs):
        self.points = args
        
    def check_vector(func):
        def wrapper(self, vector, *args, **kwargs):
            if not (type(vector) in (int, float)):
                if len(vector.points) != len(self.points):
                    raise ArithmeticError('размерности векторов не совпадают')
            return func(self, vector)
        return wrapper
    
    @check_vector    
    def __add__(self, other):
        return Vector(*[i + y for i, y in zip(self.points, other.points)])
    
    @check_vector
    def __sub__(self, other):
        return Vector(*[i - y for i, y in zip(self.points, other.points)])
    
    @check_vector
    def __mul__(self, other):
        return Vector(*[i * y for i, y in zip(self.points, other.points)])
    
    @check_vector
    def __iadd__(self, other):
        if type(other) in (int, float):
            self.points = tuple(numpy.array(self.points) + other)
        else:
            self.points = tuple(numpy.array(self.points) + numpy.array(other.points))
        return self
            
    @check_vector
    def __isub__(self, other):
        if type(other) in (int, float):
            self.points = tuple(numpy.array(self.points) - other)
        else:
            self.points = tuple(numpy.array(self.points) - numpy.array(other.points))
        return self
    
    def __eq__(self, other):
        return self and other and self.points == other.points
    
    def __ne__(self, other):
        return self and other and self.points != other.points
    
    def __len__(self):
        return len(self.points)


"""
Подвиг 2. Объявите класс Record (запись), который описывает одну произвольную запись из БД. Объекты этого класса создаются командой:

r = Record(field_name1=value1,... , field_nameN=valueN)
где field_nameX - наименование поля БД; valueX - значение поля из БД.

В каждом объекте класса Record должны автоматически создаваться локальные публичные атрибуты по именам полей (field_name1,... , field_nameN) с соответствующими значениями. Например:

r = Record(pk=1, title='Python ООП', author='Балакирев')
В объекте r появляются атрибуты:

r.pk # 1
r.title # Python ООП
r.author # Балакирев
Также необходимо обеспечить доступ к этим полям (чтение/запись) через индексы следующим образом:

r[0] = 2 # доступ к полю pk
r[1] = 'Супер курс по ООП' # доступ к полю title
r[2] = 'Балакирев С.М.' # доступ к полю author
print(r[1]) # Супер курс по ООП
r[3] # генерируется исключение IndexError
Если указывается неверный индекс (не целое число или некорректное целое число), то должно генерироваться исключение командой:

raise IndexError('неверный индекс поля')
P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно.

P.P.S. Для создания локальных атрибутов используйте коллекцию __dict__ объекта класса Record.
"""
class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __getitem__(self, item):
        if not isinstance(item, int) or item > len(list(self.__dict__.values())):
            raise IndexError('неверный индекс поля')
        return list(self.__dict__.values())[item]

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key > len(list(self.__dict__.values())):
            raise IndexError('неверный индекс поля')
        self.__dict__[list(self.__dict__.keys())[key]] = value

"""
Подвиг 3. Вам необходимо для навигатора реализовать определение маршрутов. Для этого в программе нужно объявить класс Track, объекты которого создаются командой:

tr = Track(start_x, start_y)
где start_x, start_y - координата начала пути.

В этом классе должен быть реализован следующий метод:

add_point(x, y, speed) - добавление новой точки маршрута (линейный сегмент), который можно пройти со средней скоростью speed.

Также с объектами класса Track должны выполняться команды:

coord, speed = tr[indx] # получение координаты (кортеж с двумя числами) и скорости (число) для линейного сегмента маршрута с индексом indx
tr[indx] = speed # изменение средней скорости линейного участка маршрута по индексу indx
Если индекс (indx) указан некорректно (должен быть целым числом от 0 до N-1, где N - число линейных сегментов в маршруте), то генерируется исключение командой:
"""
class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.points = []

    def add_point(self, x, y, speed):
        self.points.append([(x, y), speed])

    def __setitem__(self, key, value):
        if not isinstance(key, int) and key > len(self.points):
            raise IndexError('некорректный индекс')
        self.points[key][1] = value

    def __getitem__(self, item):
        if not isinstance(item, int) and item > len(self.points):
            raise IndexError('некорректный индекс')
        return self.points[item]

tr = Track(10, -5.4)
tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2

tr[2] = 60
c, s = tr[0]
print(c, s)
        

"""
Подвиг 4. Вам необходимо написать программу по работе с массивом однотипных данных (например, только числа или строки и т.п.). Для этого нужно объявить класс с именем Array, объекты которого создаются командой:

ar = Array(max_length, cell)
где max_length - максимальное количество элементов в массиве; cell - ссылка на класс, описывающий отдельный элемент этого массива (см. далее, класс Integer). Начальные значения в ячейках массива (в объектах класса Integer) должны быть равны 0.

Для работы с целыми числами объявите в программе еще один класс с именем Integer, объекты которого создаются командой:

cell = Integer(start_value)
где start_value - начальное значение ячейки (в данном случае - целое число).

В классе Integer должно быть следующее свойство (property):

value - для изменения и считывания значения из ячейки (само значение хранится в локальной приватной переменной; имя придумайте сами).

При попытке присвоить не целое число должно генерироваться исключение командой:

raise ValueError('должно быть целое число')
Для обращения к отдельным элементам массива в классе Array необходимо определить набор магических методов для следующих операций:

value = ar[0] # получение значения из первого элемента (ячейки) массива ar
ar[1] = value # запись нового значения во вторую ячейку массива ar
Если индекс не целое число или число меньше нуля или больше либо равно max_length, то должно генерироваться исключение командой:

raise IndexError('неверный индекс для доступа к элементам массива')
"""
class Integer:
    def __init__(self, start_value=0):
        self.__value = start_value

    @property
    def value (self):
        return self.__value

    @value.setter
    def value (self, values):
        if type(values) != int:
            raise ValueError('должно быть целое число')
        self.__value = values

    def __repr__(self):
        return str(self.__value)

class Array:
    def __init__(self, max_length, cell):
        self.__max_length = max_length
        self.__cell = cell
        self.__array = [self.__cell() for _ in range (self.__max_length)]

    def __check(self, index):
        if type(index) != int or not (-self.__max_length <= index < self.__max_length):
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __getitem__(self, item):
        self.__check(item)
        return self.__array[item].value

    def __setitem__(self, key, value):
        self.__check(key)
        self.__array[key].value = value
    
    def __repr__(self):
        return ' '.join(map(str, self.__array))

"""
Большой подвиг 5. Вам необходимо написать программу для удобного обращения с таблицами однотипных данных (чисел, строк, булевых значений и т.п.), то есть, все ячейки таблицы должны представлять какой-то один указанный тип.



Для этого в программе необходимо объявить три класса:

TableValues - для работы с таблицей в целом;
CellInteger - для операций с целыми числами;
IntegerValue - дескриптор данных для работы с целыми числами.

Начнем с дескриптора IntegerValue. Это должен быть дескриптор данных (то есть, и для записи и считывания значений). Если присваиваемое значение не является целым числом, должно генерироваться исключение командой:

raise ValueError('возможны только целочисленные значения')
Следующий класс CellInteger описывает одну ячейку таблицы для работы с целыми числами. В этом классе должен быть публичный атрибут (атрибут класса):

value - объект дескриптора, класса IntegerValue.

А объекты класса CellInteger должны создаваться командой:

cell = CellInteger(start_value)
где start_value - начальное значение ячейки (по умолчанию равно 0 и сохраняется в ячейке через дескриптор value).

Наконец, объекты последнего класса TableValues создаются командой:

table = TableValues(rows, cols, cell=CellInteger)
где rows, cols - число строк и столбцов (целые числа); cell - ссылка на класс, описывающий работу с отдельными ячейками таблицы. Если параметр cell не указан, то генерировать исключение командой:

raise ValueError('параметр cell не указан')
Иначе, в объекте table класса TableValues создается двумерный (вложенный) кортеж с именем cells размером rows x cols, состоящий из объектов указанного класса (в данном примере - класса CellInteger).

Также в классе TableValues предусмотреть возможность обращения к отдельной ячейке по ее индексам, например:

value = table[1, 2] # возвращает значение ячейки с индексом (1, 2)
table[0, 0] = value # записывает новое значение в ячейку (0, 0)
Обратите внимание, по индексам сразу должно возвращаться значение ячейки, а не объект класса CellInteger. И то же самое с присваиванием нового значения.
"""
#дескриптор
class IntegerValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name
 
    def __get__(self, instance, owner):
        return getattr(instance, self.name, None)
 
    def __set__(self, instance, value):
        if type(value) != int:
            raise ValueError('возможны только целочисленные значения')
        setattr(instance, self.name, value)

# класс CellInteger описывает одну ячейку таблицы для работы с целыми числами
class CellInteger:
    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value

#для работы с таблицей в целом
class TableValues:
    def __init__(self, rows, cols, cell=None):
        self._rows = rows
        self._cols = cols
        if not cell:
            raise ValueError('параметр cell не указан')
        self.cells = tuple(tuple(cell() for _ in range(cols)) for _ in range(rows))


    def __getitem__(self, item):
        return self.cells[item[0]][item[1]].value

    def __setitem__(self, key, value):
        self.cells[key[0]][key[1]].value = value