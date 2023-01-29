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




"""
Подвиг 6. В программе предполагается реализовать парсер (обработчик) строки с данными string в определенный выходной формат. Для этого объявлен следующий класс:

class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq
И предполагается его использовать следующим образом:

res = Loader.parse_format("4, 5, -6", Factory)
На выходе (в переменной res) ожидается получать список из набора целых чисел. Например, для заданной строки, должно получиться:

[4, 5, -6]

Для реализации этой идеи необходимо вначале программы прописать класс Factory с двумя статическими методами:

build_sequence() - для создания пустого списка (метод возвращает пустой список);
build_number(string) - для преобразования строки (string) в целое число (метод возвращает полученное целочисленное значение).

Объявите класс с именем Factory, чтобы получать на выходе искомый результат.

P.S. В программе на экран ничего выводить не нужно.
"""

class Factory:
    def build_sequence():
        return []
        
    def build_number(string):
        return int(string)

class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


# эти строчки не менять!
res = Loader.parse_format("1, 2, 3, -5, 10", Factory)



"""
Подвиг 7. В программе объявлен следующий класс для работы с формами ввода логин/пароль:

class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])
Который предполагается использовать следующим образом:

login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()
Необходимо прописать классы TextInput и PasswordInput, объекты которых формируются командами:

login = TextInput(name, size)
psw = PasswordInput(name, size)
В каждом объекте этих классов должны быть следующие локальные свойства:

name - название для поля (сохраняет передаваемое имя, например, "Логин" или "Пароль");
size - размер поля ввода (целое число, по умолчанию 10).

Также классы TextInput и PasswordInput должны иметь метод:

get_html(self) - возвращает сформированную HTML-строку в формате (1-я строка для класса TextInput ; 2-я - для класса PasswordInput):

<p class='login'><имя поля>: <input type='text' size=<размер поля> />
<p class='password'><имя поля>: <input type='text' size=<размер поля> />

Например, для поля login:

<p class='login'>Логин: <input type='text' size=10 />

Также классы TextInput и PasswordInput должны иметь метод класса (@classmethod):

check_name(cls, name) - для проверки корректности переданного имя поля (следует вызывать в инициализаторе) по следующим критериям:

- длина имени не менее 3 символов и не более 50;
- в именах могут использоваться только символы русского, английского алфавитов, цифры и пробелы

Если проверка не проходит, то генерировать исключение командой:

raise ValueError("некорректное поле name")
Для проверки допустимых символов в каждом классе должен быть прописан атрибут CHARS_CORRECT:

CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
CHARS_CORRECT = CHARS + CHARS.upper() + digits
По заданию нужно объявить только классы TextInput и PasswordInput с соответствующим функционалом. Более ничего.

P. S. В данном задании получится дублирование кода в классах TextInput и PasswordInput. На данном этапе - это нормально.
"""

from string import ascii_lowercase, digits

# здесь объявляйте классы TextInput и PasswordInput
class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits   
    
    def __init__(self, name, size=10):
        self.check_name(name)
        self.name = name
        self.size = size
        
    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"
        
    @classmethod
    def check_name(cls, name):
        if type(name) != str or len(name) < 3 or len(name) > 50:
            raise ValueError("некорректное поле name")
            
        if not set(name) < set(cls.CHARS_CORRECT):
            raise ValueError("некорректное поле name")


class PasswordInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits   
    
    def __init__(self, name, size=10):
        self.check_name(name)
        self.name = name
        self.size = size
        
    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"
        
    @classmethod
    def check_name(cls, name):
        if type(name) != str or len(name) < 3 or len(name) > 50:
            raise ValueError("некорректное поле name")
            
        if not set(name) < set(cls.CHARS_CORRECT):
            raise ValueError("некорректное поле name")



class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()



"""
Подвиг 8. Объявите класс CardCheck для проверки корректности информации на пластиковых картах. Этот класс должен иметь следующие методы:

check_card_number(number) - проверяет строку с номером карты и возвращает булево значение True, если номер в верном формате и False - в противном случае. Формат номера следующий: XXXX-XXXX-XXXX-XXXX, где X - любая цифра (от 0 до 9).
check_name(name) - проверяет строку name с именем пользователя карты. Возвращает булево значение True, если имя записано верно и False - в противном случае.

Формат имени: два слова (имя и фамилия) через пробел, записанные заглавными латинскими символами и цифрами. Например, SERGEI BALAKIREV.

Предполагается использовать класс CardCheck следующим образом (эти строчки в программе не писать):

is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")
Для проверки допустимых символов в классе должен быть прописан атрибут:

CHARS_FOR_NAME = ascii_lowercase.upper() + digits
Подумайте, как правильнее объявить методы check_card_number и check_name (декораторами @classmethod и @staticmethod).

P.S. В программе только объявить класс. На экран ничего выводить не нужно.
"""
from string import ascii_lowercase, digits
import re

class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod 
    def check_card_number(number):
        if re.match(r'\d{4}-\d{4}-\d{4}-\d{4}$', number):
            return True
        else:
            return False
     
    @staticmethod      
    def check_name(name):
        if re.match(r'[A-Z]+\s[A-Z]+$', name):
            return True
        else:
            return False
            
            
is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")



"""
Подвиг 9. Объявите в программе класс Video с двумя методами:

create(self, name) - для задания имени name текущего видео (метод сохраняет имя name в локальном атрибуте name объекта класса Video);
play(self) - для воспроизведения видео (метод выводит на экран строку "воспроизведение видео <name>").

Объявите еще один класс с именем YouTube, в котором объявите два метода (с декоратором @classmethod):

add_video(cls, video) - для добавления нового видео (метод помещает объект video класса Video в список);
play(cls, video_indx) - для проигрывания видео из списка по указанному индексу (индексация с нуля).

(здесь cls - ссылка на класс YouTube). И список (тоже внутри класса YouTube):

videos - для хранения добавленных объектов класса Video (изначально список пуст).

Метод play() класса YouTube должен обращаться к объекту класса Video по индексу списка videos и, затем, вызывать метод play() класса Video.

Методы add_video и play вызывайте напрямую из класса YouTube. Создавать экземпляр этого класса не нужно.

Создайте два объекта v1 и v2 класса Video, затем, через метод create() передайте им имена "Python" и "Python ООП". После этого с помощью метода add_video класса YouTube, добавьте в него эти два видео и воспроизведите (с помощью метода play класса YouTube) сначала первое, а затем, второе видео.
"""

class Video:
 
    def create(self, name):
        self.name = name
        
    def play(self):
        print(f"воспроизведение видео {self.name}")

class YouTube:
    videos = []
    
    @classmethod
    def add_video(cls, video):
        cls.videos.append(video)
        
    @classmethod
    def play(cls, video_indx):
        cls.videos[video_indx].play()
        
v1 = Video()
v2 = Video()

v1.create('Python')
v2.create('Python ООП')

YouTube.add_video(v1)
YouTube.add_video(v2)
YouTube.play(0)
YouTube.play(1)


"""
Подвиг 10 (на повторение). Объявите класс AppStore - интернет-магазин приложений для устройств под iOS. В этом классе должны быть реализованы следующие методы:

add_application(self, app) - добавление нового приложения app в магазин;
remove_application(self, app) - удаление приложения app из магазина;
block_application(self, app) - блокировка приложения app (устанавливает локальное свойство blocked объекта app в значение True);
total_apps(self) - возвращает общее число приложений в магазине.

Класс AppStore предполагается использовать следующим образом (эти строчки в программе не писать):

store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.remove_application(app_youtube)
Здесь Application - класс, описывающий добавляемое приложение с указанным именем. Каждый объект класса Application должен содержать локальные свойства:

name - наименование приложения (строка);
blocked - булево значение (True - приложение заблокировано; False - не заблокировано, изначально False).

Как хранить список приложений в объектах класса AppStore решите сами.

P.S. В программе нужно только объявить классы с указанным функционалом.
"""

class AppStore:
    def __init__ (self):
        self.store = []
     

    def add_application(self, app):
        self.store.append(app)
        

    def remove_application(self, app):
        self.store.remove(app)
        

    def block_application(self, app):
         app.blocked = True
         

    def total_apps(self):
        return len(self.store)
        


class Application:
    
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked
        
        
store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.remove_application(app_youtube)



"""
Объявите класс для мессенджера с именем Viber. В этом классе должны быть следующие методы:

add_message(msg) - добавление нового сообщения в список сообщений;
remove_message(msg) - удаление сообщения из списка;
set_like(msg) - поставить/убрать лайк для сообщения msg (т.е. изменить атрибут fl_like объекта msg: если лайка нет то он ставится, если уже есть, то убирается);
show_last_message(число) - отображение последних сообщений;
total_messages() - возвращает общее число сообщений.

Эти методы предполагается использовать следующим образом (эти строчки в программе не писать):

msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)
Класс Message (необходимо также объявить) позволяет создавать объекты-сообщения со следующим набором локальных свойств:

text - текст сообщения (строка);
fl_like - поставлен или не поставлен лайк у сообщения (булево значение True - если лайк есть и False - в противном случае, изначально False);

P.S. Как хранить список сообщений, решите самостоятельно.
"""

class Viber:
    message = []
    
    @classmethod  
    def add_message(cls, msg):
        cls.message.append(msg)
     
    @classmethod    
    def remove_message(cls, msg):
        cls.message.remove(msg)
    
    @classmethod      
    def set_like(cls, msg):
        msg.fl_like = not msg.fl_like
    
    @classmethod          
    def show_last_message(cls, x):
        print (cls.message[-x])
    
    @classmethod      
    def total_messages(cls):
        return len(cls.message)
    
    
    
class Message :
    def __init__(self, text, fl_like = False):
        self.text = text
        self.fl_like = fl_like
        
        
msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)



"""
Время первого испытания. Представьте, что вы получили задание от заказчика. Вас просят реализовать простую имитацию локальной сети, состоящую из набора серверов, соединенных между собой через роутер.



Каждый сервер может отправлять пакет любому другому серверу сети. Для этого у каждого есть свой уникальный IP-адрес. Для простоты - это просто целое (натуральное) число от 1 и до N, где N - общее число серверов. Алгоритм следующий. Предположим, сервер с IP = 2 собирается отправить пакет информации серверу с IP = 3. Для этого, он сначала отправляет пакет роутеру, а уже тот, смотрит на IP-адрес и пересылает пакет нужному узлу (серверу).

Для реализации этой схемы программе предлагается объявить три класса:

Server - для описания работы серверов в сети;
Router - для описания работы роутеров в сети (в данной задаче полагается один роутер);
Data - для описания пакета информации.

Серверы будут создаваться командой:

sv = Server()
При этом, уникальный IP-адрес каждого сервера должен формироваться автоматически при создании нового экземпляра класса Server.

Далее, роутер должен создаваться аналогичной командой:

router = Router()
А, пакеты данных, командой:

data = Data(строка с данными, IP-адрес назначения)
Для формирования и функционирования локальной сети, в классе Router должны быть реализованы следующие методы:

link(server) - для присоединения сервера server (объекта класса Server) к роутеру (для простоты, каждый сервер соединен только с одним роутером);
unlink(server) - для отсоединения сервера server (объекта класса Server) от роутера;
send_data() - для отправки всех пакетов (объектов класса Data) из буфера роутера соответствующим серверам (после отправки буфер должен очищаться).

И одно обязательное локальное свойство (могут быть и другие свойства):

buffer - список для хранения принятых от серверов пакетов (объектов класса Data).

Класс Server должен содержать свой набор методов:

send_data(data) - для отправки информационного пакета data (объекта класса Data) с указанным IP-адресом получателя (пакет отправляется роутеру и сохраняется в его буфере - локальном свойстве buffer);
get_data() - возвращает список принятых пакетов (если ничего принято не было, то возвращается пустой список) и очищает входной буфер;
get_ip() - возвращает свой IP-адрес.

Соответственно в объектах класса Server должны быть локальные свойства:

buffer - список принятых пакетов (объекты класса Data, изначально пустой);
ip - IP-адрес текущего сервера.

Наконец, объекты класса Data должны содержать два следующих локальных свойства:

data - передаваемые данные (строка);
ip - IP-адрес назначения.
"""

class Router:
    def __init__(self):
        self.buffer = []
        self.servers = {}
        
    def link(self, server):
        self.servers[server.ip] = server
        server.router = self
        
    def unlink(self, server):
        s = self.servers.pop(server.ip, False)
        if s:
            s.router = None
            
    def send_data(self):
        for d in self.buffer:
            if d.ip in self.servers:
                self.servers[d.ip].buffer.append(d)
        self.buffer.clear()
        
        
class Server:
    server_ip = 1
    
    def __init__(self):
        self.buffer = []
        self.ip = Server.server_ip
        Server.server_ip += 1
        self.router = None
        
    def send_data(self, data):
        if self.router:
            self.router.buffer.append(data)
            
    def get_data(self):
        b = self.buffer[:]
        self.buffer.clear()
        return b
        
    def get_ip(self):
        return self.ip
        
class Data:
    def __init__(self, msg, ip):
        self.data = msg
        self.ip = ip


"""
Подвиг 3. Объявите класс с именем Clock и определите в нем следующие переменные и методы:

- приватная локальная переменная time для хранения текущего времени, целое число (своя для каждого объекта класса Clock с начальным значением 0);
- публичный метод set_time(tm) для установки текущего времени (присваивает значение tm приватному локальному свойству time, если метод check_time(tm) возвратил True);
- публичный метод get_time() для получения текущего времени из приватной локальной переменной time;
- приватный метод класса check_time(tm) для проверки корректности времени в переменной tm (возвращает True, если значение корректно и False - в противном случае).

Проверка корректности выполняется по критерию: tm должна быть целым числом, больше или равна нулю и меньше 100 000.

Объекты класса Clock предполагается использовать командой:

clock = Clock(время)
Создайте объект clock класса Clock и установите время, равным 4530.
"""

class Clock :
    def __init__(self, tm):
        self.__time = 0
        if self.__check_time(tm):
            self.__time = tm
    @classmethod
    def __check_time(cls, tm):
        return type(tm)==int and 0 <= tm < 100000
    
    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm
        
    def  get_time(self):
        return self.__time
        
            
clock = Clock(4530)

"""
Подвиг 4. Объявите класс с именем Money и определите в нем следующие переменные и методы:

- приватная локальная переменная money (целочисленная) для хранения количества денег (своя для каждого объекта класса Money);
- публичный метод set_money(money) для передачи нового значения приватной локальной переменной money (изменение выполняется только если метод check_money(money) возвращает значение True);
- публичный метод get_money() для получения текущего объема средств (денег);
- публичный метод add_money(mn) для прибавления средств из объекта mn класса Money к средствам текущего объекта;
- приватный метод класса check_money(money) для проверки корректности объема средств в параметре money (возвращает True, если значение корректно и False - в противном случае).

Проверка корректности выполняется по критерию: параметр money должен быть целым числом, больше или равным нулю.
"""
class Money :
    def __init__(self, money):
        self.__money = money
        
    @classmethod
    def check_money(cls,money):
        return type(money) == int and money >= 0

    def set_money(self, money):
        if self.check_money(money):
            self.__money = money

    def get_money(self):
        return self.__money

    def add_money(self, mn):
        self.__money += mn.get_money()
            

mn_1 = Money(10)
mn_2 = Money(20)
mn_1.set_money(100)
mn_2.add_money(mn_1)
m1 = mn_1.get_money()    # 100
m2 = mn_2.get_money()    # 120


"""
Подвиг 6. Объявите класс Book со следующим набором сеттеров и геттеров:

set_title(self, title) - запись в локальное приватное свойство __title объектов класса Book значения title;
set_author(self, author) - запись в локальное приватное свойство __author объектов класса Book значения author;
set_price(self, price) - запись в локальное приватное свойство __price объектов класса Book значения price;
get_title(self) - получение значения локального приватного свойства __title объектов класса Book;
get_author(self) - получение значения локального приватного свойства __author объектов класса Book;
get_price(self) - получение значения локального приватного свойства __price объектов класса Book;
"""
class Book:
    def __init__(self, author, title, price):
        self.__author = author
        self.__title = title
        self.__price = price

    def set_title(self, title):
        self.__title = title
    
    def set_author(self, author):
        self.__author = author

    def set_price(self, price):
        self.__price = price

    def get_title(self):
        return self.__title 

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price
    

"""
Подвиг 7. Объявите класс Line для описания линии на плоскости, объекты которого предполагается создавать командой:

line = Line(x1, y1, x2, y2)
При этом в объекте line должны создаваться следующие приватные локальные свойства:

__x1, __y1 - начальная координата;
__x2, __y2 - конечная координата.

В самом классе Line должны быть реализованы следующие сеттеры и геттеры:

set_coords(self, x1, y1, x2, y2) - для изменения координат линии;
get_coords(self) - для получения кортежа из текущих координат линии.

А также метод:

draw(self) - для отображения в консоли списка текущих координат линии (в одну строчку через пробел).

P.S. В программе требуется объявить только класс. Ничего на экран выводить не нужно.
"""
class Line():
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def set_coords(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_coords(self):
        return  self.__x1, self.__y1, self.__x2, self.__y2

    def draw(self):
        print (*self.get_coords())


"""
Подвиг 8. Объявите в программе два класса Point и Rectangle. Объекты первого класса должны создаваться командой:

pt = Point(x, y)
где x, y - координаты точки на плоскости (целые или вещественные числа). При этом в объектах класса Point должны формироваться следующие локальные свойства:

__x, __y - координаты точки на плоскости.

и один геттер:

get_coords() - возвращение кортежа текущих координат __x, __y

Объекты второго класса Rectangle (прямоугольник) должны создаваться командами:

r1 = Rectangle(Point(x1, y1), Point(x2, y2))
или

r2 = Rectangle(x1, y1, x2, y2)
Здесь первая координата (x1, y1) - верхний левый угол, а вторая координата (x2, y2) - правый нижний. При этом, в объектах класса Rectangle (вне зависимости от способа их создания) должны формироваться следующие локальные свойства:

__sp - объект класса Point с координатами x1, y1 (верхний левый угол);
__ep - объект класса Point с координатами x2, y2 (нижний правый угол).

Также к классе Rectangle должны быть реализованы следующие методы:

set_coords(self, sp, ep) - изменение текущих координат, где sp, ep - объекты класса Point;
get_coords(self) - возвращение кортежа из объектов класса Point с текущими координатами прямоугольника (ссылки на локальные свойства __sp и __ep);
draw(self) - отображение в консоли сообщения: "Прямоугольник с координатами: (x1, y1) (x2, y2)". Здесь x1, y1, x2, y2 - соответствующие числовые значения координат.

Создайте объект rect класса Rectangle с координатами (0, 0), (20, 34).

P.S. На экран ничего выводить не нужно.
"""
class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y

class Rectangle:
    def __init__(self, a, b, c=None, d=None):
        self.__sp = self.__ep = None
        if isinstance(a, Point) and isinstance(b, Point):
            self.__sp = a
            self.__ep = b
        elif all(map(lambda x : type(x) in (int, float), (a, b, c, d))):
            self.__sp = Point(a, b)
            self.__ep = Point(c, d)

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(f'Прямоугольник с координатами: {self.__sp.get_coords} {self.__ep.get_coords}')

rect = Rectangle((0, 0), (20, 34))


            
"""
Большой подвиг 9. Необходимо реализовать связный список (не список языка Python и не хранить объекты в списке Python), когда объекты класса ObjList связаны с соседними через приватные свойства __next и __prev:



Для этого объявите класс LinkedList, который будет представлять связный список в целом и иметь набор следующих методов:

add_obj(self, obj) - добавление нового объекта obj класса ObjList в конец связного списка;
remove_obj(self) - удаление последнего объекта из связного списка;
get_data(self) - получение списка из строк локального свойства __data всех объектов связного списка.

И в каждом объекте этого класса должны создаваться локальные публичные атрибуты:

head - ссылка на первый объект связного списка (если список пустой, то head = None);
tail - ссылка на последний объект связного списка (если список пустой, то tail = None).

Объекты класса ObjList должны иметь следующий набор приватных локальных свойств:

__next - ссылка на следующий объект связного списка (если следующего объекта нет, то __next = None);
__prev - ссылка на предыдущий объект связного списка (если предыдущего объекта нет, то __prev = None);
__data - строка с данными.

Также в классе ObjList должны быть реализованы следующие сеттеры и геттеры:

set_next(self, obj) - изменение приватного свойства __next на значение obj;
set_prev(self, obj) - изменение приватного свойства __prev на значение obj;
get_next(self) - получение значения приватного свойства __next;
get_prev(self) - получение значения приватного свойства __prev;
set_data(self, data) - изменение приватного свойства __data на значение data;
get_data(self) - получение значения приватного свойства __data.

Создавать объекты класса ObjList предполагается командой:

ob = ObjList("данные 1")
А использовать класс LinkedList следующим образом (пример, эти строчки писать в программе не нужно):

lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']
Объявите в программе классы LinkedList и ObjList в соответствии с заданием.

P.S. На экран ничего выводить не нужно.
"""
class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__next = self.__prev = None

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data
    
    def get_data(self):
        return self.__data

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.tail:
            self.tail.set_next(obj)
        obj.set_prev(self.tail)
        self.tail = obj
        if not self.head:
            self.head = obj

    def remove_obj(self):
        if self.tail is None:
            return

        prev = self.tail.get_prev()
        if prev:
            prev.set_next(None)

        self.tail = prev
        if self.tail is None:
            self.head = None

    def get_data(self):
        s = []
        h = self.head
        while h:
            s.append(h.get_data())
            h = h.get_next()
        return s


"""
Подвиг 10 (на повторение). Объявите класс EmailValidator для проверки корректности email-адреса. Необходимо запретить создание объектов этого класса: при создании экземпляров должно возвращаться значение None, например:

em = EmailValidator() # None
В самом классе реализовать следующие методы класса (@classmethod):

get_random_email(cls) - для генерации случайного email-адреса по формату: xxxxxxx...xxx@gmail.com, где x - любой допустимый символ в email (латинский буквы, цифры, символ подчеркивания и точка);
check_email(cls, email) - возвращает True, если email записан верно и False - в противном случае.

Корректность строки email определяется по следующим критериям:

- допустимые символы: латинский алфавит, цифры, символы подчеркивания, точки и собачка @ (одна);
- длина email до символа @ не должна превышать 100 (сто включительно);
- длина email после символа @ не должна быть больше 50 (включительно);
- после символа @ обязательно должна идти хотя бы одна точка;
- не должно быть двух точек подряд.

Также в классе нужно реализовать приватный статический метод класса:

is_email_str(email) - для проверки типа переменной email, если строка, то возвращается значение True, иначе - False.

Метод is_email_str() следует использовать в методе check_email() перед проверкой корректности email. Если параметр email не является строкой, то check_email() возвращает False.

Пример использования класса EmailValidator (эти строчки в программе писать не нужно):

res = EmailValidator.check_email("sc_lib@list.ru") # True
res = EmailValidator.check_email("sc_lib@list_ru") # False
P.S. В программе требуется объявить только класс. На экран ничего выводить не нужно. 
"""
from string import ascii_lowercase, ascii_uppercase, digits
from random import randint

class EmailValidator :
    EMAIL_CHARS = ascii_lowercase + ascii_uppercase + digits + "_.@"
    EMAIL_RANDOM_CHARS = ascii_lowercase + ascii_uppercase + digits + "_"
    
    def __new__(cls, *args, **kwargs):
        return None
    
    @classmethod   
    def get_random_email(cls):
        n = randint(4, 20)
        length = len(cls.EMAIL_RANDOM_CHARS) - 1
        return ''.join(cls.EMAIL_RANDOM_CHARS[randint(0, length)] for i in range(n)) + "@gmail.com"
        
        
    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        
        if not set(email) < set(cls.EMAIL_CHARS):
            return False
            
        s = email.split('@')
        if len(s) != 2:
            return False
            
        if len(s[0]) > 100 or len(s[1]) > 50:
            return False
            
        if "." not in s[1]:
            return False
            
        if email.count('..') > 0:
            return False
        
        return True
 
    @staticmethod       
    def __is_email_str(email):
        return type(email) == str

"""
Подвиг 4. Объявите в программе класс Car, в котором реализуйте объект-свойство с именем model для записи и считывания информации о модели автомобиля из локальной приватной переменной __model.

Объект-свойство объявите с помощью декоратора @property. Также в объекте-свойстве model должны быть реализованы проверки:

- модель автомобиля - это строка;
- длина строки модели должна быть в диапазоне [2; 100].

Если проверка не проходит, то локальное свойство __model остается без изменений.

Объекты класса Car предполагается создавать командой:

car = Car()
и далее работа с объектом-свойством, например:

car.model = "Toyota"
P.S. В программе объявить только класс. На экран ничего выводить не нужно. 
"""
class Car:
    def __init__(self, model=None):
        self.__model = model
        
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model (self, model):
        if type(model) == str and (2 <len(model) < 100):
            self.__model = model
            
car = Car()
car.model = "Toyota"


"""
Подвиг 5. Объявите в программе класс WindowDlg, объекты которого предполагается создавать командой:

wnd = WindowDlg(заголовок окна, ширина, высота)
В каждом объекте класса WindowDlg должны создаваться приватные локальные атрибуты:

__title - заголовок окна (строка);
__width, __height - ширина и высота окна (числа).

В классе WindowDlg необходимо реализовать метод:

show() - для отображения окна на экране (выводит в консоль строку в формате: "<Заголовок>: <ширина>, <высота>", например "Диалог 1: 100, 50").

Также в классе WindowDlg необходимо реализовать два объекта-свойства:

width - для изменения и считывания ширины окна;
height - для изменения и считывания высоты окна.

При изменении размеров окна необходимо выполнять проверку:

- переданное значение является целым числом в диапазоне [0; 10000].

Если хотя бы один размер изменился (высота или ширина), то следует выполнить автоматическую перерисовку окна (вызвать метод show()). При начальной инициализации размеров width, height вызывать метод show() не нужно.

P.S. В программе нужно объявить только класс с требуемой функциональностью.
"""
class WindowDlg:
    def __init__(self, title, width=None, height=None):
        self.__title = title
        self.__width = width
        self.__height = height 
        
    @property
    def width(self):
        return self.__width
        
    @width.setter
    def width(self, value):
        if type(value) == int and 0 <= value <= 10000:
            self.__width = value
            self.show()
            
    @property
    def height(self):
        return self.__height
        
    @height.setter
    def height(self, value):
        if type(value) == int and 0 <= value <= 10000:
            self.__height = value
            self.show()
            
    def show(self):
        print (f'{self.__title}: {self.__width}, {self.__height}')


"""
Подвиг 6. Реализуйте односвязный список (не список Python, не использовать список Python для хранения объектов), когда один объект ссылается на следующий и так по цепочке до последнего:



Для этого объявите в программе два класса: 

StackObj - для описания объектов односвязного списка;
Stack - для управления односвязным списком.

Объекты класса StackObj предполагается создавать командой:

obj = StackObj(данные)
Здесь данные - это строка с некоторым содержимым. Каждый объект класса StackObj должен иметь следующие локальные приватные атрибуты:

__data - ссылка на строку с данными, указанными при создании объекта;
__next - ссылка на следующий объект класса StackObj (при создании объекта принимает значение None).

Также в классе StackObj должны быть объявлены объекты-свойства:

next - для записи и считывания информации из локального приватного свойства __next;
data - для записи и считывания информации из локального приватного свойства __data.

При записи необходимо реализовать проверку, что __next будет ссылаться на объект класса StackObj или значение None. Если проверка не проходит, то __next остается без изменений.

Класс Stack предполагается использовать следующим образом:

st = Stack() # создание объекта односвязного списка
В объектах класса Stack должен быть локальный публичный атрибут:

top - ссылка на первый добавленный объект односвязного списка (если список пуст, то top = None).

А в самом классе Stack следующие методы:

push(self, obj) - добавление объекта класса StackObj в конец односвязного списка;
pop(self) - извлечение последнего объекта с его удалением из односвязного списка;
get_data(self) - получение списка из объектов односвязного списка (список из строк локального атрибута __data каждого объекта в порядке их добавления, или пустой список, если объектов нет).

Пример использования классов Stack и StackObj (эти строчки в программе писать не нужно):
"""
class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, obj):
        if isinstance(obj, StackObj) or obj is None:
            self.__next = obj
            
class Stack:
    def __init__(self):
        self.top = None
        self.last = None
        
    def push(self, obj):
        if self.last:
            self.last.next = obj
        self.last = obj
        if self.top is None:
            self.top = obj
            
    def pop(self):
        h = self.top
        if h is None:
            return
        while h and h.next != self.last:
            h = h.next
        if h:
            h.next = None
        last = self.last
        self.last = h
        if self.last is None:
            self.top = None
            
        return last
        
    def get_data(self):
        s = []
        h = self.top
        while h:
            s.append(h.data)
            h = h.next
        return s
        
st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()    # ['obj1', 'obj2']



"""
Подвиг 7. Объявите класс RadiusVector2D, объекты которого должны создаваться командами:

v1 = RadiusVector2D()        # радиус-вектор с координатами (0; 0)
v2 = RadiusVector2D(1)       # радиус-вектор с координатами (1; 0)
v3 = RadiusVector2D(1, 2)    # радиус-вектор с координатами (1; 2)
В каждом объекте класса RadiusVector2D должны формироваться локальные приватные атрибуты:

__x, __y - координаты конца вектора (изначально значения равны 0, если не передано какое-либо другое).

В классе RadiusVector2D необходимо объявить два объекта-свойства:

x - для изменения и считывания локального атрибута __x;
y - для изменения и считывания локального атрибута __y.

При инициализации и изменении локальных атрибутов, необходимо проверять корректность передаваемых значений:

- значение должно быть числом (целым или вещественным) в диапазоне [MIN_COORD; MAX_COORD].

Если проверка не проходит, то координаты не меняются (напомню, что при инициализации они изначально равны 0). Величины MIN_COORD = -100, MAX_COORD = 1024 задаются как публичные атрибуты класса RadiusVector2D.

Также в классе RadiusVector2D необходимо объявить статический метод:

norm2(vector) - для вычисления квадратической нормы vector - переданного объекта класса RadiusVector2D (квадратическая норма вектора: x*x + y*y).

P.S. В программе требуется объявить только класс. На экран ничего выводить не нужно.
"""

class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024


    @classmethod
    def __is_verify(cls, value):
        return type(value) in (int, float) and cls.MIN_COORD <= value <= cls.MAX_COORD
        
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__is_verify(x):
            self.__x = x
        if self.__is_verify(y):
            self.__y = y
    

    @staticmethod
    def norm2(vector):
        return vector.x * vector.x + vector.y * vector.y 

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if self.__is_verify(value):
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if self.__is_verify(value):
            self.__y = value



"""
Большой подвиг 8. Требуется реализовать программу по работе с решающими деревьями:



Здесь в каждом узле дерева делается проверка (задается вопрос). Если проверка проходит, то осуществляется переход к следующему объекту по левой стрелке (с единицей), а иначе - по правой стрелке (с нулем). И так до тех пор, пока не дойдем до одного из листа дерева (вершины без потомков).

В качестве входных данных используется вектор (список) с бинарными значениями: 1 - да, 0 - нет. Каждый элемент этого списка соответствует своему вопросу (своей вершине дерева), например:



Далее, этот вектор применяется к решающему дереву, следующим образом. Корневая вершина "Любит Python" с ней связан первый элемент вектора x и содержит значение 1, следовательно, мы переходим по левой ветви. Попадаем в вершину "Понимает ООП". С ней связан второй элемент вектора x со значением 0, следовательно, мы переходим по правой ветви и попадаем в вершину "будет кодером". Так как эта вершина конечная (листовая), то получаем результат в виде строки "будет кодером". По аналогии выполняется обработка вектора x с другими наборами значений 0 и 1.

Для реализации решающих деревьев в программе следует объявить два класса:

TreeObj - для описания вершин и листьев решающего дерева;
DecisionTree - для работы с решающим деревом в целом.

В классе DecisionTree должны быть реализованы (по крайне мере) два метода уровня класса (@classmethod):

def predict(cls, root, x) - для построения прогноза (прохода по решающему дереву) для вектора x из корневого узла дерева root.
def add_obj(cls, obj, node=None, left=True) - для добавления вершин в решающее дерево (метод должен возвращать добавленную вершину - объект класса TreeObj);

В методе add_obj параметры имеют, следующие значения:

obj - ссылка на новый (добавляемый) объект решающего дерева (объект класса TreeObj);
node - ссылка на объект дерева, к которому присоединяется вершина obj;
left - флаг, определяющий ветвь дерева (объекта node), к которой присоединяется объект obj (True - к левой ветви; False - к правой).

В классе TreeObj следует объявить инициализатор:

def __init__(self, indx, value=None): ...

где indx - проверяемый в вершине дерева индекс вектора x; value - значение, хранящееся в вершине (принимает значение None для вершин, у которых есть потомки - промежуточных вершин).

При этом, в каждом создаваемом объекте класса TreeObj должны автоматически появляться следующие локальные атрибуты:

indx - проверяемый индекс (целое число);
value - значение с данными (строка);
__left - ссылка на следующий объект дерева по левой ветви (изначально None);
__right - ссылка на следующий объект дерева по правой ветви (изначально None).

Для работы с локальными приватными атрибутами __left и __right необходимо объявить объекты-свойства с именами left и right
"""

class TreeObj:
    def __init__(self, indx, value=None):
        self.index = indx
        self.value = value
        self.left = self.right = None
        

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, obj):
        self.__left = obj

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, obj):
        self.__right = obj


class DecisionTree:
    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if node:
            if left:
                node.left = obj
            else:
                node.right = obj
        return obj

    @classmethod
    def get_next(cls, obj, x):
        if x[obj.index] == 1:
            return obj.left
        return obj.right


    @classmethod
    def predict(cls, root, x):
        obj = root
        while obj:
            obj_next = cls.get_next(obj, x)
            if obj_next is None:
                break
            obj = obj_next

        return obj.value



"""
Подвиг 9 (на закрепление). Вам требуется сформировать класс PathLines для описания маршрутов, состоящих из линейных сегментов. При этом каждый линейный сегмент предполагается задавать отдельным классом LineTo. Объекты этого класса будут формироваться командой:

line = LineTo(x, y)
где x, y - следующая координата линейного участка (начало маршрута из точки 0, 0).

В каждом объекте класса LineTo должны формироваться локальные атрибуты:

x, y - для хранения координат конца линии (начало определяется по координатам предыдущего объекта).

Объекты класса PathLines должны создаваться командами:

p = PathLines()                   # начало маршрута из точки 0, 0
p = PathLines(line1, line2, ...)  # начало маршрута из точки 0, 0
где line1, line2, ... - объекты класса LineTo.

Сам же класс PathLines должен иметь следующие методы:

get_path() - возвращает список из объектов класса LineTo (если объектов нет, то пустой список);
get_length() - возвращает суммарную длину пути (сумма длин всех линейных сегментов);
add_line(self, line) - добавление нового линейного сегмента (объекта класса LineTo) в конец маршрута.

Пояснение: суммарный маршрут - это сумма длин всех линейных сегментов, а длина каждого линейного сегмента определяется как евклидовое расстояние по формуле:

L = sqrt((x1-x0)^2 + (y1-y0)^2)

где x0, y0 - предыдущая точка маршрута; x1, y1 - текущая точка маршрута.

Пример использования классов (эти строчки в программе писать не нужно):

p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
dist = p.get_length()
P.S. В программе требуется объявить только классы. На экран ничего выводить не нужно. 
"""
class PathLines:
    def __init__(self, *args):
        self.coords = list((LineTo(0, 0), ) + args)


    def get_path(self):
        return self.coords[1:]

    def get_length(self):
        g = ((self.coords[i - 1], self.coords[i]) for i in range(1, len(self.coords)))
        return sum(map(lambda t: ((t[0].x - t[1].x) **2 + (t[0].y - t[1].y) **2) **0.5, g))

    def add_line(self, line):
        self.coords.append(line)



class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


"""
Подвиг 10 (на закрепление). Вы создаете телефонную записную книжку. Она определяется классом PhoneBook. Объекты этого класса создаются командой:

p = PhoneBook()
А сам класс должен иметь следующий набор методов:

add_phone(phone) - добавление нового номера телефона (в список);
remove_phone(indx) - удаление номера телефона по индексу списка;
get_phone_list() - получение списка из объектов всех телефонных номеров.

Каждый номер телефона должен быть представлен классом PhoneNumber. Объекты этого класса должны создаваться командой:

note = PhoneNumber(number, fio)
где number - номер телефона (число) в формате XXXXXXXXXXX (одиннадцати цифр, X - цифра); fio - Ф.И.О. владельца номера (строка).

В каждом объекте класса PhoneNumber должны формироваться локальные атрибуты:

number - номер телефона (число);
fio - ФИО владельца номера телефона.

Необходимо объявить два класса PhoneBook и PhoneNumber в соответствии с заданием.

Пример использования классов (эти строчки в программе писать не нужно):
"""

class PhoneBook:
    def __init__(self, *args):
        self.list = list(args)

    def add_phone(self, phone):
        self.list.append(phone)

    def remove_phone(self, indx):
        self.list.pop(indx)

    def get_phone_list(self):
        return self.list



class PhoneNumber:
    def __init__(self, number, fio):
           self.check_number(number)
           self.check_fio(fio)
           self.number = number
           self.fio = fio

    @staticmethod 
    def check_number(number):
        if re.match(r'^\d{11}$', number):
            return True
        else:
            return False

    @staticmethod
    def check_fio(fio):
        if type(fio) == str:
            return True
        else:
            return False



"""
Подвиг 6. Объявите дескриптор данных FloatValue, который бы устанавливал и возвращал вещественные значения. При записи вещественного числа должна выполняться проверка на вещественный тип данных. Если проверка не проходит, то генерировать исключение командой:

raise TypeError("Присваивать можно только вещественный тип данных.")
Объявите класс Cell, в котором создается объект value дескриптора FloatValue. А объекты класса Cell должны создаваться командой:

cell = Cell(начальное значение ячейки)
Объявите класс TableSheet, с помощью которого создается таблица из N строк и M столбцов следующим образом:

table = TableSheet(N, M)
Каждая ячейка этой таблицы должна быть представлена объектом класса Cell, работать с вещественными числами через объект value (начальное значение должно быть 0.0).

В каждом объекте класса TableSheet должен формироваться локальный атрибут:

cells - список (вложенный) размером N x M, содержащий ячейки таблицы (объекты класса Cell).

Создайте объект table класса TableSheet с размером таблицы N = 5, M = 3. Запишите в эту таблицу числа от 1.0 до 15.0 (по порядку).

P.S. На экран в программе выводить ничего не нужно.
"""
class FloatValue: 
    @classmethod
    def check(cls, value):
        if type(value) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")
            
    def __set_name__(self, owner, name):
        self.name = "_" + name
 
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
 
    def __set__(self, instance, value):
        self.check(value)
        setattr(instance, self.name, value)
        
class Cell:
    value = FloatValue()
    
    def __init__(self, value=0.0):
        self.value = value
        
class TableSheet:
    def __init__(self, N, M):
        self.cells = [[Cell() for _ in range(M)] for _ in range(N)]
        
        
        
table = TableSheet(5, 3)
n = 1.0
for i in range(5):
    for j in range(3):
        table.cells[i][j].value = n
        n += 1.0


"""
Подвиг 7. Объявите класс ValidateString для проверки корректности переданной строки. Объекты этого класса создаются командой:

validate = ValidateString(min_length=3, max_length=100)
где min_length - минимальное число символов в строке; max_length - максимальное число символов в строке.
В классе ValidateString должен быть реализован метод:

validate(self, string) - возвращает True, если string является строкой (тип str) и длина строки в пределах [min_length; max_length]. Иначе возвращается False.

Объявите дескриптор данных StringValue для работы со строками, объекты которого создаются командой:

st = StringValue(validator=ValidateString(min_length, max_length))
При каждом присвоении значения объекту st должен вызываться валидатор (объект класса ValidateString) и с помощью метода validate() проверяться корректность присваиваемых данных. Если данные некорректны, то присвоение не выполняется (игнорируется).

Объявите класс RegisterForm с тремя объектами дескриптора StringValue:

login = StringValue(...) - для ввода логина;
password = StringValue(...)  - для ввода пароля;
email = StringValue(...)  - для ввода Email.

Объекты класса RegisterForm создаются командой:

form = RegisterForm(логин, пароль, email)
где логин, пароль, email - начальные значения логина, пароля и Email.
В классе RegisterForm также должны быть объявлены методы:

get_fields() - возвращает список из значений полей в порядке [login, password, email];
show() - выводит в консоль многострочную строку в формате:

<form>
Логин: <login>
Пароль: <password>
Email: <email>
</form>

P.S. В программе требуется объявить классы с описанным функционалом. На экран в программе выводить ничего не нужно.
"""

class ValidateString:
    def __init__(self, min_length=3, max_length=100):
        self.min_length = min_length
        self.max_length = max_length
    
    def validate(self, string):
        return type(string) == str and self.min_length <= len(string) <= self.max_length    
            
class  StringValue:
    def __init__(self, validator):
        self.validator = validator
        
    def __set_name__(self, owner, name):
        self.name = "_"+ name
        
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
        
    def __set__(self, instance, value):
        if self.validator.validate(value):
            return setattr(instance, self.name, value)
            
class RegisterForm:
    
    login = StringValue(validator=ValidateString())
    password = StringValue(validator=ValidateString())
    email = StringValue(validator=ValidateString())
    
    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email
        
    def get_fields(self):
        return [self.login, self.password, self.email]
        
    def show(self):
        print (f'<form>\nЛогин: {self.login}\nПароль: {self.password}\nEmail: <{self.email}\n</form>')
        
        

"""
Подвиг 8. Вы начинаете создавать интернет-магазин. Для этого в программе объявляется класс SuperShop, объекты которого создаются командой:

myshop = SuperShop(название магазина)
В каждом объекте класса SuperShop должны формироваться следующие локальные атрибуты:

name - название магазина (строка);
goods - список из товаров.

Также в классе SuperShop должны быть методы:

add_product(product) - добавление товара в магазин (в конец списка goods);
remove_product(product) - удаление товара из магазина (из списка goods).

Здесь product - это объект класса Product, описывающий конкретный товар. В этом классе следует объявить следующие дескрипторы:

name = StringValue(min_length, max_length)    # min_length - минимально допустимая длина строки; max_length - максимально допустимая длина строки
price = PriceValue(max_value)    # max_value - максимально допустимое значение

Объекты класса Product будут создаваться командой:

pr = Product(наименование, цена)
Классы StringValue и PriceValue - это дескрипторы данных. Класс StringValue должен проверять, что присваивается строковый тип с длиной строки в диапазоне [2; 50], т.е. min_length = 2, max_length = 50. Класс PriceValue должен проверять, что присваивается вещественное или целочисленное значение в диапазоне [0; 10000], т.е. max_value = 10000. Если проверки не проходят, то соответствующие (прежние) значения меняться не должны.

Пример использования класса SuperShop (эти строчки в программе писать не нужно):
"""

class StringValue:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length    

    def __set_name__(self, owner, name):
        self.name = "_"+ name
        
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
        
    def __set__(self, instance, value):
        if type(value) == str and self.min_length <= len(value) <= self.max_length:
             setattr(instance, self.name, value)
            

class  PriceValue:
    def __init__(self, max_value):
        self.max_value = max_value
        
    def __set_name__(self, owner, name):
        self.name = "_"+ name
        
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
        
    def __set__(self, instance, value):
        if type(value) in (float, int) and 0 <= value <= self.max_value:
             setattr(instance, self.name, value)


class SuperShop:
    def __init__(self, name):
        self.name = name
        self.goods = []
        
    def add_product(self, product):
        self.goods.append(product)
        
    def remove_product(self, product):
        self.goods.remove(product)
        
class Product:
    name = StringValue(2, 50)
    price = PriceValue(10000)
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    
shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 2000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")


"""
Подвиг 9 (на повторение). Необходимо объявить класс Bag (рюкзак), объекты которого будут создаваться командой:

bag = Bag(max_weight)
где max_weight - максимальный суммарный вес вещей, который выдерживает рюкзак (целое число).

В каждом объекте этого класса должен создаваться локальный приватный атрибут:

__things - список вещей в рюкзаке (изначально список пуст).

Сам же класс Bag должен иметь объект-свойство:

things - для доступа к локальному приватному атрибуту __things (только для считывания, не записи).

Также в классе Bag должны быть реализованы следующие методы:

add_thing(self, thing) - добавление нового предмета в рюкзак (добавление возможно, если суммарный вес (max_weight) не будет превышен, иначе добавление не происходит);
remove_thing(self, indx) - удаление предмета по индексу списка __things;
get_total_weight(self) - возвращает суммарный вес предметов в рюкзаке.

Каждая вещь описывается как объект класса Thing и создается командой:

t = Thing(название, вес)
где название - наименование предмета (строка); вес - вес предмета (целое или вещественное число).

В каждом объекте класса Thing должны формироваться локальные атрибуты:

name - наименование предмета;
weight - вес предмета.

Пример использования классов (эти строчки в программе писать не нужно):
"""

class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight 

class Bag:   
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__things =[]
        
    @property
    def things(self):
        return self.__things
        
    def add_thing(self, thing):
        s = self.get_total_weight()
        if s + thing.weight <= self.max_weight:
            self.__things.append(thing)
        
    def remove_thing(self, indx):
        self.__things.pop(indx)
        
    def get_total_weight(self):
        return sum(i.weight for i in self.__things)

"""
Подвиг 10 (на повторение). Необходимо написать программу для представления и управления расписанием телевизионного вещания. Для этого нужно объявить класс TVProgram, объекты которого создаются командой:

pr = TVProgram(название канала)
где название канала - это строка с названием телеканала.

В каждом объекте класса TVProgram должен формироваться локальный атрибут:

items - список из телепередач (изначально список пуст).

В самом классе TVProgram должны быть реализованы следующие методы:

add_telecast(self, tl) - добавление новой телепередачи в список items;
remove_telecast(self, indx) - удаление телепередачи по ее порядковому номеру (атрибуту __id, см. далее).

Каждая телепередача должна описываться классом Telecast, объекты которого создаются командой:

tl = Telecast(порядковый номер, название, длительность)
где порядковый номер - номер телепередачи в сетке вещания (от 1 и далее); название - наименование телепередачи; длительность - время телепередачи (в секундах - целое число).

Соответственно, в каждом объекте класса Telecast должны формироваться локальные приватные атрибуты:

__id - порядковый номер (целое число);
__name - наименование телепередачи (строка);
__duration - длительность телепередачи в секундах (целое число).

Для работы с этими приватными атрибутами в классе Telecast должны быть объявлены соответствующие объекты-свойства (property):

uid - для записи и считывания из локального атрибута __id;
name - для записи и считывания из локального атрибута __name;
duration - для записи и считывания из локального атрибута __duration.

Пример использования классов (эти строчки в программе писать не нужно):
"""

class TVProgram:
    def __init__(self, name):
        self.name = name 
        self.items = []
        
    def add_telecast(self, tl):
        self.items.append(tl)
        
    def remove_telecast(self, indx):
        x = tuple(filter(lambda y: y.uid == indx, self.items))
        for i in x:
            self.items.remove(i)
        
class Telecast:
    def __init__(self, id, name, duration):
        self.__id = id
        self.__name = name
        self.__duration = duration
        
    @property
    def uid(self):
        return self.__id
        
    @uid.setter
    def uid(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name
        
    @name.setter
    def name(self, name):
        self.__name = name
        
    @property
    def duration (self):
        return self.__duration 
        
    @duration.setter
    def duration (self, duration ):
        self.__duration  = duration 
        
        

pr = TVProgram("Первый канал")
pr.add_telecast(Telecast(1, "Доброе утро", 10000))
pr.add_telecast(Telecast(2, "Новости", 2000))
pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
for t in pr.items:
    print(f"{t.name}: {t.duration}")
    



"""
Подвиг 3. Объявите класс Book для представления информации о книге. Объекты этого класса должны создаваться командами:

book = Book()
book = Book(название, автор, число страниц, год издания)
В каждом объекте класса Book автоматически должны формироваться следующие локальные свойства:

title - заголовок книги (строка, по умолчанию пустая строка);
author - автор книги (строка, по умолчанию пустая строка);
pages - число страниц (целое число, по умолчанию 0);
year - год издания (целое число, по умолчанию 0).

Объявите в классе Book магический метод __setattr__ для проверки типов присваиваемых данных локальным свойствам title, author, pages и year. Если типы не соответствуют локальному атрибуту (например, title должна ссылаться на строку, а pages - на целое число), то генерировать исключение командой:

raise TypeError("Неверный тип присваиваемых данных.")
Создайте в программе объект book класса Book для книги:

автор: Сергей Балакирев
заголовок: Python ООП
pages: 123
year: 2022

P.S. На экран ничего выводить не нужно.
"""

class Book:
    def __init__(self, title="", author="", pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year
    
    def __setattr__(self, key, value):
        if key == ('title' or 'author') and type(value) != str:
            raise TypeError("Неверный тип присваиваемых данных.")
        if key == ('pages' or 'year') and type(value) != int:
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)


book = Book("Python ООП", "Сергей Балакирев", 123, 2022)
    

"""
Подвиг 4. Вы создаете интернет-магазин. Для этого нужно объявить два класса:

Shop - класс для управления магазином в целом;
Product - класс для представления отдельного товара.

Объекты класса Shop следует создавать командой:

shop = Shop(название магазина)
В каждом объекте класса Shop должно создаваться локальное свойство:

goods - список товаров (изначально список пустой).

А также в классе объявить методы:

add_product(self, product) - добавление нового товара в магазин (в конец списка goods);
remove_product(self, product) - удаление товара product из магазина (из списка goods);

Объекты класса Product следует создавать командой:

p = Product(название, вес, цена)
В них автоматически должны формироваться локальные атрибуты:

id - уникальный идентификационный номер товара (генерируется автоматически как целое положительное число от 1 и далее);
name - название товара (строка);
weight - вес товара (целое или вещественное положительное число);
price - цена (целое или вещественное положительное число).

В классе Product через магические методы (подумайте какие) осуществить проверку на тип присваиваемых данных локальным атрибутам объектов класса (например, id - целое число, name - строка и т.п.). Если проверка не проходит, то генерировать исключение командой:

raise TypeError("Неверный тип присваиваемых данных.")
Также в классе Product с помощью магического(их) метода(ов) запретить удаление локального атрибута id. При попытке это сделать генерировать исключение:

raise AttributeError("Атрибут id удалять запрещено.")
"""
class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)



class Product:
    _id_instance = 1
    
    def __init__(self, name, weight, price ):
        self.id = Product._id_instance
        Product._id_instance +=1
        
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        d = {'name': (str,), 'weight': (float, int), 'price': (float, int), 'id': (int,)}
        if type(value) not in d[key] or type(value) in (int, float) and value < 0:
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item == "id":
            raise AttributeError("Атрибут id удалять запрещено.")



"""
Подвиг 5. Необходимо создать программу для обучающего курса. Для этого объявляются три класса:

Course - класс, отвечающий за управление курсом в целом;
Module - класс, описывающий один модуль (раздел) курса;
LessonItem - класс одного занятия (урока).

Структура курса на уровне этих классов, приведена на рисунке ниже:



Объекты класса LessonItem должны создаваться командой:

lesson = LessonItem(название урока, число практических занятий, общая длительность урока)
Соответственно, в каждом объекте класса LessonItem должны создаваться локальные атрибуты:

title - название урока (строка);
practices - число практических занятий (целое положительное число);
duration - общая длительность урока (целое положительное число).

Необходимо с помощью магических методов реализовать следующую логику взаимодействия с объектами класса LessonItem:

1. Проверять тип присваиваемых данных локальным атрибутам. Если типы не соответствуют требованиям, то генерировать исключение командой:

raise TypeError("Неверный тип присваиваемых данных.")
2. При обращении к несуществующим атрибутам объектов класса LessonItem возвращать значение False.
3. Запретить удаление атрибутов title, practices и duration в объектах класса LessonItem.

Объекты класса Module должны создаваться командой:

module = Module(название модуля)
Каждый объект класса Module должен содержать локальные атрибуты:

name - название модуля;
lessons - список из уроков (объектов класса LessonItem), входящих в модуль (изначально список пуст).

Также в классе Module должны быть реализованы методы:

add_lesson(self, lesson) - добавление в модуль (в конец списка lessons) нового урока (объекта класса LessonItem);
remove_lesson(self, indx) - удаление урока по индексу в списке lessons.

Наконец, объекты класса Course создаются командой:

course = Course(название курса)
И содержат следующие локальные атрибуты:

name - название курса (строка);
modules - список модулей в курсе (изначально список пуст).

Также в классе Course должны присутствовать следующие методы:

add_module(self, module) - добавление нового модуля в конце списка modules;
remove_module(self, indx) - удаление модуля из списка modules по индексу в этом списке.
"""
class LessonItem:
    attrs = {"title":str, "practices":int, "duration":int}
    
    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration
        
    def __setattr__(self, key, value):
        if key in self.attrs:
            if type(value) != self.attrs[key]:
                raise TypeError("Неверный тип присваиваемых данных.")
            if key == ("practices " or "duration ")  and value <= 0:
                raise TypeError("Неверный тип присваиваемых данных.")
                
        object.__setattr__(self, key, value)
            
    def __getattr__(self, item):
        return False
        
    def __delattr__(self, item):
        if item == ("title" or "practices" or "duration"):
            raise AttrbuteError()
        
        
class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = []
        
    def add_lesson(self, lesson):
        self.lessons.append(lesson)
        
    def remove_lesson(self, indx):
        self.lessons.pop(indx)
        
        
        
class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []
        
    def add_module(self, module):
        self.modules.append(module)
        
    def remove_module(self, indx):
        self.modules.pop(indx)



"""
Подвиг 6. Вам необходимо написать программу описания музеев. Для этого нужно объявить класс Museum, объекты которого формируются командой:

mus = Museum(название музея)
В объектах этого класса должны формироваться следующие локальные атрибуты:

name - название музея (строка);
exhibits - список экспонатов (изначально пустой список).

Сам класс Museum должен иметь методы:

add_exhibit(self, obj) - добавление нового экспоната в музей (в конец списка exhibits);
remove_exhibit(self, obj) - удаление экспоната из музея (из списка exhibits по ссылке obj - на экспонат)
get_info_exhibit(self, indx) - получение информации об экспонате (строка) по индексу списка (нумерация с нуля).

Экспонаты представляются объектами своих классов. Для примера объявите в программе следующие классы экспонатов:

Picture - для картин;
Mummies - для мумий;
Papyri - для папирусов.

Объекты этих классов должны создаваться следующим образом (с соответствующим набором локальных атрибутов):

p = Picture(название, художник, описание)            # локальные атрибуты: name - название; author - художник; descr - описание
m = Mummies(имя мумии, место находки, описание)      # локальные атрибуты: name - имя мумии; location - место находки; descr - описание
pr = Papyri(название папируса, датировка, описание)  # локальные атрибуты: name - название папируса; date - датировка (строка); descr - описание
Метод get_info_exhibit() класса Museum должен возвращать значение атрибута descr указанного экспоната в формате:

"Описание экспоната {name}: {descr}"

Например:

"Описание экспоната Девятый вал: Айвазовский написал супер картину."
"""

class Museum:
    def __init__(self, name):
        self.name = name
        self.exhibits = []
        
    def add_exhibit(self, obj):
        self.exhibits.append(obj)
        
    def remove_exhibit(self, obj):
        self.exhibits.remove(obj)
        
    def get_info_exhibit(self, indx):
        return (f"Описание экспоната {self.exhibits[indx].name}: {self.exhibits[indx].descr}")
        

class Picture:
    def __init__(self, name, author, descr):
        self.name = name
        self.author = author
        self.descr = descr
        
class Mummies:
    def __init__(self, name, location, descr):
        self.name = name
        self.location = location
        self.descr = descr
        
class Papyri:
    def __init__(self, name, date, descr):
        self.name = name
        self.date = date
        self.descr = descr




"""
Подвиг 7 (на повторение). Объявите класс SmartPhone, объекты которого предполагается создавать командой:

sm = SmartPhone(марка смартфона)
Каждый объект должен содержать локальные атрибуты:

model - марка смартфона (строка);
apps - список из установленных приложений (изначально пустой).

Также в классе SmartPhone должны быть объявлены следующие методы:

add_app(self, app) - добавление нового приложения на смартфон (в конец списка apps);
remove_app(self, app) - удаление приложения по ссылке на объект app.

При добавлении нового приложения проверять, что оно отсутствует в списке apps (отсутствует объект соответствующего класса).

Каждое приложение должно определяться своим классом. Для примера объявите следующие классы:

AppVK - класс приложения ВКонтаке;
AppYouTube - класс приложения YouTube;
AppPhone - класс приложения телефона.

Объекты этих классов должны создаваться следующим образом (с соответствующим набором локальных атрибутов):
"""

class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []
        
    def add_app(self, app):
        if len(tuple(filter(lambda x: type(x) == type(app), self.apps))) == 0:
            self.apps.append(app)
            
    def remove_app(self, app):
        self.apps.remove(app)
        
class AppVK:
    def __init__(self):
        self.name = "ВКонтакте"
    
class AppYouTube:
    def __init__(self, memory_max):
        self.name = "YouTube"
        self.memory_max = memory_max
        
class AppPhone:
    def __init__(self, phones):
        self.name = "Phone"
        self.phone_list = phones



"""
Подвиг 8. Объявите класс Circle (окружность), объекты которого должны создаваться командой:

circle = Circle(x, y, radius)   # x, y - координаты центра окружности; radius - радиус окружности
В каждом объекте класса Circle должны формироваться локальные приватные атрибуты:

__x, __y - координаты центра окружности (вещественные или целые числа);
__radius - радиус окружности (вещественное или целое положительное число).

Для доступа к этим приватным атрибутам в классе Circle следует объявить объекты-свойства (property):

x, y - для изменения и доступа к значениям __x, __y, соответственно;
radius - для изменения и доступа к значению __radius.

При изменении значений приватных атрибутов через объекты-свойства нужно проверять, что присваиваемые значения - числа (целые или вещественные). Дополнительно у радиуса проверять, что число должно быть положительным (строго больше нуля). Сделать все эти проверки нужно через магические методы. При некорректных переданных числовых значениях, прежние значения меняться не должны (исключений никаких генерировать при этом не нужно).

Если присваиваемое значение не числовое, то генерировать исключение командой:

raise TypeError("Неверный тип присваиваемых данных.")
При обращении к несуществующему атрибуту объектов класса Circle выдавать булево значение False.

Пример использования класса (эти строчки в программе писать не нужно):
"""

class Circle:
    attrs = {"x":(int, float), "y":(int, float), "radius":(int, float)}
    def __init__(self, x, y, radius):
        self.__x = self.__y = self.__radius = None
        self.x = x
        self.y = y
        self.radius = radius

    def __setattr__(self, key, value):
        if key in self.attrs and type(value) not in self.attrs[key]:
            raise TypeError("Неверный тип присваиваемых данных.")
        if key == "radius" and value <=0:
            return
        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

    @property
    def x (self):
        return self.__x
    
    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y (self):
        return self.__y
    
    @y.setter
    def y (self, value):
        self.__y = value

    @property
    def radius (self):
        return self.__radius
    
    @radius.setter
    def radius (self, value):
        self.__radius = value


"""
Подвиг 9. Объявите в программе класс Dimensions (габариты) с атрибутами:

MIN_DIMENSION = 10
MAX_DIMENSION = 1000

Каждый объект класса Dimensions должен создаваться командой:

d3 = Dimensions(a, b, c)   # a, b, c - габаритные размеры
и содержать локальные атрибуты:

__a, __b, __c - габаритные размеры (целые или вещественные числа).

Для работы с этими локальными атрибутами в классе Dimensions следует прописать следующие объекты-свойства:

a, b, c - для изменения и считывания соответствующих локальных атрибутов __a, __b, __c.

При изменении значений __a, __b, __c следует проверять, что присваиваемое значение число в диапазоне [MIN_DIMENSION; MAX_DIMENSION]. Если это не так, то новое значение не присваивается (игнорируется).

С помощью магических методов данного занятия запретить создание локальных атрибутов MIN_DIMENSION и MAX_DIMENSION в объектах класса Dimensions. При попытке это сделать генерировать исключение:

raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
"""

class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000
    
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
        
    def __setattr__(self, key, value):
        if key == ("MIN_DIMENSION" and "MAX_DIMENSION"):
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
            
        if type(value) in (int, float) and self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
            object.__setattr__(self, key, value)
        
        
    @property
    def a (self):
        return self.__a
    
    @a.setter
    def a (self, value):
        self.__a = value
        
    @property
    def b (self):
        return self.__b
    
    @b.setter
    def b (self, value):
        self.__b = value
        
    @property
    def c (self):
        return self.__c
    
    @c.setter
    def c (self, value):
        self.__c = value



"""
Подвиг 10. Объявите класс GeyserClassic - фильтр для очистки воды. В этом классе должно быть три слота для фильтров. Каждый слот строго для своего класса фильтра:

Mechanical - для очистки от крупных механических частиц;
Aragon - для последующей очистки воды;
Calcium - для обработки воды на третьем этапе.



Объекты классов фильтров должны создаваться командами:

filter_1 = Mechanical(дата установки)
filter_2 = Aragon(дата установки)
filter_3 = Calcium(дата установки)
Во всех объектах этих классов должен формироваться локальный атрибут:

date - дата установки фильтров (для простоты - положительное вещественное число).

Также нужно запретить изменение этого атрибута после создания объектов этих классов (только чтение). В случае присвоения нового значения, прежнее значение не менять. Ошибок никаких не генерировать.

Объекты класса GeyserClassic должны создаваться командой:

g = GeyserClassic()
А сам класс иметь атрибут:

MAX_DATE_FILTER = 100 - максимальное время работы фильтра (любого)

и следующие методы:

add_filter(self, slot_num, filter) - добавление фильтра filter в указанный слот slot_num (номер слота: 1, 2 и 3), если он (слот) пустой (без фильтра). Также здесь следует проверять, что в первый слот можно установить только объекты класса Mechanical, во второй - объекты класса Aragon и в третий - объекты класса Calcium. Иначе слот должен оставаться пустым.

remove_filter(self, slot_num) - извлечение фильтра из указанного слота (slot_num: 1, 2, и 3);

get_filters(self) - возвращает кортеж из набора трех фильтров в порядке их установки (по возрастанию номеров слотов);

water_on(self) - включение воды: возвращает True, если вода течет и False - в противном случае.

Метод water_on() должен возвращать значение True при выполнении следующих условий:

- все три фильтра установлены в слотах;
- все фильтры работают в пределах срока службы (значение (time.time() - date) должно быть в пределах [0; MAX_DATE_FILTER])
"""
import time

class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.filter_class = ('Mechanical', 'Aragon', 'Calcium')
        self.filters = {(1, self.filter_class[0]): None, (2, self.filter_class[1]): None, (3, self.filter_class[2]): None}

    def add_filter(self, slot_num, filter):
        key = (slot_num, filter.__class__.__name__)
        if key in self.filters and not self.filters[key]:
            self.filters[key] = filter

    def remove_filter(self, slot_num):
        if type(slot_num) == int and 1 <= slot_num <= 3:
            key = (slot_num, self.filter_class[slot_num-1])
            if key in self.filters:
                self.filters[key] = None

    def get_filters(self):
        return tuple(self.filters.values())

    def water_on(self):
        end = time.time()
        for x in self.filters.values():
            if x is None:
                return False
            start = x.date
            if end - start > self.MAX_DATE_FILTER:
                return False
        return True

class Mechanical:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == "date" and key in self.__dict__:
            return
        object.__setattr__(self, key, value)
        
class Aragon:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == "date" and key in self.__dict__:
            return
        object.__setattr__(self, key, value)

class Calcium:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == "date" and key in self.__dict__:
            return
        object.__setattr__(self, key, value)


"""
Подвиг 2. Объявите класс RandomPassword для генерации случайных паролей. Объекты этого класса должны создаваться командой:

rnd = RandomPassword(psw_chars, min_length, max_length)
где psw_chars - строка из разрешенных в пароле символов; min_length, max_length - минимальная и максимальная длина генерируемых паролей.

Непосредственная генерация одного пароля должна выполняться командой:

psw = rnd()
где psw - ссылка на строку длиной в диапазоне [min_length; max_length] из случайно выбранных символов строки psw_chars.

С помощью генератора списка (list comprehension) создайте список lst_pass из трех сгенерированных паролей объектом rnd класса RandomPassword, созданного с параметрами: 

min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
P.S. Выводить на экран ничего не нужно, только создать список из паролей.

P.P.S. Дополнительное домашнее задание: попробуйте реализовать этот же функционал с использованием замыканий функций.
"""
from random import randint

class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length
        
    def __call__(self, *args, **kwargs):
        n = randint(self.min_length, self.max_length)
        len_chars = len(self.psw_chars)
        return ''.join(self.psw_chars[randint(0, len_chars-1)] for _ in range(n))
        
rnd = RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)
lst_pass = [rnd(), rnd(), rnd()]



"""
Подвиг 3. Для последовательной обработки файлов из некоторого списка, например:

filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.8.jpg", "forest.jpeg", "eq_1.png", "eq_2.png", "my.html", "data.shtml"]
Необходимо объявить класс ImageFileAcceptor, который бы выделял только файлы с указанными расширениями.

Для этого предполагается создавать объекты класса командой:

acceptor = ImageFileAcceptor(extensions)
где extensions - кортеж с допустимыми расширениями файлов, например: extensions = ('jpg', 'bmp', 'jpeg').

А, затем, использовать объект acceptor в стандартной функции filter языка Python следующим образом:

image_filenames = filter(acceptor, filenames)
Пример использования класса (эти строчки в программе писать не нужно):
"""
class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions
        
    def __call__(self, name, *args, **kwargs):
        start = name.rfind('.')
        ext = '' if start == -1 else name[start+1:]
        return ext in self.extensions
        
filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]


"""
Вам необходимо в программе объявить классы валидаторов:

LengthValidator - для проверки длины данных в диапазоне [min_length; max_length];
CharsValidator - для проверки допустимых символов в строке.

Объекты этих классов должны создаваться командами:

lv = LengthValidator(min_length, max_length) # min_length - минимально допустимая длина; max_length - максимально допустимая длина
cv = CharsValidator(chars) # chars - строка из допустимых символов
Для проверки корректности данных каждый валидатор должен вызываться как функция:

res = lv(string)
res = cv(string)
и возвращать True, если string удовлетворяет условиям валидатора и False - в противном случае.

P.S. В программе следует только объявить два класса валидаторов, на экран выводить ничего не нужно.
"""

class LengthValidator:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length
        
    def __call__(self, string, *args, **kwargs):
        return  self.min_length <= len(string) <= self.max_length
 
        
class CharsValidator:
    def __init__(self, chars):
        self.chars = chars
        
    def __call__(self, string, *args, **kwargs):
        return set(string) <= set(self.chars)


"""
одвиг 5. Объявите класс DigitRetrieve для преобразования данных из строки в числа. Объекты этого класса создаются командой:

dg = DigitRetrieve()
Затем, их предполагается использовать, например следующим образом:

d1 = dg("123")   # 123 (целое число)
d2 = dg("45.54")   # None (не целое число)
d3 = dg("-56")   # -56 (целое число)
d4 = dg("12fg")  # None (не целое число)
d5 = dg("abc")   # None (не целое число)
То есть, целые числа в строке следует приводить к целочисленному типу данных, а все остальные - к значению None.

С помощью объектов класса DigitRetrieve должно выполняться преобразование чисел из списка строк следующим образом:
"""
class DigitRetrieve:
    def __call__(self, string, *args, **kwargs):
        if string[0] == "-":
            if string[1:].isdigit():
                return int(string)
        elif string.isdigit():
                return int(string)
        else:
            return None

dg = DigitRetrieve()           
st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]



"""
Подвиг 6. Предположим, вам необходимо создать программу по преобразованию списка строк, например:

lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
в следующий фрагмент HTML-разметки (многострочной строки, кавычки выводить не нужно):

'''<ul>
<li>Пункт меню 1</li>
<li>Пункт меню 2</li>
<li>Пункт меню 3</li>
</ul>'''

Для этого необходимо объявить класс RenderList, объекты которого создаются командой:

render = RenderList(type_list)
где type_list - тип списка (принимает значения: "ul" - для списка с тегом <ul> и "ol" - для списка с тегом <ol>). Если значение параметра type_list другое (не "ul" и не "ol"), то формируется список с тегом <ul>.

Затем, предполагается использовать объект render следующим образом:

html = render(lst) # возвращается многострочная строка с соответствующей HTML-разметкой
Пример использования класса (эти строчки в программе писать не нужно):
"""
class RenderList:
    def __init__(self, type_list):
        self.type_list = type_list if type_list in ("ul", "ol") else "ul"
        
    def __call__(self, lst, *args, **kwargs):
        return "\n".join([f'<{self.type_list}>', *map(lambda x: f"<li>{x}</li>", lst), f"</{self.type_list}>"])
        
        
lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
print(html)


"""
Подвиг 7. Необходимо объявить класс-декоратор с именем HandlerGET, который будет имитировать обработку GET-запросов на стороне сервера. Для этого сам класс HandlerGET нужно оформить так, чтобы его можно было применять к любой функции как декоратор. Например:

@HandlerGET
def contact(request):
    return "Сергей Балакирев"
Здесь request - это произвольный словарь с данными текущего запроса, например, такой: {"method": "GET", "url": "contact.html"}. А функция должна возвращать строку.

Затем, при вызове декорированной функции:

res = contact({"method": "GET", "url": "contact.html"})
должна возвращаться строка в формате:

"GET: <данные из функции>"

В нашем примере - это будет:

"GET: Сергей Балакирев"

Если ключ method в словаре request отсутствует, то по умолчанию подразумевается GET-запрос. Если же ключ method принимает другое значение, например, "POST", то декорированная функция contact должна возвращать значение None.

Для реализации имитации GET-запроса в классе HandlerGET следует объявить вспомогательный метод со следующей сигнатурой:

def get(self, func, request, *args, **kwargs): ...
Здесь func - ссылка на декорируемую функцию; request - словарь с переданными данными при вызове декорированной функции. Именно в этом методе следует формировать возвращаемую строку в указанном формате:

"GET: Сергей Балакирев"

P.S. В программе достаточно объявить только класс. Ничего на экран выводить не нужно.
"""

class HandlerGET:
    def __init__(self, func):
        self.func = func
        
    def __call__(self, request, *args, **kwargs):
        m = request.get('method', 'GET')
        if m == 'GET':
            return self.get(self.func, request)
        return None
        
    def get(self, func, request, *args, **kwargs):
        return f'GET: {func(request)}'





"""
Подвиг 8 (развитие подвига 7). Необходимо объявить класс-декоратор с именем Handler, который можно было бы применять к функциям следующим образом:

@Handler(methods=('GET', 'POST')) # по умолчанию methods = ('GET',)
def contact(request):
    return "Сергей Балакирев"
Здесь аргумент methods декоратора Handler содержит список разрешенных запросов для обработки. Сама декорированная функция вызывается по аналогии с предыдущим подвигом:

res = contact({"method": "POST", "url": "contact.html"})
В результате функция contact должна возвращать строку в формате:

"<метод>: <данные из функции>"

В нашем примере - это будет:

"POST: Сергей Балакирев"

Если ключ method в словаре request отсутствует, то по умолчанию подразумевается GET-запрос. Если ключ method принимает значение отсутствующее в списке methods декоратора Handler, например, "PUT", то декорированная функция contact должна возвращать значение None.

Для имитации GET и POST-запросов в классе Handler необходимо объявить два вспомогательных метода с сигнатурами:

def get(self, func, request, *args, **kwargs) - для имитации обработки GET-запроса
def post(self, func, request, *args, **kwargs) - для имитации обработки POST-запроса

В зависимости от типа запроса должен вызываться соответствующий метод (его выбор в классе можно реализовать методом __getattribute__()). На выходе эти методы должны формировать строки в заданном формате.

P.S. В программе достаточно объявить только класс. Ничего на экран выводить не нужно.
"""
class Handler:
    def __init__(self, methods=('GET', )):
        self.__methods = methods
        
    def __call__(self, func, *args, **kwargs):
        def wrapper(request):
            m = request.get('method', 'GET')
            if m in self.__methods:
                method = m.lower()
                return self.__getattribute__(method)(func, request)
        return wrapper
    
    def get(self, func, request, *args, **kwargs):
        return f"GET: {func(request)}"
        
    def post(self, func, request, *args, **kwargs):
        return f"POST: {func(request)}"


"""
Подвиг 9. Объявите класс-декоратор InputDigits для декорирования стандартной функции input так, чтобы при вводе строки из целых чисел, записанных через пробел, например:

"12 -5 10 83"

на выходе возвращался список из целых чисел:

[12, -5, 10, 83]

Назовите декорированную функцию input_dg и вызовите ее командой:

res = input_dg()
"""
class InputDigits:
    def __init__(self, func):
        self.func = func
        
    def __call__(self, *args, **kwargs):
        return list(map(int, self.func().split()))
        

input_dg = InputDigits(input)
res = input_dg()


"""
Подвиг 10 (развитие подвига 9). Объявите класс-декоратор InputValues с параметром render - функция или объект для преобразования данных из строк в другой тип данных. Чтобы реализовать такой декоратор в инициализаторе __init__() следует указать параметр render, а магический метод __call__() определяется как функция-декоратор:

class InputValues:
    def __init__(self, render):     # render - ссылка на функцию или объект для преобразования
        # здесь строчки программы

    def __call__(self, func):     # func - ссылка на декорируемую функцию
        def wrapper(*args, **kwargs):
            # здесь строчки программы
        return wrapper
В качестве рендера объявите класс с именем RenderDigit, который бы преобразовывал строковые данные в целые числа. Объекты этого класса создаются командой:

render = RenderDigit()
и применяются следующим образом:

d1 = render("123")   # 123 (целое число)
d2 = render("45.54")   # None (не целое число)
d3 = render("-56")   # -56 (целое число)
d4 = render("12fg")  # None (не целое число)
d5 = render("abc")   # None (не целое число)
Декорируйте стандартную функцию input декоратором InputValues и объектом рендера класса RenderDigit так, чтобы на выходе при вводе целых чисел через пробел возвращался список из введенных значений. А на месте не целочисленных данных - значение None.

Например, при вводе строки:

"1 -5.3 0.34 abc 45f -5"

должен возвращаться список:

[1, None, None, None, None, -5]

Назовите декорированную функцию input_dg и вызовите ее командой:

res = input_dg()
Выведите результат res на экран.
"""
class InputValues:
    def __init__(self, render):     # render - ссылка на функцию или объект для преобразования
        self.__render = render

    def __call__(self, func):     # func - ссылка на декорируемую функцию
        def wrapper(*args, **kwargs):
            return list(map(self.__render, func(*args, **kwargs).split()))
        return wrapper
        
class RenderDigit:
    def __call__(self, string, *args, **kwargs):
        try:
            return int(string)
        except:
            return None

render = RenderDigit()
input_dg = InputValues(render)(input)           
res = input_dg()
print (res)



"""
Подвиг 2. Объявите класс с именем Book (книга), объекты которого создаются командой:

book = Book(title, author, pages)
где title - название книги (строка); author - автор книги (строка); pages - число страниц в книге (целое число).

Также при выводе информации об объекте на экран командой:

print(book)
должна отображаться строчка в формате:

"Книга: {title}; {author}; {pages}"

Например:

"Книга: Муму; Тургенев; 123"
"""
import sys

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self):
        return f"Книга: {self.title}; {self.author}; {self.pages}"

title, author, pages = input().strip(), input().strip(), int(input().strip()) 
book = Book(title, author, pages) 
print(book)



"""
Подвиг 3. Объявите класс с именем Model, объекты которого создаются командой:

model = Model()
Объявите в этом классе метод query() для формирования записи базы данных. Использоваться этот метод должен следующим образом:

model.query(field_1=value_1, field_2=value_2, ..., field_N=value_N)

Например:

model.query(id=1, fio='Sergey', old=33)
Все эти переданные данные должны сохраняться внутри объекта model класса Model. Затем, при выполнении команды:

print(model)
В консоль должна выводиться информация об объекте в формате:

"Model: field_1 = value_1, field_2 = value_2, ..., field_N = value_N"

Например:

"Model: id = 1, fio = Sergey, old = 33"

Если метод query() не вызывался, то в консоль выводится строка:

"Model"

P.S. В программе нужно только объявить класс, выводить в консоль ничего не нужно.
"""
class Model:
    def __init__(self):
        self.count = None
    
    
    def query(self, **kwargs):
        self.count = kwargs
        
    def __str__(self):
        if self.count is None:
            return 'Model'
        else:
            return 'Model: ' + ', '.join([f'{key} = {value}' for key, value in self.count.items()])
        
model = Model()
model.query(id=1, fio='Sergey', old=33)
print(model)



"""
Подвиг 4. Объявите класс WordString, объекты которого создаются командами:

w1 = WordString()
w2 = WordString(string)
где string - передаваемая строка. Например:

words = WordString("Курс по Python ООП")
Реализовать следующий функционал для объектов этого класса:

len(words) - должно возвращаться число слов в переданной строке (слова разделяются одним или несколькими пробелами);
words(indx) - должно возвращаться слово по его индексу (indx - порядковый номер слова в строке, начиная с 0).

Также в классе WordString реализовать объект-свойство (property):

string - для передачи и считывания строки.
"""
class WordString:
    def __init__(self, arg=''):
        self.__word = arg
        
    def __len__(self):
        return len(self.string.split())
        
    def __call__(self, indx):
        x = self.__word.split()
        return x[indx]
        
    @property
    def string(self):
        return self.__word
        
    @string.setter
    def string(self, s):
        self.__word = s
        
        
words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")



"""
Подвиг 5. Объявите класс LinkedList (связный список) для работы со следующей структурой данных:



Здесь создается список из связанных между собой объектов класса ObjList. Объекты этого класса создаются командой:

obj = ObjList(data)
где data - строка с некоторой информацией. Также в каждом объекте obj класса ObjList должны создаваться следующие локальные атрибуты:

__data - ссылка на строку с данными;
__prev - ссылка на предыдущий объект связного списка (если объекта нет, то __prev = None);
__next - ссылка на следующий объект связного списка (если объекта нет, то __next = None).

В свою очередь, объекты класса LinkedList должны создаваться командой:

linked_lst = LinkedList()
и содержать локальные атрибуты:

head - ссылка на первый объект связного списка (если список пуст, то head = None);
tail - ссылка на последний объект связного списка (если список пуст, то tail = None).

А сам класс содержать следующие методы:

add_obj(obj) - добавление нового объекта obj класса ObjList в конец связного списка;
remove_obj(indx) - удаление объекта класса ObjList из связного списка по его порядковому номеру (индексу); индекс отсчитывается с нуля.

Также с объектами класса LinkedList должны поддерживаться следующие операции:

len(linked_lst) - возвращает число объектов в связном списке;
linked_lst(indx) - возвращает строку __data, хранящуюся в объекте класса ObjList, расположенного под индексом indx (в связном списке).
"""

class ObjList:
    def __init__(self, data):
        self.__data = ''
        self.data = data
        self.__next = self.__prev = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) == str:
            self.__data = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if type(obj) in (ObjList, type(None)):
            self.__next = obj

    @property
    def prev(self):
        return self.__prev

    @next.setter
    def prev(self, obj):
        if type(obj) in (ObjList, type(None)):
            self.__prev = obj


class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def add_obj(self, obj):
        obj.prev = self.tail

        if self.tail:
            self.tail.next = obj
        self.tail = obj

        if not self.head:
            self.head = obj

    def __get_obj_by_index(self, indx):
        h = self.head
        n = 0
        while h and n < indx:
            h = h.next
            n += 1
        return h  


    def remove_obj(self, indx):
        obj = self.__get_obj_by_index(indx)
        if obj is None:
            return
        
        p, n = obj.prev, obj.next
        if p:
            p.next = n
        if n:
            n.prev = p

        if self.head == obj:
            self.head = n
        if self.tail == obj:
            self.tail = p

    def __len__(self):
        n = 0
        h = self.head
        while h:
            n += 1
            h = h.next
        return n

    def __call__(self, indx, *args, **kwargs):
        obj = self.__get_obj_by_index(indx)
        return obj.data if obj else None


"""
Подвиг 6. Объявите класс с именем Complex для представления и работы с комплексными числами. Объекты этого класса должны создаваться командой:

cm = Complex(real, img)
где real - действительная часть комплексного числа (целое или вещественное значение); img - мнимая часть комплексного числа (целое или вещественное значение).

Объявите в этом классе следующие объекты-свойства (property):

real - для записи и считывания действительного значения;
img - для записи и считывания мнимого значения.

При записи новых значений необходимо проверять тип передаваемых данных. Если тип не соответствует целому или вещественному числу, то генерировать исключение командой:

raise ValueError("Неверный тип данных.")
Также с объектами класса Complex должна поддерживаться функция:

res = abs(cm)
возвращающая модуль комплексного числа (вычисляется по формуле: sqrt(real*real + img*img) - корень квадратный от суммы квадратов действительной и мнимой частей комплексного числа).

Создайте объект cmp класса Complex для комплексного числа с real = 7 и img = 8. Затем, через объекты-свойства real и img измените эти значения на real = 3 и img = 4. Вычислите модуль полученного комплексного числа (сохраните результат в переменной c_abs).

P.S. На экран ничего выводить не нужно.
"""

class Complex:
    def __init__(self, real, img):
        self.__real = self.__img = 0
        self.__real = real
        self.__img = img

    def __abs__(self):
        return (self.__real**2 + self.__img**2)**0.5

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, value):
        if type(value) not in (int, float):
            raise ValueError("Неверный тип данных.")
        else:
            self.__real = value

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        if type(value) not in (int, float):
            raise ValueError("Неверный тип данных.")
        else:
            self.__img = value

cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_ads = abs(cmp)

"""
Подвиг 7. Объявите класс с именем RadiusVector для описания и работы с n-мерным вектором (у которого n координат). Объекты этого класса должны создаваться командами:

# создание 5-мерного радиус-вектора с нулевыми значениями координат (аргумент - целое число больше 1)
vector = RadiusVector(5)  # координаты: 0, 0, 0, 0, 0

# создание 4-мерного радиус-вектора с координатами: 1, -5, 3.4, 10 (координаты - любые целые или вещественные числа)
vector = RadiusVector(1, -5, 3.4, 10)
То есть, при передаче одного значения, оно интерпретируется, как размерность нулевого радиус-вектора. Если же передается более одного числового аргумента, то они интерпретируются, как координаты радиус-вектора.

Класс RadiusVector должен содержать методы:

set_coords(coord_1, coord_2, ..., coord_N) - для изменения координат радиус-вектора;
get_coords() - для получения текущих координат радиус-вектора (в виде кортежа).

Также с объектами класса RadiusVector должны поддерживаться следующие функции:

len(vector) - возвращает число координат радиус-вектора (его размерность);
abs(vector) - возвращает длину радиус-вектора (вычисляется как: sqrt(coord_1*coord_1 + coord_2*coord_2 + ... + coord_N*coord_N) - корень квадратный из суммы квадратов координат).
"""
class RadiusVector:
    def __init__(self, arg1, *args):
        if len(args) == 0:
            self.__coords = [0] * arg1
        else:
            self.__coords = [arg1] + list(args)

    def set_coords(self, *args):
        n = min(len(args), len(self.__coords))
        self.__coords[:n] = args[:n]

    def get_coords(self):
        return tuple(self.__coords)

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return sum(map(lambda x: x**2, self.__coords))**0.5



