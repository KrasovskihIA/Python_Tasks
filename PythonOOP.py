"""
open(file) - для открытия медиа-файла с именем file (создает локальное свойство filename со значением аргумента file в объекте класса MediaPlayer)
play() - для воспроизведения медиа-файла (выводит на экран строку "Воспроизведение <название медиа-файла>")
Создайте два экземпляра этого класса с именами: media1 и media2. Вызовите из них метод open() с аргументом "filemedia1" для объекта media1 и "filemedia2" для объекта media2. После этого вызовите через объекты метод play(). При этом, на экране должно отобразиться две строки (без кавычек):
"""
class MediaPlayer:
    
    def open(self, file):
        self.filename = file
        
    def play(self):
        print(f'Воспроизведение {self.filename}')
        
media1 = MediaPlayer()
media1.open("filemedia1")
media1.play()

media2 = MediaPlayer()
media2.open("filemedia2")
media2.play()


"""
Подвиг 5. Объявите класс с именем Graph и методами:

set_data(data) - передача набора данных data для последующего отображения (data - список числовых данных);
draw() - отображение данных (в том же порядке, что и в списке data)
и атрибутом:
LIMIT_Y = [0, 10]
Метод set_data() должен формировать локальное свойство data объекта класса Graph. Атрибут data должен ссылаться на переданный в метод список. Метод draw() должен выводить на экран список в виде строки из чисел, разделенных пробелами и принадлежащие заданному диапазону атрибута LIMIT_Y (границы включаются).
Создайте объект graph_1 класса Graph, вызовите для него метод set_data() и передайте список:
[10, -5, 100, 20, 0, 80, 45, 2, 5, 7]
Затем, вызовите метод draw() через объект graph_1. На экране должна появиться строка с соответствующим набором чисел, записанных через пробел. Например (вывод без кавычек):
"10 0 2 5 7"
"""

class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data

    def draw(self):
        e = ''
        for x in self.data:
            if self.LIMIT_Y[0] <= x <= self.LIMIT_Y[1]:
                e = e + str(x) + ' '
        print(e[:-1])

graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()

"""
Подвиг 7. Имеется следующий класс для считывания информации из входного потока:

import sys


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res
Которым, затем, можно воспользоваться следующим образом:

sr = StreamReader()
data, result = sr.readlines()

Необходимо перед классом StreamReader объявить еще один класс StreamData с методом:
def create(self, fields, lst_values): ...
который бы на входе получал кортеж FIELDS из названий локальных атрибутов (передается в атрибут fields) и список строк lst_in (передается в атрибут lst_values) и формировал бы в объекте класса StreamData локальные свойства с именами полей из fields и соответствующими значениями из lst_values.
Если создание локальных свойств проходит успешно, то метод create() возвращает True, иначе - False. Если число полей и число строк не совпадает, то метод create() возвращает False и локальные атрибуты создавать не нужно.
P.S. В программе нужно дополнительно объявить только класс StreamData. Больше ничего делать не нужно.
"""

import sys

class StreamData:
    def create(self, fields, lst_values):
        if len(fields) != len(lst_values):
            return False
        else:
            for i, key in enumerate(fields):
                setattr(self, key, lst_values[i])
        return True

class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()




"""
Подвиг 9. Из входного потока читаются строки данных с помощью команды:

lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
в формате: id, name, old, salary (записанные через пробел). Например:

1 Сергей 35 120000
2 Федор 23 12000
3 Иван 13 1200
...

То есть, каждая строка - это элемент списка lst_in.

Необходимо в класс DataBase:

class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')
добавить два метода:
select(self, a, b) - возвращает список из элементов списка lst_data в диапазоне [a; b] (включительно) по их индексам (не id, а индексам списка); также учесть, что граница b может превышать длину списка.
insert(self, data) - для добавления в список lst_data новых данных из переданного списка строк data;
Каждая запись в списке lst_data должна быть представлена словарем в формате:
{'id': 'номер', 'name': 'имя', 'old': 'возраст', 'salary': 'зарплата'}

Например:
{'id': '1', 'name': 'Сергей', 'old': '35', 'salary': '120000'}
Примечание: в этой задаче число элементов в строке (разделенных пробелом) всегда совпадает с числом полей в коллекции FIELDS.
P. S. Ваша задача только добавить два метода в класс DataBase.
"""

import sys

# программу не менять, только добавить два метода
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def select(self, a, b):
        return self.lst_data[a:b+1]

    def insert(self, data):
        for x in data:
            self.lst_data.append(dict(zip(self.FIELDS, x.split())))


db = DataBase()
db.insert(lst_in)


"""
Подвиг 10. Объявите класс с именем Translator (для перевода с английского на русский) со следующими методами:

add(self, eng, rus) - для добавления новой связки английского и русского слова (если английское слово уже существует, то новое русское слово добавляется как синоним для перевода, например, go - идти, ходить, ехать); если связка eng-rus уже существует, то второй раз ее добавлять не нужно, например:  add('go', 'идти'), add('go', 'идти');
remove(self, eng) - для удаления связки по указанному английскому слову;
translate(self, eng) - для перевода с английского на русский (метод должен возвращать список из русских слов, соответствующих переводу английского слова, даже если в списке всего одно слово).

Все добавления и удаления связок должны выполняться внутри каждого конкретного объекта класса Translator, т.е. связки хранить локально внутри экземпляров классов класса Translator.
Создайте экземпляр tr класса Translator и вызовите метод add для следующих связок:

tree - дерево
car - машина
car - автомобиль
leaf - лист
river - река
go - идти
go - ехать
go - ходить
milk - молоко

Затем методом remove() удалите связку для английского слова car. С помощью метода translate() переведите слово go. Результат выведите на экран в виде строки из всех русских слов, связанных со словом go:
"""

class Translator:
    def add(self, eng, rus):
        if 'tr' not in self.__dict__:
            self.tr = {}

        self.tr.setdefault(eng, [])
        if rus not in self.tr[eng]:
            self.tr[eng].append(rus)

    
    def remove(self, eng):
        self.tr.pop(eng, False)

    def translate(self, eng):
        return self.tr[eng]

    
tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")

tr.remove("car")
print(*tr.translate('go'))




"""
Подвиг 2. Объявите класс Money так, чтобы объекты этого класса можно было создавать следующим образом:

my_money = Money(100)
your_money = Money(1000)
Здесь при создании объектов указывается количество денег, которое должно сохраняться в локальном свойстве (атрибуте) money каждого экземпляра класса.
"""

class Money:
    def __init__(self, money):
        self.money = money


"""
Подвиг 3. Объявите класс Point так, чтобы объекты этого класса можно было создавать командами:

p1 = Point(10, 20)
p2 = Point(12, 5, 'red')
Здесь первые два значения - это координаты точки на плоскости (локальные свойства x, y), а третий необязательный аргумент - цвет точки (локальное свойство color). Если цвет не указывается, то он по умолчанию принимает значение black.

Создайте тысячу таких объектов с координатами (1, 1), (3, 3), (5, 5), ... то есть, с увеличением на два для каждой новой точки. Каждый объект следует поместить в список points (по порядку). Для второго объекта в списке points укажите цвет 'yellow'.
"""

class Point:

    def __init__(self, x, y, value='black'):
        self.x = x
        self.y = y
        self.color = value

points = [Point(i, i) for i in range(1, 2000, 2)]
points[1].color = 'yellow'


"""
Подвиг 4. Объявите три класса геометрических фигур: Line, Rect, Ellipse. Должна быть возможность создавать объекты каждого класса следующими командами:

g1 = Line(a, b, c, d)
g2 = Rect(a, b, c, d)
g3 = Ellipse(a, b, c, d)
Здесь в качестве аргументов a, b, c, d передаются координаты верхнего правого и нижнего левого углов (произвольные числа). В каждом объекте координаты должны сохраняться в локальных свойствах sp (верхний правый угол) и ep (нижний левый) в виде кортежей (a, b) и (c, d) соответственно.

Сформируйте 217 объектов этих классов: для каждого текущего объекта класс выбирается случайно (или Line, или Rect, или Ellipse). Координаты также генерируются случайным образом (числовые значения). Все объекты сохраните в списке elements.

В списке elements обнулите координаты объектов только для класса Line.
"""
import random

class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

figure = (Line, Rect, Ellipse)
elements = []
for i in range(217):
    a = random.randint(0,9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    d = random.randint(0, 9)
    elements.append(random.choice([Line(0, 0, 0, 0), Rect(a, b, c, d), Ellipse(a, b, c, d)] ))




"""
Подвиг 5. Объявите класс TriangleChecker, объекты которого можно было бы создавать командой:

tr = TriangleChecker(a, b, c)
Здесь a, b, c - длины сторон треугольника.

В классе TriangleChecker необходимо объявить метод is_triangle(), который бы возвращал следующие коды:

1 - если хотя бы одна сторона не число (не float или int) или хотя бы одно число меньше или равно нулю;
2 - указанные числа a, b, c не могут являться длинами сторон треугольника;
3 - стороны a, b, c образуют треугольник.

Проверку параметров a, b, c проводить именно в таком порядке.

Прочитайте из входного потока строку, содержащую три числа, разделенных пробелами, командой:

a, b, c = map(int, input().split())
Затем, создайте объект tr класса TriangleChecker и передайте ему прочитанные значения a, b, c. Вызовите метод is_triangle() из объекта tr и выведите результат на экран (код, который она вернет).
"""

class TriangleChecker:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def  is_triangle(self):
        if not all(map(lambda x: type(x) in (int, float), (self.a, self.b, self.c))) or (int(self.a) <=0 or int(self.b) <=0 or int(self.c) <=0):
            return 1
        elif int(self.a) >= int(self.b)+int(self.c) or int(self.b)>=int(self.a)+int(self.c) or int(self.c)>=int(self.a)+int(self.b):
            return 2
        else:
            return 3
            
a, b, c = map(int, input().split()) 
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())


"""
Подвиг 6. Объявите класс Graph, объекты которого можно было бы создавать с помощью команды:

gr_1 = Graph(data)
где data - список из числовых данных (данные для графика). При создании каждого экземпляра класса должны формироваться следующие локальные свойства:

data - ссылка на список из числовых данных (у каждого объекта должен быть свой список с данными, нужно создавать копию переданного списка);
is_show - булево значение (True/False) для показа (True) и сокрытия (False) данных графика (по умолчанию True);

В этом классе объявите следующие методы:

set_data(self, data) - для передачи нового списка данных в текущий график;
show_table(self) - для отображения данных в виде строки из списка чисел (числа следуют через пробел);
show_graph(self) - для отображения данных в виде графика (метод выводит в консоль сообщение: "Графическое отображение данных: <строка из чисел следующих через пробел>");
show_bar(self) - для отображения данных в виде столбчатой диаграммы (метод выводит в консоль сообщение: "Столбчатая диаграмма: <строка из чисел следующих через пробел>");
set_show(self, fl_show) - метод для изменения локального свойства is_show на переданное значение fl_show.

Если локальное свойство is_show равно False, то методы show_table(), show_graph() и show_bar() должны выводить сообщение:

"Отображение данных закрыто"

Прочитайте из входного потока числовые данные с помощью команды:

data_graph = list(map(int, input().split()))
Создайте объект gr класса Graph с набором прочитанных данных, вызовите метод show_bar(), затем метод set_show() со значением fl_show = False и вызовите метод show_table(). На экране должны отобразиться две соответствующие строки.
"""

class Graph:
    def __init__(self, data, is_show=True):
        self.data = data[:]
        self.is_show = is_show
        
    def set_data(self, data):
        self = Graph(data)
        
    def show_table(self):
        if self.is_show==False:
            print('Отображение данных закрыто')
        else:
            print(' '.join(self.data))
        
    def show_graph(self):
        if self.is_show==False:
            print('Отображение данных закрыто')
        else:
            string = ' '.join(self.data)
            print(f'Графическое отображение данных: {string}')
        
    def show_bar(self):
        if self.is_show==False:
            print('Отображение данных закрыто')
        else:
            string = ' '.join(map(str, self.data))
            print(f'Столбчатая диаграмма: {string}')
        
    def set_show(self, fl_show):
        self.is_show = fl_show
        
        
data_graph = list(map(int, input().split()))

gr=Graph(data_graph)
gr.show_bar()
gr.set_show(fl_show = False)
gr.show_table()


"""
Подвиг 7. Объявите в программе следующие несколько классов:

CPU - класс для описания процессоров;
Memory - класс для описания памяти;
MotherBoard - класс для описания материнских плат.

Обеспечить возможность создания объектов каждого класса командами:

cpu = CPU(наименование, тактовая частота)
mem = Memory(наименование, размер памяти)
mb = MotherBoard(наименование, процессор, память1, память2, ..., памятьN)
Обратите внимание при создании объекта класса MotherBoard можно передавать несколько объектов класса Memory, максимум N - по числу слотов памяти на материнской плате (N = 4).

Объекты классов должны иметь следующие локальные свойства: 

для класса CPU: name - наименование; fr - тактовая частота;
для класса Memory: name - наименование; volume - объем памяти;
для класса MotherBoard: name - наименование; cpu - ссылка на объект класса CPU; total_mem_slots = 4 - общее число слотов памяти (атрибут прописывается с этим значением и не меняется); mem_slots - список из объектов класса Memory (максимум total_mem_slots = 4 штук по максимальному числу слотов памяти).

Класс MotherBoard должен иметь метод get_config(self) для возвращения текущей конфигурации компонентов на материнской плате в виде следующего списка из четырех строк:

['Материнская плата: <наименование>',
'Центральный процессор: <наименование>, <тактовая частота>',
'Слотов памяти: <общее число слотов памяти>',
'Память: <наименование_1> - <объем_1>; <наименование_2> - <объем_2>; ...; <наименование_N> - <объем_N>']

Создайте объект mb класса MotherBoard с одним CPU (объект класса CPU) и двумя слотами памяти (объекты класса Memory).
"""

class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr

class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

class MotherBoard:
    def __init__(self, name, cpu, *args):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = args[:self.total_mem_slots]

    def get_config(self):
        return [f'Материнская плата:{self.name}',
                f'Центральный процессор: {self.cpu.name},{self.cpu.fr}',
                f'Слотов памяти:{self.total_mem_slots}',
                'Память:' + ';'.join(map(lambda x: f'{x.name} - {x.volume}', self.mem_slots))]


mb = MotherBoard('Most', CPU('intel', 100), Memory('Test', 1000), Memory('Test2', 1000))


"""
Подвиг 8. Объявите в программе класс Cart (корзина), объекты которого создаются командой:

cart = Cart()
Каждый объект класса Cart должен иметь локальное свойство goods - список объектов для покупки (объекты классов Table, TV, Notebook и Cup). Изначально этот список должен быть пустым.

В классе Cart объявить методы:

add(self, gd) - добавление в корзину товара, представленного объектом gd;
remove(self, indx) - удаление из корзины товара по индексу indx;
get_list(self) - получение из корзины товаров в виде списка из строк:

['<наименовние_1>: <цена_1>',
'<наименовние_2>: <цена_2>',
...
'<наименовние_N>: <цена_N>']

Объявите в программе следующие классы для описания товаров:

Table - столы;
TV - телевизоры;
Notebook - ноутбуки;
Cup - кружки.

Объекты этих классов должны создаваться командой:

gd = ИмяКласса(name, price)
Каждый объект классов товаров должен содержать локальные свойства:

name - наименование;
price - цена.

Создайте в программе объект cart класса Cart. Добавьте в него два телевизора (TV), один стол (Table), два ноутбука (Notebook) и одну кружку (Cup). Названия и цены придумайте сами. 
"""

class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f"{i.name}: {i.price}" for i in self.goods]

class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
cart.add(TV('TestTV', 100))
cart.add(TV('TestTV2', 200))
cart.add(Table('TestTable', 100))
cart.add(Notebook('TestNotebook', 100))
cart.add(Notebook('TestNotebook2', 200))
cart.add(Cup('TestCup', 100))


"""
Подвиг 9. Вам необходимо реализовать односвязный список (не список языка Python, объекты в списке не хранить, а формировать связанную структуру, показанную на рисунке) из объектов класса ListObject:



Для этого объявите в программе класс ListObject, объекты которого создаются командой:

obj = ListObject(data)
Каждый объект класса ListObject должен содержать локальные свойства:

next_obj - ссылка на следующий присоединенный объект (если следующего объекта нет, то next_obj = None);
data - данные объекта в виде строки.

В самом классе ListObject должен быть объявлен метод:

link(self, obj) - для присоединения объекта obj такого же класса к текущему объекту self (то есть, атрибут next_obj объекта self должен ссылаться на obj).

Прочитайте список строк из входного потока командой:

lst_in = list(map(str.strip, sys.stdin.readlines()))
Затем сформируйте односвязный список, в объектах которых (в атрибуте data) хранятся строки из списка lst_in (первая строка в первом объекте, вторая - во втором и  т.д.). На первый добавленный объект класса ListObject должна ссылаться
"""
import sys

class ListObject:
    def __init__(self, data):
        self.data = data
        self. next_obj = None

    def link(self, obj):
        self. next_obj = obj

lst_in = list(map(str.strip, sys.stdin.readlines()))

head_obj = ListObject(lst_in[0])
obj = head_obj
for i in range(1, len(lst_in)):
    obj_new = ListObject(lst_in[i])
    obj.link(obj_new)
    obj = obj_new


"""
ольшой подвиг 10. Объявите два класса: 

Cell - для представления клетки игрового поля;
GamePole - для управления игровым полем, размером N x N клеток.

С помощью класса Cell предполагается создавать отдельные клетки командой:

c1 = Cell(around_mines, mine)
Здесь around_mines - число мин вокруг данной клетки поля; mine - булева величина (True/False), означающая наличие мины в текущей клетке. При этом, в каждом объекте класса Cell должны создаваться локальные свойства:

around_mines - число мин вокруг клетки (начальное значение 0);
mine - наличие мины в текущей клетке (True/False);
fl_open - открыта/закрыта клетка - булево значение (True/False). Изначально все клетки закрыты (False).



С помощью класса GamePole должна быть возможность создавать квадратное игровое поле с числом клеток N x N:

pole_game = GamePole(N, M)
Здесь N - размер поля; M - общее число мин на поле. При этом, каждая клетка представляется объектом класса Cell и все объекты хранятся в двумерном списке N x N элементов - локальном свойстве pole объекта класса GamePole. 

В классе GamePole должны быть также реализованы следующие методы:

init() - инициализация поля с новой расстановкой M мин (случайным образом по игровому полю, разумеется каждая мина должна находиться в отдельной клетке).
show() - отображение поля в консоли в виде таблицы чисел открытых клеток (если клетка не открыта, то отображается символ #).

При создании экземпляра класса GamePole в его инициализаторе следует вызывать метод init() для первоначальной инициализации игрового поля.

В классе GamePole могут быть и другие вспомогательные методы.

Создайте экземпляр pole_game класса GamePole с размером поля N = 10 и числом мин M = 12. 
"""
from random import randint
class Cell:
    def __init__(self, around_mines=0,  mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False

class GamePole:
    def __init__(self,N, M):
        self._n = N
        self._m = M
        self.pole = [[Cell() for n in range(self._n)] for n in range(self._m)]
        self.init()

    def init(self):
        m = 0
        while m < self._m:
            i = randint(0, self._n - 1)
            j = randint(0, self._n - 1)
            if self.pole[i][j].mine:
                continue
            self.pole[i][j].mine = True
            m += 1
        
        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self._n):
            for y in range(self._n):
                if not self.pole[x][y].mine: 
                    mines = sum((self.pole[x+i][y+j].mine for i, j in indx if 0 <= x+i < self._n and 0 <= y+j < self._n))
                    self.pole[x][y].around_mines = mines 
    
    def show(self):
        for row in self.pole:
            print(*map(lambda x : '#' if not x.fl_open else x.around_mines if not x.mine else '*', row))


pole_game = GamePole (10, 12)
pole_game.show()  


"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/7aVqWfrAdqw

Подвиг 6. Объявите класс AbstractClass, объекты которого нельзя было бы создавать. При выполнении команды:

obj = AbstractClass()
переменная obj должна ссылаться на строку с содержимым:

"Ошибка: нельзя создавать объекты абстрактного класса"
"""
class AbstractClass:
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            return 'Ошибка: нельзя создавать объекты абстрактного класса'
            


"""
Подвиг 7. Объявите класс SingletonFive, с помощью которого можно было бы создавать объекты командой:

a = SingletonFive(<наименование>)
Здесь <наименование> - это данные, которые сохраняются в локальном свойстве name созданного объекта.

Этот класс должен формировать только первые пять объектов. Остальные (шестой, седьмой и т.д.) должны быть ссылкой на последний (пятый) созданный объект.

Создайте первые десять объектов класса SingletonFive с помощью следующего фрагмента программы:

objs = [SingletonFive(str(n)) for n in range(10)]
"""
class SingletonFive:
    __instance = None
    __count = 0
    
    def __new__(cls, *args, **kwargs):
        if cls.__count < 5:
            cls.__instance = super().__new__(cls)
            cls.__count +=1
        return cls.__instance 
        
    def __init__(self, name):
        self.name = name
        
objs = [SingletonFive(str(n)) for n in range(10)]


"""
Подвиг 8. В программе объявлена переменная TYPE_OS и два следующих класса:

TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"
Необходимо объявить третий класс с именем Dialog, который бы создавал объекты командой:

dlg = Dialog(<название>)
Здесь <название> - это строка, которая сохраняется в локальном свойстве name объекта dlg.

Класс Dialog должен создавать объекты класса DialogWindows, если переменная TYPE_OS = 1 и объекты класса DialogLinux, если переменная TYPE_OS не равна 1. При этом, переменная TYPE_OS может меняться в последующих строчках программы. Имейте это в виду, при объявлении класса Dialog.

P.S. В программе на экран ничего выводить не нужно. Только объявить класс Dialog.
"""
TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"
    

class DialogLinux:
    name_class = "DialogLinux"
    
    
class Dialog:
    
    def __new__(cls, *args, **kwargs):
        obj = None
        if TYPE_OS == 1:
            obj = super().__new__(DialogWindows)
        else:
            obj = super().__new__(DialogLinux)
            
        obj.name = args[0]
        return obj


"""
одвиг 9 (на повторение материала). Объявите класс Point для представления точек на плоскости. Создавать объекты этого класса предполагается командой:

pt = Point(x, y)
Здесь x, y - числовые координаты точки на плоскости (числа), то есть, в каждом объекте этого класса создаются локальные свойства x, y, которые хранят конкретные координаты точки.

Необходимо в классе Point реализовать метод clone(self), который бы создавал новый объект класса Point как копию текущего объекта с локальными атрибутами x, y и соответствующими значениями.

Создайте в программе объект pt класса Point и еще один объект pt_clone через вызов метода clone.

P.S. В программе на экран ничего выводить не нужно.
"""
class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def clone(self):
        return Point(self.x, self.y)
        
pt = Point(10,20)
pt_clone = Point.clone(pt)


"""
Подвиг 10 (на повторение материала). В программе предполагается реализовать парсер (обработчик) строки (string) в определенный выходной формат. Для этого объявлен следующий класс:

class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq

И предполагается его использовать следующим образом:

ld = Loader()
res = ld.parse_format("4, 5, -6.5", Factory())
На выходе (в переменной res) ожидается получить список из набора вещественных чисел. Например, для заданной строки, должно получиться:

[4.0, 5.0, -6.5]

Для реализации этой идеи необходимо вначале программы прописать класс Factory с двумя методами:

build_sequence(self) - для создания начального пустого списка (метод должен возвращать пустой список);
build_number(self, string) - для преобразования переданной в метод строки (string) в вещественное значение (метод должен возвращать полученное вещественное число).

Объявите класс с именем Factory, чтобы получать на выходе искомый результат.
"""


class Factory:
    def build_sequence(self):
        self.a = []
        return self.a
        
    def build_number(self, string):
        return float(string)


class Loader:
   
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


# эти строчки не менять!
ld = Loader()
s = input()
res = ld.parse_format(s, Factory())