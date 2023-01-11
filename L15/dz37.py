'''
Создайте класс «Прямоугольник», у которого необходимо реализовать два поля (ширина и высота) и несколько обязательных методов:

    Метод сравнения прямоугольников по площади.
    Метод сложения прямоугольников (площадь суммарного прямоугольника должна быть равна сумме площадей прямоугольников,
    которые вы складываете).
    Методы умножения прямоугольника на число n (это должно увеличить площадь базового прямоугольника в n раз).

В классе могут быть созданы и дополнительные (вспомогательные методы)

Несколько уточнений:

1. Методы сложения, умножения, деления и т.д. обязательно должны возвращать новый экземпляр класса Прямоугольник!

2. Для умножения, сложения, сравнения, обязательно нужно переопределять "магичиские" методы.
Для умножение есть встроенный метод __mul__

3. Когда в результате мат. действий создаете новый экземпляр класса Прямоугольник, то у этого экземпляра,
перемножение сторон, должно давать нужную площадь. Это тоже важно

https://ru.onlinemschool.com/math/formula/rectangle/
'''

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return int(self.width * self.height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.get_square() == other.get_square())
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Rectangle):
            #return Rectangle(self.width, (self.get_square() + other.get_square()) / self.width)
            return Rectangle(self.width, (self.get_square() + other.get_square()) / self.width)
        return NotImplemented

    def __mul__(self, n):
        if isinstance(n, int):
            return Rectangle(self.width, (self.get_square() * n)/self.width)
        return NotImplemented

    def __truediv__(self, m):
        if isinstance(m, int):
            return Rectangle(self.width, (self.get_square() / m) / self.width)
        return NotImplemented

    def __str__(self):
        return f"[width = {self.width}, height = {self.height}]"

r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8
assert r2.get_square() == 18
#print(r1)
#print(r2)
#print(r1.get_square() == 9)
#print(r1.get_square() == 8)
#print(r1.get_square())
#print(r2.get_square() == 18)
#print(r2.get_square())

r3 = r1 + r2
#print(r3)
assert r3.get_square() == 26
#print(r3.get_square() == 26)
#print(r3.get_square())

r4 = r1 * 4
#print(r4)
assert r4.get_square() == 32
#print(r4.get_square() == 32)
#print(r4.get_square())

r5 = r1 / 4
assert r5.get_square() == 2
#print(r5.get_square() == 2)
#print(r5.get_square())