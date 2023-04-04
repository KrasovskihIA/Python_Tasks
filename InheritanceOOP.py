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

"""
Объявите в программе следующие классы без содержимого (используйте оператор pass):

Protists, Plants, Animals, Mosses, Flowering, Worms, Mammals, Human, Monkeys

и постройте схему наследования в соответствии со следующей иерархией древа жизни:



Затем, объявите в программе классы:

Monkey - наследуется от Monkeys и служит для описания обезьян;
Person - наследуется от Human и служит для описания человека;
Flower - наследуется от Flowering и служит для описания цветка;
Worm - наследуется от Worms и служит для описания червей.

Объекты этих классов должны создаваться командами:

obj = Monkey(name, weight, old)
obj = Person(name, weight, old)
obj = Flower(name, weight, old)
obj = Worm(name, weight, old)
где name - наименование (или имя) объекта (строка); weight - вес (вещественное число); old - возраст (целое число). В каждом объекте любого из этих классов должны создаваться соответствующие атрибуты: name, weight, old.

Создайте в программе следующие объекты и сохраните их в виде списка lst_objs:

Monkey: "мартышка", 30.4, 7
Monkey: "шимпанзе", 24.6, 8
Person: "Балакирев", 88, 34
Person: "Верховный жрец", 67.5, 45
Flower: "Тюльпан", 0.2, 1
Flower: "Роза", 0.1, 2
Worm: "червь", 0.01, 1
Worm: "червь 2", 0.02, 1

Затем, используя функции isinstance() и генератор списков (List comprehensions), сформируйте следующие списки из указанных объектов:

lst_animals - все объекты, относящиеся к животным (Animals);
lst_plants - все объекты, относящиеся к растениям (Plants);
lst_mammals - все объекты, относящиеся к млекопитающим (Mammals).
"""
class Protists: 
    def __init__(self, name, weight, old):
        self.name = name
        self.weight = weight
        self.old = old

class Plants(Protists):
    pass

class Animals(Protists):
    pass

class Mosses(Plants): 
    pass

class Flowering(Plants): 
    pass

class Flower(Flowering):
    pass

class Worms(Animals): 
    pass

class Worm(Worms):
    pass

class Mammals(Animals): 
    pass

class Human(Mammals): 
    pass

class Person(Human):
    pass

class Monkeys(Mammals): 
    pass

class Monkey(Monkeys):
    pass


lst_objs = [Monkey("мартышка", 30.4, 7), Monkey("шимпанзе", 24.6, 8),
            Person("Балакирев", 88, 34), Person("Верховный жрец", 67.5, 45),
            Flower("Тюльпан", 0.2, 1), Flower("Роза", 0.1, 2),
            Worm("червь", 0.01, 1), Worm("червь 2", 0.02, 1)]

lst_animals = []
lst_plants = []
lst_mammals  = []

for obj in lst_objs:
    if isinstance(obj, Animals):
        lst_animals.append(obj)
    elif isinstance(obj, Plants):
        lst_plants.append(obj)
        
for obj2 in lst_animals:
    if isinstance(obj2, Mammals):
        lst_mammals.append(obj2)
        
print(lst_animals) 
print(lst_plants)
print(lst_mammals)

        
"""
Подвиг 6. Известно, что с объектами класса tuple можно складывать только такие же объекты (кортежи). Например:

t1 = (1, 2, 3)
t2 = t1 + (4, 5) # (1, 2, 3, 4, 5)
Если же мы попытаемся прибавить любой другой итерируемый объект, например, список:

t2 = t1 + [4, 5]
то возникнет ошибка. Предлагается поправить этот функционал и создать свой собственный класс Tuple, унаследованный от базового класса tuple и поддерживающий оператор:

t1 = Tuple(iter_obj)
t2 = t1 + iter_obj  # создается новый объект класса Tuple с новым (соединенным) набором данных
где iter_obj - любой итерируемый объект (список, словарь, строка, множество, кортеж и т.п.)
"""
class Tuple(tuple):
    def __init__(self, iter_obj):
        self.iter_obj = iter_obj
        
    def __add__(self, other):
        return Tuple(tuple(self.iter_obj) + tuple(other))
        
    def __iadd_(self, other):
        return self.__add__(other)

t = Tuple([1, 2, 3])
t = t + "Python"
print(t)   # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
t = (t + "Python") + "ООП"

"""
Необходимо в программе объявить класс VideoItem для представления одного видео (например, в youtube). Объекты этого класса должны создаваться командой:

video = VideoItem(title, descr, path)
где title - заголовок видео (строка); descr - описание видео (строка); path - путь к видеофайлу. В каждом объекте класса VideoItem должны создаваться соответствующие атрибуты: title, descr, path.

Затем, нужно создать класс для формирования оценки видео в баллах от 0 до 5. Для этого нужно объявить еще один класс с именем VideoRating, объекты которого создаются командой:

rating = VideoRating()
В каждом объекте класса VideoRating должен быть локальный приватный атрибут с именем __rating, содержащий целое число от 0 до 5 (по умолчанию 0). А для записи и считывания значения из этого приватного атрибута должно быть объект-свойство (property) с именем rating.

Так как атрибут __rating - это целое число в диапазоне [0; 5], то в момент присвоения ему какого-либо значения необходимо проверять, что присваиваемое значение - целое число в диапазоне [0; 5]. Если это не так, то генерировать исключение командой:

raise ValueError('неверное присваиваемое значение')
Далее, в каждом объекте класса VideoItem должен быть локальный атрибут rating - объект класса VideoRating.
"""
class VideoItem:
    def __init__(self, title, descr, path):
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()


class VideoRating:
    def __init__(self):
        self.__rating = 0

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, rating):
        if not rating in range(0, 6):
            raise ValueError('неверное присваиваемое значение')
        self.__rating = rating

"""
Объявите в программе базовый класс с именем IteratorAttrs для перебора всех локальных атрибутов объектов класса. Напомню, что для этого используются два магических метода:

__iter__() - для получения объекта-итератора (в данном случае - это сам объект self)
__next__() - для перебора локальных атрибутов объекта self (используйте для этого словарь __dict__)

Метод __next__() на каждой итерации должен возвращать кортеж в формате: (имя атрибута, значение).

Подсказка: здесь можно определить один метод __iter__() как функцию-генератор.

Объявите дочерний класс SmartPhone, объекты которого создаются командой:

phone = SmartPhone(model, size, memory)
где model - модель смартфона (строка); size - габариты (ширина, длина) в виде кортежа двух чисел; memory - размер ОЗУ (памяти), как целое число. В каждом объекте класса SmartPhone должны создаваться соответствующие локальные атрибуты: model, size, memory.

Благодаря наследованию от базового класса IteratorAttrs, с объектами класса SmartPhone должен выполняться оператор for:

for attr, value in phone:
    print(attr, value)
"""
class IteratorAttrs:
    def __iter__(self):
        for x in self.__dict__.items():
            yield x


class SmartPhone(IteratorAttrs):
    def __init__(self, model, size, memory):
        self.model = model
        self.size = size
        self.memory = memory

"""
Подвиг 3. Ранее вы уже использовали делегирование методов, когда вызывали инициализатор базового класса через функцию super(). Чаще всего делегирование в Python связано с вызовом магических методов базовых классов (так как их имена нельзя менять). Выполним такой пример.

Объявите в программе базовый класс с именем Book, объекты которого создаются командой:

book = Book(title, author, pages, year)
где title - заголовок книги (строка); author - автор книги (строка); pages - число страниц (целое число); year - год издания (целое число). В каждом объекте класса Book должны формироваться соответствующие локальные атрибуты: title, author, pages, year.

Объявите дочерний класс DigitBook от класса Book, объекты которого создаются командой:

db = DigitBook(title, author, pages, year, size, frm)
где дополнительные параметры size - размер книги в байтах (целое число); frm - формат книги (строка: 'pdf', 'doc', 'fb2', 'txt'). В каждом объекте класса DigitBook должны формироваться соответствующие локальные атрибуты: title, author, pages, year, size, frm.

Инициализация локальных атрибутов title, author, pages, year должна выполняться в базовом классе Book, а параметры size, frm инициализируются в дочернем классе DigitBook.

P.S. В программе нужно объявить только классы. На экран выводить ничего не нужно.
"""
class Book:
    def __init__(self, title, author, pages, year):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

class DigitBook(Book):
    def __init__(self, title, author, pages, year, size, frm):
        super().__init__(title, author, pages, year)
        self.size = size
        self.frm = frm

"""
Подвиг 4. Создается программа по учету склада. Каждый предмет на складе должен описываться базовым классом Thing. Объекты этого класса создаются командой:

th1 = Thing(name, weight)
где name - наименование предмета (строка); weight - вес предмета (вещественное число).

Для описания каждого конкретного вида предметов, создаются дочерние классы (на основе базового Thing):

ArtObject - для представления арт-объектов;
Computer - для системных блоков компьютеров;
Auto - для автомобилей.

Объекты этих классов создаются командами:

obj = ArtObject(name, weight, author, date)  # author - автор (строка); date - дата создания (строка)
obj = Computer(name, weight, memory, cpu)    # memory - размер памяти (целое число); cpu - тип процессора (строка)
obj = Auto(name, weight, dims)               # dims - габариты, кортеж (width, length, height) - вещественные или целые числа
На основе класса Auto создаются дочерние классы Mercedes и Toyota, объекты которых определяются командами:

auto = Mercedes(name, weight, dims, model, old) # model - модель (строка); old - время использования, в годах (целое число)
auto = Toyota(name, weight, dims, model, wheel) # model - модель (строка); wheel - тип руля: True - леворульный, False - праворульный
Во всех объектах классов должны создаваться соответствующие локальные атрибуты: name, weight и т.д.

Инициализация атрибутов должна выполняться в соответствующих классах (не должно быть дублирования кода).

P.S. В программе нужно объявить только классы. На экран выводить ничего не нужно.
"""
class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class ArtObject(Thing):
    def __init__(self, name, weight, author, date):
        super().__init__(name, weight)
        self.author = author
        self.date = date

class Computer(Thing):
    def __init__(self, name, weight, memory, cpu):
        super().__init__(name, weight)
        self.memory = memory
        self.cpu = cpu

class Auto(Thing):
    def __init__(self, name, weight, dims):
        super().__init__(name, weight)
        self.dims = dims
        

class Mercedes(Auto):
    def __init__(self, name, weight, dims, model, old):
        super().__init__(name, weight, dims)
        self.model = model
        self.old = old

class Toyota(Auto):
    def __init__(self, name, weight, dims, model, wheel):
        super().__init__(name, weight, dims)
        self.model = model
        self.wheel = wheel

"""
Подвиг 5. Вам поручено организовать представление объектов для продажи в риэлтерских агентствах. Для этого в программе нужно объявить базовый класс SellItem, объекты которого создаются командой:

item = SellItem(name, price)
где name - название объекта продажи (строка); price - цена продажи (число: целое или вещественное).

Каждые конкретные типы объектов описываются следующими классами, унаследованные от базового SellItem:

House - дома;
Flat - квартиры;
Land - земельные участки.



Объекты этих классов создаются командами:

house = House(name, price, material, square)
flat = Flat(name, price, size, rooms)
land = Land(name, price, square)
В каждом объекте этих классов должны формироваться соответствующие локальные атрибуты: name, price и т.д.

Формирование атрибутов name и price должно выполняться в инициализаторе базового класса.

Далее, объявить еще один класс с именем Agency, объекты которого создаются командой:

ag = Agency(name)
где name - название агентства (строка). В классе Agency объявить следующие методы:

add_object(obj) - добавление нового объекта недвижимости для продажи (один из объектов классов: House, Flat, Land);
remove_object(obj) - удаление объекта obj из списка объектов для продажи;
get_objects() - возвращает список из всех объектов для продажи.
"""
class SellItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class House(SellItem):
    def __init__(self, name, price, material, square):
        super().__init__(name, price)
        self.material = material
        self.square = square

class Flat(SellItem):
    def __init__(self, name, price, size, rooms):
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms

class Land(SellItem):
    def __init__(self, name, price, square):
        super().__init__(name, price)
        self.square = square

class Agency:
    def __init__(self, name):
        self.name = name
        self.list_obj = []

    def add_object(self, obj):
        self.list_obj.append(obj)

    def remove_object(self, obj):
        self.list_obj.remove(obj)

    def get_objects(self):
        return self.list_obj

"""
 Ваша команда создает небольшой фреймворк для веб-сервера. Для этого был объявлен класс:
 И его предполагается использовать следующим образом:

@Callback('/', Router)
def index():
    return '<h1>Главная</h1>'


route = Router.get('/')
if route:
    ret = route()
    print(ret)
Здесь Callback - это класс-декоратор с параметрами: path = '/' - маршрут; router_cls = Router - класс роутера. Декоратор Callback должен обеспечивать добавление функции (в примере index) в словарь app класса Router. Ключом словаря выступает маршрут (path), а значением - ссылка на декорируемую функцию. Для этого следует использовать метод add_callback класса Router.

Затем, из роутера (Router) методом get выбирается ранее добавленная функция (в примере index), и если она существует, то вызывается с выводом результата в консоль.

Ваша задача реализовать класс-декоратор Callback. 
"""
class Router:
    app = {}

    @classmethod
    def get(cls, path):
        return cls.app.get(path)

    @classmethod
    def add_callback(cls, path, func):
        cls.app[path] = func

class Callback:
    def __init__(self, path, router_cls ):
        self.__path = path
        self.__router_cls = router_cls 

    def __call__(self, func):
        self.__router_cls.add_callback(self.__path, func)

"""
Подвиг 7. В программе объявлена функция integer_params для класса Vector, которая применяет к каждому методу класса декоратор integer_params_decorated:
Декоратор integer_params_decorated должен проверять, чтобы все передаваемые аргументы в методы класса (кроме первого self) были целыми числами (имели тип int). Если это не так, то должно генерироваться исключение командой:

raise TypeError("аргументы должны быть целыми числами")
Ваша задача объявить эту функцию-декоратор.
"""
def integer_params_decorated(func):
    def wrapper(self, *args, **kwargs):
        if not all(type(x) == int for x in args):
            raise TypeError("аргументы должны быть целыми числами")
        if not all(type(x) == int for x in kwargs.values()):
            raise TypeError("аргументы должны быть целыми числами")
        return func(self, *args, **kwargs)
    return wrapper

def integer_params(cls):
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))

    return cls


@integer_params
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

    def set_coords(self, *coords, reverse=False):
        c = list(coords)
        self.__coords = c if not reverse else c[::-1]

"""
Подвиг 8 (на повторение). Объявите класс SoftList, который наследуется от стандартного класса list. В классе SoftList следует объявить необходимые магические методы так, чтобы при обращении к несуществующему элементу (по индексу) возвращалось значение False (а не исключение Out of Range). Например:
"""
class SoftList(list):
    def __getitem__(self, item):
        try:
            return super().__getitem__(item)
        except IndexError:
            return False

"""
Объявите класс StringDigit, который наследуется от стандартного класса str. Объекты класса StringDigit должны создаваться командой:

sd = StringDigit(string)
где string - строка из цифр (например, "12455752345950"). Если в строке string окажется хотя бы один не цифровой символ, то генерировать исключение командой:

raise ValueError("в строке должны быть только цифры")
Также в классе StringDigit нужно переопределить оператор + (конкатенации строк) так, чтобы операции:

sd = sd + "123"
sd = "123" + sd
создавали новые объекты класса StringDigit (а не класса str). Если же при соединении строк появляется не цифровой символ, то генерировать исключение:

raise ValueError("в строке должны быть только цифры")
"""
class StringDigit(str):
    def __init__(self, string):
        self.string = string 

    def __setattr__(self, key, value):
        if not value.isdigit():
            raise ValueError("в строке должны быть только цифры")
        super().__setattr__(key, value)

    def __add__(self, value):
        if not value.isdigit():
            raise ValueError("в строке должны быть только цифры")
        return StringDigit(self.string + value)

    def __radd__(self, value):
        if not value.isdigit():
            raise ValueError("в строке должны быть только цифры")
        return StringDigit(value + self.string )


"""
Объявите базовый класс с именем ItemAttrs, который бы позволял обращаться к локальным атрибутам объектов дочерних классов по индексу. Для этого в классе ItemAttrs нужно переопределить следующие методы:

__getitem__() - для получения значения атрибута по индексу;
__setitem__() - для изменения значения атрибута по индексу.

Объявите дочерний класс Point для представления координаты точки на плоскости. Объекты этого класса должны создаваться командой:

pt = Point(x, y)
где x, y - целые или вещественные числа.
"""
class ItemAttrs:
    def __init__(self, *args):
        self.coords = list(args)

    def __getitem__(self, item):
        return self.coords[item]

    def __setitem__(self, key, value):
        self.coords[key] = value

class Point(ItemAttrs):
    pass

pt = Point(1, 2.5)
x = pt[0]   # 1
y = pt[1]   # 2.5
pt[0] = 10

"""
 Объявите класс Animal (животное), объекты которого создаются командой:

an = Animal(name, kind, old)
где name - название животного (строка); kind - вид животного (строка); old - возраст (целое число). В каждом объекте этого класса должны создаваться соответствующие приватные атрибуты: __name, __kind, __old.

В классе Animal должны быть объявлены объекты-свойства для изменения и считывания приватных атрибутов:

name - для работы с приватным атрибутом __name;
kind - для работы с приватным атрибутом __kind;
old - для работы с приватным атрибутом __old.

Создайте в программе список с именем animals, который содержит три объекта класса Animal со следующими данными:

Васька; дворовый кот; 5
Рекс; немецкая овчарка; 8
Кеша; попугай; 3

P.S. В программе нужно объявить только класс и создать список animals. На экран выводить ничего не нужно.
"""
class DesAnimal:  
    def __set_name__(self, owner, name):
        self.name = "__" + name
 
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
 
    def __set__(self, instance, value):
        setattr(instance, self.name, value)

class Animal:
    name = DesAnimal()
    kind = DesAnimal()
    old = DesAnimal()

    def __init__(self, name, kind, old):
        self.name = name
        self.kind = kind
        self.old = old

animals = [Animal('Васька', 'дворовый кот', 5), Animal('Рекс', 'немецкая овчарка', 8), Animal('Кеша', 'попугай', 3) ]