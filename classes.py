from abc import ABCMeta, abstractmethod

"""
Создать класс Point, описывающий точку(атрибуты: x, y). Создать класс Figure.
Создать три дочерних класса Circle(атрибуты: координаты центра(тип Point),
длина радиуса; методы: нахождение периметра и площади окружности),
Triangle(атрибуты: три точки, методы: нахождение площади и периметра),
Square(атрибуты: две точки, методы: нахождениеплощади и периметра).
При потребности создавать все необходимыеметоды не описанные в задании.
Создать список фигур и в цикле подсчитать и вывести площади всех фигур на экран.
Примечание: в рамках задание создать два файла: classes.py и main.py.
 Впервом будут описаны все классы, во втором классы будути мпортированы и использованы.
"""


class Point:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Figure(metaclass=ABCMeta):
    @abstractmethod
    def perimetr(self):  # Периметр
        raise NotImplementedError("Необходимо переопределить метод")

    @abstractmethod
    def area(self):  # Площадь
        raise NotImplementedError("Необходимо переопределить метод")


class Circle(Point, Figure):
    radius: int

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def area(self):
        print(f"Площадь круга равна {3.14 * self.radius ** 2}")

    def perimetr(self):
        print(f"Пeриметр круга равен {2 * 3.14 * self.radius}")


class Triangle(Figure):
    a: Point
    b: Point
    c: Point

    perim: float
    l1: int
    l2: int
    l3: int

    def __init__(self, p1, p2, p3):
        self.a = p1
        self.b = p2
        self.c = p3

    def perimetr(self):
        self.l1 = ((abs(self.b.x - self.a.x)) ** 2 + (abs(self.b.y - self.a.y)) ** 2) ** (1 / 2)
        self.l2 = ((abs(self.c.x - self.a.x)) ** 2 + (abs(self.c.y - self.a.y)) ** 2) ** (1 / 2)
        self.l3 = ((abs(self.c.x - self.b.x)) ** 2 + (abs(self.c.y - self.b.y)) ** 2) ** (1 / 2)
        self.perim = self.l1 + self.l2 + self.l3
        print(self.perim)

    def area(self):
        per = self.perim / 2
        s = (per * (per - self.l1) * (per - self.l2) * (per - self.l3)) ** (1 / 2)
        print(s)


class Square(Figure):
    


"""
 def __init__(self, ctntre,  radius):
        self.centre = super().__init__(ctntre.x, ctntre.y)
        self.radius = radius
        """
