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
    