"""
Наследование часто используют, чтобы вынести общий код дочерних классов в базовый класс. Сделаем такой пример. Объявите в программе базовый класс Animal (животное), объекты которого можно создать командой:

an = Animal(name, old)
где name - название животного (строка); old - возраст животного (целое число). Такие же локальные атрибуты (name и old) должны создаваться в объектах класса.

Далее, объявите дочерний класс (от базового Animal) с именем Cat (кошки), объекты которого создаются командой:

cat = Cat(name, old, color, weight)
где name, old - те же самые параметры, что и в базовом классе; color - цвет кошки (строка); weight - вес кошки (любое положительное число).

В объектах класса Cat должны автоматически формироваться локальные атрибуты: name, old, color, weight. Формирование атрибутов name, old должен выполнять инициализатор базового класса. 

По аналогии объявите еще один дочерний класс Dog (собака), объекты которого создаются командой:

dog = Dog(name, old, breed, size)
здесь name, old - те же самые параметры, что и в базовом классе; breed - порода собаки (строка); size - кортеж в формате (height, length) высота и длина - числа.

В объектах класса Dog по аналогии должны формироваться локальные атрибуты: name, old, breed, size. За формирование атрибутов name, old отвечает инициализатор базового класса. 

Наконец, в классах Cat и Dog объявите метод:

get_info() - для получения информации о животном.

Этот метод должен возвращать строку в формате:

"name: old, <остальные параметры через запятую>"
"""
class Animal:
    def __init__(self, name, old):
        self.name = name
        self.old = old
    
class Cat(Animal):
    def __init__(self, name, old, color, weight):
        super().__init__(name, old)
        self.color = color 
        self.weight = weight

    def get_info(self):
        return f'{self.name}: {self.old}, {self.color}, {self.weight}'

class Dog(Animal):
    def __init__(self, name, old, breed, size):
        super().__init__(name, old)
        self.breed = breed
        self.size = size

    def get_info(self):
        return f'{self.name}: {self.old}, {self.breed}, {self.size}'

"""
Предположим, вы разрабатываете программу для интернет-магазина. В этом магазине могут быть как реальные (физические) товары, так и электронные. Для этих двух групп, очевидно, нужен разный набор атрибутов:
- для реальных физических товаров: id, name, price, weight, dims
где id - идентификатор товара (целое число); name - наименование товара (строка); price - цена товара (вещественное число); weight - вес товара (вещественное число); dims = (lenght, width, depth) - длина, ширина, глубина - габариты товара (вещественные числа);
- для электронных товаров: id, name, price, memory, frm
где id - идентификатор товара (целое число); name - наименование товара (строка); price - цена товара (вещественное число); memory - занимаемый размер (в байтах - целое число); frm - формат данных (строка: pdf, docx и т.п.)
Так как все товары могут идти вперемешку, то мы хотим, чтобы в каждом объекте (для товара) присутствовали все атрибуты:
id, name, price, weight, dims, memory, frm
с начальными значениями None. А уже, затем, нужным из них будут присвоены конкретные данные.
Для реализации этой логики объявите в программе базовый класс с именем Thing (вещь, предмет), объекты которого могут создаваться командой:
th = Thing(name, price)
А атрибут id должен формироваться автоматически и быть уникальным для каждого товара (например, можно для каждого нового объекта увеличивать на единицу).
В объектах класса Thing должен формироваться полный набор локальных атрибутов (id, name, price, weight, dims, memory, frm) со значением None, кроме атрибутов: id, name, price.
Далее, нужно объявить два дочерних класса:

Table - для столов;
ElBook - для электронных книг.

Объекты этих классов должны создаваться командами:

table = Table(name, price, weight, dims)
book = ElBook(name, price, memory, frm)
Причем, атрибуты name, price (а также id) следует инициализировать в базовом классе, т.к. они общие для всех товаров. Остальные атрибуты должны либо принимать значение None, если не используются, либо инициализироваться конкретными значениями уже в дочерних классах.

Наконец, в базовом классе Thing объявите метод:

get_data() - для получения кортежа в формате (id, name, price, weight, dims, memory, frm)
"""
class Thing:
    __id = 0

    def __init__(self, name, price):
        Thing.__id+=1
        self.id = Thing.__id
        self.name = name
        self.price = price
        self.weight = self.dims = self.memory = self.frm = None

    def get_data(self):
        return self.__dict__

class Table(Thing):
    def __init__(self, name, price, weight, dims):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims

class ElBook(Thing):
    def __init__(self, name, price, memory, frm):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm


table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
print(*table.get_data())
print(*book.get_data())

"""
Подвиг 6. Еще один пример, когда в базовом классе прописывается необходимый начальный функционал для дочерних классов.
Известно, что браузер (и не только) может отправлять на сервер различные типы запросов: GET, POST, PUT, DELETE и др. Каждый из этих типов запросов обрабатывается в программе на сервере своим отдельным методом. Чтобы каждый раз не прописывать все необходимые методы в классах при обработке входящих запросов, они выносятся в базовый класс и вызываются из дочерних.
"""

class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass

class DetailView(GenericView):
    def __init__(self, methods=('GET', )):
        super().__init__(methods)

    def get(self, request):
        if type(request) != dict:
            raise TypeError('request не является словарем')
        if  'url' not in request:
            raise TypeError('request не содержит обязательного ключа url')

        return f"url: {request['url']}"

    def render_request(self, request, method):
        if method.upper() not in self.methods:
            raise TypeError('данный запрос не может быть выполнен')

        f = getattr(self, method.lower(), False)
        if f :
            return f(request)

"""
С помощью наследования можно как бы "наполнять" дочерние классы нужными качествами (свойствами). Как пример, объявите в программе класс с именем:
Singleton
который бы позволял создавать только один экземпляр (все последующие экземпляры должны ссылаться на первый). Как это делать, вы должны уже знать из этого курса.
Затем, объявите еще один класс с именем:
Game
который бы наследовался от класса Singleton. Объекты класса Game должны создаваться командой:
game = Game(name)
где name - название игры (строка). В каждом объекте класса Game должен создаваться атрибут name с соответствующим содержимым.
Убедитесь, что атрибут name принимает значение первого созданного объекта (если это не так, то поправьте инициализатор дочернего класса, чтобы это условие выполнялось).
P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
"""
class Singleton:
    __instance = None
    __instance_base = None

    def __new__(cls, *args, **kwargs):
        if cls == Singleton:
            if cls.__instance_base is None:
                cls.__instance_base =  object().__new__(cls)
            return cls.__instance_base

        if cls.__instance is None:
            cls.__instance = object().__new__(cls)
        return cls.__instance

class Game(Singleton):
    def __init__(self, name):
        if 'name' not in self.__dict__:
            self.name = name

"""
Вам необходимо создать множество классов для валидации (проверки) корректности данных. Для этого ваш непосредственный начальник (Senior) предлагает вам объявить в программе базовый класс с именем:
Validator
Проверка корректности выполняется с помощью метода _is_valid(). После этого, в программе нужно объявить два дочерних класса:

IntegerValidator - для проверки, что data - целое число в заданном диапазоне;
FloatValidator - для проверки, что data - вещественное число в заданном диапазоне.
"""
class Validator:
    def __call__(self, data):
        if not self._is_valid(data):
            raise ValueError('данные не прошли валидацию')
        return self._is_valid(data)
      
    def _is_valid(self, data):
        pass

class IntegerValidator(Validator):  # для проверки, что data - целое число в заданном диапазоне
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
            
    def _is_valid(self, data):        
        return isinstance(data, int) and self.min_value <= data <= self.max_value
    
class FloatValidator(Validator):  # для проверки, что data - вещественное число в заданном диапазоне
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
            
    def _is_valid(self, data):    
        return isinstance(data, float) and self.min_value <= data <= self.max_value
    

"""
спользуя механизм наследования, вам поручено разработать функционал по построению моделей нейронных сетей. Общая схема модели очень простая
Базовый класс Layer имеет локальный атрибут next_layer, который ссылается на следующий объект слоя нейронной сети (объект класса Layer или любого объекта дочерних классов). У последнего слоя значение next_layer = None.

Создавать последовательность слоев предполагается командами:

first_layer = Layer()
next_layer = first_layer(Layer())
next_layer = next_layer(Layer())

о есть, сначала создается объект first_layer класса Layer, а затем он вызывается как функция для образования связки со следующим слоем. При этом возвращается ссылка на следующий слой и переменная next_layer ссылается уже на этот следующий слой нейронной сети. И так можно создавать столько слоев, сколько необходимо.
В каждом объекте класса Layer также должен формироваться локальный атрибут:

name = 'Layer'

Но сам по себе класс Layer образует только связи между слоями. Никакой другой функциональности он не несет. Чтобы это исправить, в программе нужно объявить еще два дочерних класса:

Input - формирование входного слоя нейронной сети;
Dense - формирование полносвязного слоя нейронной сети.
"""
class Layer:
    def __init__(self, name = 'Layer'):
        self.name = name
        self.next_layer = None
    
    def __call__(self, layer):
        self.next_layer = layer
        return layer

class Input(Layer):
    def __init__(self, inputs):
        super().__init__('Input')
        self.inputs = inputs

class Dense(Layer):
    def __init__(self, inputs, outputs, activation):
        super().__init__('Dense')
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation

class NetworkIterator:
    def __init__(self, network):
        self.network = network

    def __iter__(self):
        layer = self.network
        while layer:
            yield layer
            layer = layer.next_layer

"""
Объявите в программе класс Vector, объекты которого создаются командой:

v = Vector(x1, x2, ..., xN)
где x1, x2, ..., xN - координаты радиус-вектора (числа: целые или вещественные).

С объектами этого класса должны выполняться команды:

v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)
v = v1 + v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
v = v1 - v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
Если размерности векторов v1 и v2 не совпадают, то генерировать исключение:

raise TypeError('размерности векторов не совпадают')
В самом классе Vector объявите метод с именем get_coords, который возвращает кортеж из текущих координат вектора.

На основе класса Vector объявите дочерний класс VectorInt для работы с целочисленными координатами:

v = VectorInt(1, 2, 3, 4)
v = VectorInt(1, 0.2, 3, 4) # ошибка: генерируется исключение raise ValueError('координаты должны быть целыми числами')
При операциях сложения и вычитания с объектом класса VectorInt:

v = v1 + v2  # v1 - объект класса VectorInt
v = v1 - v2  # v1 - объект класса VectorInt
должен формироваться объект v как объект класса Vector, если хотя бы одна координата является вещественной. Иначе, v должен быть объектом класса VectorInt.

P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
"""
class Vector:
    def __init__(self, *args):
        self.coords = args

    def __make_vector(self, coords):
        try:
            return self.__class__(*coords)
        except ValueError:
            return Vector(*coords)

    def __add__(self, other):
        if len(self.coords) != len(other.coords):
            raise TypeError('размерности векторов не совпадают')
        coords = tuple(map(sum, zip(self.coords, other.coords)))
        return self.__make_vector(coords)

    def __sub__(self, other):
        if len(self.coords) != len(other.coords):
            raise TypeError('размерности векторов не совпадают')
        coords = tuple(x - y for (x, y) in zip(self.coords, other.coords))
        return self.__make_vector(coords)

    def get_coords(self):
        return self.coords


class VectorInt(Vector):
    def __init__(self, *args):
        super().__init__(*args)
        if not all(type(i) is int for i in args):
            raise ValueError('координаты должны быть целыми числами')


"""
Подвиг 3. Создается проект, в котором предполагается использовать списки из целых чисел. Для этого вам ставится задача создать класс с именем ListInteger с базовым классом list и переопределить три метода:

__init__()
__setitem__()
append()

так, чтобы список ListInteger содержал только целые числа. При попытке присвоить любой другой тип данных, генерировать исключение командой:

raise TypeError('можно передавать только целочисленные значения')
"""
class ListInteger(list):
    def __init__(self, li):
        for x in li:
            self.__check_num(x)
        super().__init__(li)

    def __setitem__(self, key, value):
        self.__check_num(value)
        super().__setitem__(key, value)

    def append(self, value):
        self.__check_num(value)
        super().append(value)


    @staticmethod
    def __check_num(num):
        if type(num) != int:
            raise TypeError('можно передавать только целочисленные значения')

"""
Подвиг 4. Разрабатывается интернет-магазин. Каждый товар предполагается представлять классом Thing, объекты которого создаются командой:
thing = Thing(name, price, weight)
где name - наименование товара (строка); price - цена (вещественное число); weight - вес товара (вещественное число). В каждом объекте этого класса создаются аналогичные атрибуты: name, price, weight.

Класс Thing необходимо определить так, чтобы его объекты можно было использовать в качестве ключей словаря, например:
d = {}
d[thing] = thing

И для каждого уникального набора данных name, price, weight должны формироваться свои уникальные ключи.
Затем, вам необходимо объявить класс словаря DictShop, унаследованный от базового класса dict. В этом новом словаре ключами могут выступать только объекты класса Thing. При попытке указать любой другой тип, генерировать исключение командой:
raise TypeError('ключами могут быть только объекты класса Thing')
Объекты класса DictShop должны создаваться командами:

dict_things = DictShop() # пустой словарь
dict_things = DictShop(things) # словарь с набором словаря things
где things - некоторый словарь. В инициализаторе следует проверять, чтобы аргумент thing был словарем, если не так, то выбрасывать исключение:

raise TypeError('аргумент должен быть словарем')
И проверять, чтобы все ключи являлись объектами класса Thing. Если это не так, то генерировать исключение:

raise TypeError('ключами могут быть только объекты класса Thing')
Дополнительно в классе DictShop переопределить метод:

__setitem__()

с проверкой, что создаваемый ключ является объектом класса Thing. Иначе, генерировать исключение:

raise TypeError('ключами могут быть только объекты класса Thing')
Пример использования классов (эти строчки в программе не писать):
"""
class Thing:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self):
        return hash((self.name, self.price, self.weight))

class DictShop(dict):
    def __init__(self, things=None):
        things = {} if things is None else things

        if not isinstance(things, dict):
            raise TypeError('аргумент должен быть словарем')
        if things and not all(isinstance(key, Thing) for key in things):
            raise TypeError('ключами могут быть только объекты класса Thing')
        super().__init__(things)

    def __setitem__(self, key, value):
        if not isinstance(key, Thing):
            raise TypeError('ключами могут быть только объекты класса Thing')
        super().__setitem__(key, value)