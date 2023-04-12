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

"""
Подвиг 6. Объявите класс Furniture (мебель), объекты которого создаются командой:

f = Furniture(name, weight)
где name - название предмета (строка); weight - вес предмета (целое или вещественное число).

В каждом объекте класса Furniture должны создаваться защищенные локальные атрибуты с именами _name и _weight. В самом классе Furniture нужно объявить приватные методы:

__verify_name() - для проверки корректности имени;
__verify_weight() - для проверки корректности веса.

Метод __verify_name() проверяет, что имя должно быть строкой, если это не так, то генерируется исключение командой:

raise TypeError('название должно быть строкой')
Метод __verify_weight() проверяет, что вес должен быть положительным числом (строго больше нуля), если это не так, то генерируется исключение командой:

raise TypeError('вес должен быть положительным числом')
Данные методы следует вызывать всякий раз при записи новых значений в атрибуты _name и _weight (а также при их создании).

На основе базового класса Furniture объявить следующие дочерние классы:

Closet - для представления шкафов;
Chair - для представления стульев;
Table - для представления столов.

Объекты этих классов должны создаваться командами:

obj = Closet(name, weight, tp, doors)   # tp: True - шкаф-купе; False - обычный шкаф; doors - число дверей (целое число)
obj = Chair(name, weight, height)       # height - высота стула (любое положительное число)
obj = Table(name, weight, height, square) # height - высота стола; square - площадь поверхности (любые положительные числа)
В каждом объекте этих классов должны создаваться соответствующие защищенные атрибуты:

- в объектах класса Closet: _name, _weight, _tp, _doors
- в объектах класса Chair: _name, _weight, _height
- в объектах класса Table: _name, _weight, _height, _square

В каждом классе (Closet, Chair, Table) объявить метод:

get_attrs()
который возвращает кортеж из значений локальных защищенных атрибутов объектов этих классов.
"""
class Furniture:
    def __init__(self, name, weight):
        self._name = name
        self._weight = weight

    def __verify_name(self, string):
        if  type(string) != str:
            raise TypeError('название должно быть строкой')

    def __verify_weight(self, value):
        if value < 0:
            raise TypeError('вес должен быть положительным числом')

    def __setattr__(self, key, value):
        if key == '_name':
            self.__verify_name(value)
            object.__setattr__(self, key, value)
        else :
            self.__verify_weight(value)
            object.__setattr__(self, key, value)

    def get_attrs(self):
        return self.__dict__.values()

class Closet(Furniture):
    def __init__(self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors

class Chair(Furniture):
    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self._height = height

class Table(Furniture):
    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        self._height = height
        self._square = square

"""
Подвиг 7 (введение в паттерн слушатель). Своей работой вы немного впечатлили начальство и оно поручило вам доделать паттерн слушатель (listener). Идея этого паттерна очень проста и основа реализуется следующим образом:
десь в объектах класса Subject можно зарегистрировать (добавить) множество объектов класса Observer (наблюдатель, слушатель). Это делается с помощью метода add_observer(). Затем, когда данные (self.__data) меняются путем вызова метода change_data() класса Subject, то у всех слушателей автоматически вызывается метод update(). В этом методе можно прописать самую разную логику работы при изменении данных в каждом конкретном слушателе.

В проекте данный паттерн предполагается использовать для отображения информации о погоде в различных форматах:

- текущая температура;
- текущее атмосферное давление;
- текущая влажность воздуха.
А вам поручается разработать дочерние классы, унаследованные от класса Observer, с именами:

TemperatureView - слушатель для отображения информации о температуре;
PressureView - слушатель для отображения информации о давлении;
WetView - слушатель для отображения информации о влажности.

Каждый из этих классов должен переопределять метод update() базового класса так, чтобы выводилась в консоль информация в формате:

TemperatureView: "Текущая температура <число>"
PressureView: "Текущее давление <число>"
WetView: "Текущая влажность <число>"

Важно: для вывода информации в консоль используйте функцию print() с одним аргументом в виде F-строки.
"""
class Observer:
    def update(self, data):
        pass

    def __hash__(self):
        return hash(id(self))


class Subject:
    def __init__(self):
        self.__observers = {}
        self.__data = None

    def add_observer(self, observer):
        self.__observers[observer] = observer

    def remove_observer(self, observer):
        if observer in self.__observers:
            self.__observers.pop(observer)

    def __notify_observer(self):
        for ob in self.__observers:
            ob.update(self.__data)

    def change_data(self, data):
        self.__data = data
        self.__notify_observer()


class Data:
    def __init__(self, temp, press, wet):
        self.temp = temp    # температура
        self.press = press  # давление
        self.wet = wet      # влажность

class TemperatureView(Observer):
    def update(self, data):
        if data:
            print (f"Текущая температура {data.temp}")

class PressureView(Observer):
    def update(self, data):
        if data:
            print (f"Текущее давление {data.press}")

class WetView(Observer):
    def update(self, data):
        if data:
            print (f"Текущая влажность {data.wet}")


"""
Подвиг 8. Объявите базовый класс Aircraft (самолет), объекты которого создаются командой:

air = Aircraft(model, mass, speed, top)
где model - модель самолета (строка); mass - подъемная масса самолета (любое положительное число); speed - максимальная скорость (любое положительное число); top - максимальная высота полета (любое положительное число).

В каждом объекте класса Aircraft должны создаваться локальные атрибуты с именами: _model, _mass, _speed, _top и соответствующими значениями. Если передаваемые аргументы не соответствуют указанным критериям (строка, любое положительное число), то генерируется исключение командой:

raise TypeError('неверный тип аргумента')
Далее, в программе объявите следующие дочерние классы:

PassengerAircraft - пассажирский самолет;
WarPlane - военный самолет.

Объекты этих классов создаются командами:

pa = PassengerAircraft(model, mass, speed, top, chairs)  # chairs - число пассажирских мест (целое положительное число)
wp = WarPlane(model, mass, speed, top, weapons) # weapons - вооружение (словарь); ключи - название оружия, значение - количество
В каждом объекте классов PassengerAircraft и WarPlane должны формироваться локальные атрибуты с именами _chairs и _weapons соответственно. Инициализация остальных атрибутов должна выполняться через инициализатор базового класса.

В инициализаторах классов PassengerAircraft и WarPlane проверять корректность передаваемых аргументов chairs и weapons. Если тип данных не совпадает, то генерировать исключение командой:

raise TypeError('неверный тип аргумента')
"""
class Aircraft:
    def __init__(self, model, mass, speed, top):
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top

    def __setattr__(self, key, value):
        if key == '_model' and (type(value) != str or value.isdigit() == True):
            raise TypeError('неверный тип аргумента')
        if key == ('_mass' or '_speed' or '_top') and value < 0:
            raise TypeError('неверный тип аргумента')
        object.__setattr__(self, key, value)

class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self._chairs = chairs

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key == '_chairs' and (value < 0 or type(value) != int):
            raise TypeError('неверный тип аргумента')

class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self._weapons = weapons

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key == '_weapons' and  type(value) != dict:
            raise TypeError('неверный тип аргумента')

planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]

"""
Необходимо объявить функцию-декоратор class_log для класса, которая бы создавала логирование вызовов методов класса. Например следующие строчки программы
екорируют класс Vector и в список vector_log добавляются имена методов, которые были вызваны при использовании этого класса. В частности, после выполнения команд:

v = Vector(1, 2, 3)
v[0] = 10
в списке vector_log должны быть два метода:

['__init__', '__setitem__']

Ваша задача реализовать декоратор с именем class_log.
"""
def class_log(log_lst):
    def log_methods(cls):
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(cls, k, log_methods_decorator(v))
        return cls

    def log_methods_decorator(func):
        def wrapper(*args, **kwargs):
            log_lst.append(func.__name__)
            return func(*args, **kwargs)
        return wrapper

    return log_methods


vector_log = []   # наименование (vector_log) в программе не менять!


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value


"""
Вам необходимо объявить класс с именем FileDialogFactory (фабрика классов), который бы при выполнении команды:

dlg = FileDialogFactory(title, path, exts)
возвращал объект класса WindowsFileDialog, если CURRENT_OS равна строке 'windows', в противном случае - объект класса LinuxFileDialog. Объект самого класса FileDialogFactory создаваться не должен.

Для реализации такой логики, объявите внутри класса FileDialogFactory два статических метода:

def create_windows_filedialog(title, path, exts) - для создания объектов класса WindowsFileDialog;
def create_linux_filedialog(title, path, exts) - для создания объектов класса LinuxFileDialog.

Эти методы следует вызывать в магическом методе __new__() класса FileDialogFactory. Подумайте, как это правильно сделать, чтобы не создавался объект самого класса, а лишь возвращался объект или класса WindowsFileDialog, или класса LinuxFileDialog.
"""
CURRENT_OS = 'windows'   # 'windows', 'linux'


class WindowsFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class LinuxFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class FileDialogFactory:
    def __new__(cls, *args, **kwargs):
        if CURRENT_OS == 'windows':
            return cls.create_windows_filedialog(*args)
        else:
            return cls.create_linux_filedialog(*args)

    def create_windows_filedialog(title, path, exts):
        return WindowsFileDialog(title, path, exts)

    def create_linux_filedialog(title, path, exts):
        return LinuxFileDialog(title, path, exts)

"""
Первый класс описывает студентов, а второй - менторов. Вам поручается на основе базового класса Mentor разработать еще два дочерних класса:

Lector - для описания лекторов;
Reviewer - для описания экспертов.

Объекты этих классов должны создаваться командами:

lector = Lector(fio, subject)
reviewer = Reviewer(fio, subject)
где fio - ФИО (строка); subject - предмет (строка). Инициализации этих параметров (fio, subject) должна выполняться базовым классом Mentor.

В самих классах Lector и Reviewer необходимо объявить метод:

def set_mark(self, student, mark): ...
для простановки оценки (mark) студенту (student). Причем, в классе Lector оценки добавляются в список _lect_marks объекта класса Student, а в классе Reviewer - в список _house_marks. Используйте для этого методы add_lect_marks() и add_house_marks() класса Student.

Также в классах Lector и Reviewer должен быть переопределен магический метод:

__str__()
для формирования следующей информации об объектах:

- для объектов класса Lector: Лектор <ФИО>: предмет <предмет>
- для объектов класса Reviewer: Эксперт <ФИО>: предмет <предмет>
"""
class Student:
    def __init__(self, fio, group):
        self._fio = fio
        self._group = group
        self._lect_marks = []  # оценки за лекции
        self._house_marks = []  # оценки за домашние задания

    def add_lect_marks(self, mark):
        self._lect_marks.append(mark)

    def add_house_marks(self, mark):
        self._house_marks.append(mark)

    def __str__(self):
        return f"Студент {self._fio}: оценки на лекциях: {str(self._lect_marks)}; оценки за д/з: {str(self._house_marks)}"


class Mentor:
    def __init__(self, fio, subject):
        self._fio = fio
        self._subject = subject


class Lector(Mentor):
    def set_mark(self, student, mark):
            student.add_lect_marks(mark)

    def __str__(self):
        return f"Лектор {self._fio}: предмет {self._subject}"

class Reviewer(Mentor):
        def set_mark(self, student, mark):
            student.add_house_marks(mark)

        def __str__(self):
            return f"Эксперт {self._fio}: предмет {self._subject}"

"""
Подвиг 4. Вам необходимо объявить базовый класс ShopInterface с абстрактным методом:

def get_id(self): ...
В самом методе должно генерироваться исключение командой:

raise NotImplementedError('в классе не переопределен метод get_id')
Инициализатор в классе ShopInterface прописывать не нужно.

Далее объявите дочерний класс ShopItem (от базового класса ShopInterface), объекты которого создаются командой:

item = ShopItem(name, weight, price)
где name - название товара (строка); weight - вес товара (любое положительное число); price - цена товара (любое положительное число).

В каждом объекте класса ShopItem должны формироваться локальные атрибуты с именами _name, _weight, _price и соответствующими значениями. Также в объектах класса ShopItem должен автоматически формироваться локальный приватный атрибут __id с уникальным (для каждого товара) целым значением.

В классе ShopItem необходимо переопределить метод get_id() базового класса так, чтобы он (метод) возвращал значение атрибута __id.

P.S. В программе требуется объявить только классы. На экран выводить ничего не нужно.
"""
class ShopInterface:
    id_shop = 0

    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')

class ShopItem(ShopInterface):
    def __new__(cls, *args):
        cls.id_shop +=1
        return super().__new__(ShopItem)

    def __init__(self, name, weight, price):
        self._name = name
        self._weight = weight
        self._price = price
        self.__id = self.id_shop

    def get_id(self):
        return self.__id

"""

"""
class Validator:
    def __call__(self, data):
        if not self._is_valid(data):
            raise ValueError('данные не прошли валидацию')
        return self._is_valid(data)
      
    def _is_valid(self, data):
        raise NotImplementedError('в классе не переопределен метод _is_valid')

   
class FloatValidator(Validator):  # для проверки, что data - вещественное число в заданном диапазоне
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        return self._is_valid(value)
            
    def _is_valid(self, data):    
        return isinstance(data, float) and self.min_value <= data <= self.max_value


"""
Jбъявите базовый класс Model (модель), в котором нужно объявить один абстрактный метод с сигнатурой:

def get_pk(self): ...

и один обычный метод:

def get_info(self): ...

который бы возвращал строку "Базовый класс Model".

На основе класса Model объявите дочерний класс ModelForm, объекты которого создаются командой:

form = ModelForm(login, password)
где login - заголовок перед полем ввода логина (строка); password - заголовок перед полем ввода пароля (строка). В каждом объекте класса ModelForm должны формироваться локальные атрибуты с именами _login и _password, а также автоматически появляться локальный атрибут _id с уникальным целочисленным значением для каждого объекта класса ModelForm.
В классе ModelForm переопределите метод:

def get_pk(self): ...

который должен возвращать значение атрибута _id.
"""
from abc import ABC, abstractmethod

class Model(ABC):
    id_model = 0

    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self):
        pass

class ModelForm(Model):
    def __new__(cls, *args):
        cls.id_model +=1
        return super().__new__(ModelForm)

    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._id = self.id_model

    def get_pk(self):
        return self._id

"""
Используя информацию о модуле abc из предыдущего подвига 6, объявите базовый класс с именем StackInterface со следующими абстрактными методами:

def push_back(self, obj) - добавление объекта в конец стека;
def pop_back(self) - удаление последнего объекта из стека.
На основе этого класса объявите дочерний класс с именем Stack. Объекты этого класса должны создаваться командой:

st = Stack()
и в каждом объекте этого класса должен формироваться локальный атрибут:

_top - ссылка на первый объект стека (для пустого стека _top = None).

В самом классе Stack переопределить абстрактные методы базового класса:

def push_back(self, obj) - добавление объекта в конец стека;
def pop_back(self) - удаление последнего объекта из стека.

Сами объекты стека должны определяться классом StackObj и создаваться командой:

obj = StackObj(data)
где data - информация, хранящаяся в объекте (строка). В каждом объекте класса StackObj должны автоматически формироваться атрибуты:

_data - информация, хранящаяся в объекте (строка);
_next - ссылка на следующий объект стека (если следующий отсутствует, то _next = None).
"""
from abc import ABC, abstractmethod

class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        pass

    @abstractmethod
    def pop_back(self):
        pass

class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = value

class Stack(StackInterface):
    def __init__(self):
        self._top = self._tail = None

    def __get_pre(self):
        pre = self._top
        while pre.next.next:
            pre = pre.next
        return pre

    def push_back(self, obj):
        if self._tail:
            self._tail.next = obj
            self._tail = obj
        else:
            self._top = self._tail = obj

    def pop_back(self):
        if self._top == self._tail:
            res = self._tail
            self._top = self._tail = None
            return res

        pre = self.__get_pre()
        last = self._tail
        self._tail = pre
        pre.next = None
        return last

"""
 С помощью модуля abc можно определять не только абстрактные методы, но и абстрактные объекты-свойства (property). Делается это следующим образом:
 Используя эту информацию и информацию о модуле abc из подвига 6, объявите базовый класс с именем CountryInterface со следующими абстрактными методами и свойствами:

name - абстрактное свойство (property), название страны (строка);
population - абстрактное свойство (property), численность населения (целое положительное число);
square - абстрактное свойство (property), площадь страны (положительное число);

get_info() - абстрактный метод для получения сводной информации о стране.
В самом классе Country должны быть переопределены следующие свойства и методы базового класса:

name - свойство (property) для считывания названия страны (строка);
population - свойство (property) для записи и считывания численности населения (целое положительное число);
square - свойство (property) для записи и считывания площади страны (положительное число);

get_info() - метод для получения сводной информации о стране в виде строки:

"<название>: <площадь>, <численность населения>"
"""
from abc import ABC, abstractmethod

class CountryInterface (ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def population (self):
        pass

    @property
    @abstractmethod
    def square (self):
        pass

    @abstractmethod
    def get_info(self):
        pass

class Country(CountryInterface):
    def __init__(self, name, population, square):
        self._name = name
        self._population = population
        self._square = square

    @property
    def name(self):
        return self._name

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, value):
        self._population = value

    @property
    def square (self):
        return self._square 

    @square.setter
    def square (self, value):
        self._square  = value
    

    def get_info(self):
        return f"{self._name}: {self._square}, {self._population}"

"""
Вам поручают разработать класс для представления маршрутов в навигаторе. Для этого требуется объявить класс с именем Track, объекты которого могут создаваться командами:

tr = Track(start_x, start_y)
tr = Track(pt1, pt2, ..., ptN)
где start_x, start_y - начальная координата маршрута (произвольные числа); pt1, pt2, ..., ptN - набор из произвольного числа точек (координат) маршрута (объекты класса PointTrack).

При передаче аргументов (start_x, start_y) координата должна представляться первым объектом класса PointTrack. Наборы всех точек (объектов PointTrack) должны сохраняться в локальном приватном атрибуте объекта класса Track:

__points - список из точек (координат) маршрута.

Далее, каждая точка (координата) должна определяться классом PointTrack, объекты которого создаются командой:

pt = PointTrack(x, y)
где x, y - числа (целые или вещественные). Если передается другой тип данных, то должно генерироваться исключение командой:

raise TypeError('координаты должны быть числами')
В классе PointTrack переопределите магический метод __str__, чтобы информация об объекте класса возвращалась в виде строки:

"PointTrack: <x>, <y>"
В самом классе Track должно быть свойство (property) с именем:

points - для получения кортежа из точек маршрута.

Также в классе Track должны быть методы:

def add_back(self, pt) - добавление новой точки в конец маршрута (pt - объект класса PointTrack);
def add_front(self, pt) - добавление новой точки в начало маршрута (pt - объект класса PointTrack);
def pop_back(self) - удаление последней точки из маршрута;
def pop_front(self) - удаление первой точки из маршрута.
"""
class Track:
    def __init__(self, *args):
        self.__points = list(args)
    
    def __setattr__(self, name, val):
        if isinstance(val[0], PointTrack):            
            super().__setattr__(name, val)
        else:            
            super().__setattr__(name, [PointTrack(val[0], val[1])])
            
    @property
    def points(self):
        return tuple(self.__points)
    
    def add_back(self, pt):
        self.__points.append(pt)

    def add_front(self, pt):
        self.__points.insert(0, pt)

    def pop_back(self):
        self.__points.pop()

    def pop_front(self):
        self.__points.pop(0)
        
    
    
class PointTrack:
    def __init__(self, x, y):
        self.valid(x, y)
        self.x = x
        self.y = y
    
    @staticmethod
    def valid(x, y):
        if type(x) not in (int, float) or type(y) not in (int, float):
            raise TypeError('координаты должны быть числами')
        
    def __str__(self):
        return f'PointTrack: {self.x}, {self.y}'


"""
Объявите класс с именем Food (еда), объекты которого создаются командой:

food = Food(name, weight, calories)
где name - название продукта (строка); weight - вес продукта (любое положительное число); calories - калорийная ценность продукта (целое положительное число).

Объявите следующие дочерние классы с именами:

BreadFood - хлеб;
SoupFood - суп;
FishFood - рыба.

Объекты этих классов должны создаваться командами:

bf = BreadFood(name, weight, calories, white) # white - True для белого хлеба, False - для остальных
sf = SoupFood(name, weight, calories, dietary) # dietary - True для диетического супа, False - для других видов
ff = FishFood(name, weight, calories, fish) # fish - вид рыбы (семга, окунь, сардина и т.д.)
В каждом объекте этих дочерних классов должны формироваться соответствующие локальные атрибуты с именами:

BreadFood: _name, _weight, _calories, _white
SoupFood: _name, _weight, _calories, _dietary
FishFood: _name, _weight, _calories, _fish
"""
class FoodValue: 
    def __set_name__(self, owner, name):
        self.name = "_" + name
 
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
 
    def __set__(self, instance, value):
        setattr(instance, self.name, value)

class Food:
    name = FoodValue()
    weight = FoodValue()
    calories = FoodValue()

    def __init__(self, name, weight, calories):
        self.name = name
        self.weight = weight
        self.calories = calories

class BreadFood(Food):
    white = FoodValue()

    def __init__(self, name, weight, calories, white):
        super().__init__(name, weight, calories)
        self.white = white

class SoupFood(Food):
    dietary = FoodValue()

    def __init__(self, name, weight, calories, dietary):
        super().__init__(name, weight, calories)
        self.dietary = dietary

class FishFood(Food):
    fish = FoodValue()

    def __init__(self, name, weight, calories, fish):
        super().__init__(name, weight, calories)
        self.fish = fish

"""
Определите в программе классы в соответствии с их иерархией, представленной на рисунке выше:

Digit, Integer, Float, Positive, Negative

Каждый объект этих классов должен создаваться однотипной командой вида:

obj = Имя_класса(value)
где value - числовое значение. В каждом классе следует делать свою проверку на корректность значения value:

- в классе Digit: value - любое число;
- в классе Integer: value - целое число;
- в классе Float: value - вещественное число;
- в классе Positive: value - положительное число;
- в классе Negative: value - отрицательное число.

Если проверка не проходит, то генерируется исключение командой:

raise TypeError('значение не соответствует типу объекта')
После этого объявите следующие дочерние классы:

PrimeNumber - простые числа; наследуется от классов Integer и Positive;
FloatPositive - наследуется от классов Float и Positive.

Создайте три объекта класса PrimeNumber и пять объектов класса FloatPositive с произвольными допустимыми для них значениями. Сохраните все эти объекты в виде списка digits.

Затем, используя функции isinstance() и filter(), сформируйте следующие списки из указанных объектов:

lst_positive - все объекты, относящиеся к классу Positive;
lst_float - все объекты, относящиеся к классу Float.
"""
class Digit:                                                         
    def __init__(self, value):                                       
        self._value = value                                          
                                                                     
    def __setattr__(self, name, value):                              
        if not self._check_value(value):                             
            raise TypeError('значение не соответствует типу объекта')
        super().__setattr__(name, value)                             
                                                                     
    def _check_value(self, value):                                   
        return type(value) in (int, float)                           
                                                                     
                                                                     
class Integer(Digit):                                                
    def _check_value(self, value):                                   
        return super()._check_value(value) and type(value) is int                                    
                                                                                                                                        
class Float(Digit):                                                  
    def _check_value(self, value):                                   
        return super()._check_value(value) and type(value) is float  
   
class Positive(Digit):                                               
    def _check_value(self, value):                                   
        return super()._check_value(value) and value > 0             
    
class Negative(Digit):                                               
    def _check_value(self, value):                                    
        return super()._check_value(value) and value < 0             
                                                                        
class PrimeNumber(Integer, Positive):                                
    pass                                                             
                                                                                                                                         
class FloatPositive(Float, Positive):                                
    pass                                                             
                                                                     
                                                                     
digits = [PrimeNumber(1), PrimeNumber(2), PrimeNumber(3),            
          FloatPositive(1.2), FloatPositive(1.3), FloatPositive(1.4),
          FloatPositive(1.5), FloatPositive(1.6)]                    

lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits)) 


"""
ShopGenericView - для отображения всех локальных атрибутов объектов любых дочерних классов (не только Book);
ShopUserView - для отображения всех локальных атрибутов, кроме атрибута _id, объектов любых дочерних классов (не только Book).

То есть, в этих классах нужно переопределить два магических метода: __str__() и __repr__().
"""
class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id



class ShopGenericView:
    Exclude = tuple()
    def __str__(self):
        return '\n'.join('{0}: {1}'.format(attr, v) for attr, v in self.__dict__.items() if attr not in self.Exclude)

    def __repr__(self):
        return self.__str__()

class ShopUserView(ShopGenericView):
    Exclude = ('_id', )

class Book(ShopItem):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year


"""
Часто множественное наследование используют для наполнения дочернего класса определенным функционалом. То есть, с указанием каждого нового базового класса, дочерний класс приобретает все больше и больше возможностей. И, наоборот, убирая часть базовых классов, дочерний класс теряет соответствующую часть функционала. 
Например, паттерн миксинов активно используют в популярном фреймворке Django.  В частности, когда нужно указать дочернему классу, какие запросы от клиента он должен обрабатывать (запросы типа GET, POST, PUT, DELETE и т.п.). В качестве примера реализуем эту идею в очень упрощенном виде, но сохраняя суть паттерна миксинов.
"""
class RetriveMixin:
    def get(self, request):
        return "GET: " + request.get('url')


class CreateMixin:
    def post(self, request):
        return "POST: " + request.get('url')


class UpdateMixin:
    def put(self, request):
        return "PUT: " + request.get('url')


class GeneralView:
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')

    def render_request(self, request):
        method = request.get('method').upper()
        if method not in self.allowed_methods:
            raise TypeError(f"Метод {request.get('method')} не разрешен.")

        method_request = self.__getattribute__(method.lower())
        if method_request:
            return method_request(request)


class DetailView(RetriveMixin, UpdateMixin, GeneralView):
    allowed_methods = ('GET', 'POST', )

"""
Вам необходимо добавить в класс MoneyOperators аналогичную реализацию оператора вычитания.
"""
class Money:
    def __init__(self, value):
        self._money = value

    def __setattr__(self, key, value):
        if type(value) != (int or float):
            raise TypeError('сумма должна быть числом')
        object.__setattr__(self, key, value)

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        self._money = value

class MoneyOperators:
    def __add__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money + other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money + other.money)

    def __sub__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money - other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money - other.money)

class MoneyR(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyR: {self.money}"


class MoneyD(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyD: {self.money}"


"""
Подвиг 4. Объявите класс Person, в объектах которого разрешены только локальные атрибуты с именами (ограничение задается через коллекцию __slots__):

_fio - ФИО сотрудника (строка);
_old - возраст сотрудника (целое положительное число);
_job - занимаемая должность (строка).

"""
class Person:
    __slots__ = ('_fio', '_old', '_job')

    def __init__(self, fio, old, job):
        self._fio = fio
        self._old = old
        self._job = job

persons = [Person('Суворов', 52, 'полководец'),
           Person('Рахманинов', 50, 'пианист, композитор'),
           Person('Балакирев', 34, 'программист и преподаватель'),
           Person('Пушкин', 32, 'поэт и писатель')
           ]

"""
Объявите класс Planet (планета), объекты которого создаются командой:

p = Planet(name, diametr, period_solar, period)
где name - наименование планеты; diametr - диаметр планеты (любое положительное число); period_solar - период (время) обращения планеты вокруг Солнца (любое положительное число); period - период обращения планеты вокруг своей оси (любое положительное число).

В каждом объекте класса Planet должны формироваться локальные атрибуты с именами: _name, _diametr, _period_solar, _period и соответствующими значениями.
Затем, объявите класс с именем SolarSystem (солнечная система). В объектах этого класса должны быть допустимы, следующие локальные атрибуты (ограничение задается через коллекцию __slots__):
бъект класса SolarSystem должен создаваться командой:

s_system = SolarSystem()
и быть только один (одновременно в программе два и более объектов класса SolarSystem недопустимо). Используйте для этого паттерн Singleton.

В момент создания объекта SolarSystem должны автоматически создаваться перечисленные локальные атрибуты и ссылаться на соответствующие объекты класса Planet
"""
class Planet:
    def __init__(self, name, diametr, period_solar, period):
        self._name = name
        self._diametr = diametr
        self._period_solar = period_solar
        self._period = period

class SolarSystem:
    __instance = None
    __slots__ = ('_mercury', '_venus', '_earth', '_mars', '_jupiter', '_saturn', '_uranus', '_neptune')

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        
        return cls.__instance

    def __init__(self):
        self._mercury = Planet('Меркурий', 4878, 87.97, 1407.5)
        self._venus = Planet('Венера', 12104, 224.7, 5832.45)
        self._earth = Planet('Земля', 12756, 365.3, 23.93)
        self._mars = Planet('Марс', 6794, 687, 24.62)
        self._jupiter = Planet('Юпитер', 142800, 4330, 9.9)
        self._saturn = Planet('Сатурн', 120660, 10753, 10.63)
        self._uranus = Planet('Уран', 51118, 30665, 17.2)
        self._neptune = Planet('Нептун', 49528, 60150, 16.1)

s_system = SolarSystem()

"""
Подвиг 6. Объявите класс с именем Star (звезда), в объектах которого разрешены только локальные атрибуты с именами (ограничение задается через коллекцию __slots__):

_name - название звезды (строка);
_massa - масса звезды (любое положительное число); часто измеряется в массах Солнца;
_temp - температура поверхности звезды в Кельвинах (любое положительное число).
На основе класса Star объявите следующие дочерние классы:

WhiteDwarf - белый карлик;
YellowDwarf - желтый карлик;
RedGiant - красный гигант;
Pulsar - пульсар.

В каждом объекте этих классов должны быть разрешены (дополнительно к атрибутам базового класса Star) только следующие локальные атрибуты:

_type_star - название типа звезды (строка);
_radius - радиус звезды (любое положительное число); часто измеряется в радиусах Солнца.
Все эти объекты сохраните в виде списка stars. Затем, с помощью функций isinstance() и filter() сформируйте новый список с именем white_dwarfs, состоящий только из белых карликов (WhiteDwarf).
"""
class Star:
    __slots__ = ('_name', '_massa', '_temp')

    def __init__(self, name, massa, temp, type_star=None, radius=None):
        self._name = name
        self._massa = massa
        self._temp = temp
        self._type_star = type_star
        self._radius = radius

class WhiteDwarf(Star):
    __slots__ = ('_type_star', '_radius')

class YellowDwarf(Star):
    __slots__ = ('_type_star', '_radius')

class RedGiant(Star):
    __slots__ = ('_type_star', '_radius')

class Pulsar (Star):
    __slots__ = ('_type_star', '_radius')


stars = [RedGiant('Альдебаран', 5, 3600, 'красный гигант', 45),
         WhiteDwarf('Сириус А', 2.1, 9250, 'белый карлик', 2),
         WhiteDwarf('Сириус B', 1, 8200, 'белый карлик', 0.01),
         YellowDwarf('Солнце', 1, 6000, 'желтый карлик', 1)]

white_dwarfs = list(filter(lambda x: isinstance(x, WhiteDwarf), stars))

print(white_dwarfs)