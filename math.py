
import cmath
class Shape:
    def __init__(self, a=10, b=6, c=1):
        self.set_params(a, b, c)

    def set_params(self, a, par_b, c):
        self._a = a
        self.b = par_b
        self.c = c

    def get_a(self):
        return self._a

    def perimeter(self):
        return self._a + self.b + self.c

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a) + " by " + str(self.b) + "] at " + str(hex(id(self)))


class Triangle(Shape):
    def calc_surface(self):
        p = self.perimeter() / 2
        area = cmath.sqrt(p * (p - self._a) * (p - self.b) * (p - self.c))
        r_area= area.real
        return r_area

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a) + " by " + str(self.b) + " by "+str(self.c)+ "] at " + str(hex(id(self)))
class EquilateralTriangle (Triangle):
    def __init__(self, a):

        super().__init__(a, a, a)

class Rectangle(Shape):
    def __init__(self, a, b):
        # call constructor of superclass (parent)
        super().__init__(a, b, 0)

    def calc_surface(self):
        return self._a * self.b
    def perimeter(self):
        return 2*(self._a + self.b)

    def swap_sides(self):
        a = self._a
        b = self.b
        self._a = b
        self.b = a

class Squer (Rectangle):
    def __init__(self, a):

        super().__init__(a, a)

class Circle(Shape):
    def __init__(self, a):
        # call constructor of superclass (parent)
        super().__init__(a, 0, 0)
        # self._a = a

    def calc_surface(self):
        return  cmath.pi* self._a**2

    def perimeter(self):
        return 2*cmath.pi* self._a

    def __repr__(self):
        return self.__class__.__name__ + "[r=" + str(self._a) + "] at " + str(hex(id(self)))


r = Rectangle(5, 6)
print(r)
# r._a = 600
print(r.calc_surface())
print(r.perimeter())
r.swap_sides()
print(r)


S = Squer(3)
print(S)
print(S.calc_surface())
print(S.perimeter())

c = Circle(7)
print(c)
print(c.calc_surface())
print(c.perimeter())

t= Triangle(3,4,5)
print(t)
print(t.calc_surface())
print(t.perimeter())

E= EquilateralTriangle(5)
print(E)
print(E.calc_surface())
print(E.perimeter())

Triangle.