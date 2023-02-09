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
