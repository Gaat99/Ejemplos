from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return 2 * (self.height + self.width)


class Square(Shape):
    def __init__(self, width):
        self.width = width

    def calculate_area(self):
        return self.width ** 2

    def calculate_perimeter(self):
        return 4 * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius


class ShapeFactory:
    def create_shape(self, name):
        if name == 'circulo':
            radius = input("Ingresa el radio del circulo: ")
            try:
                return Circle(float(radius))
            except ValueError:
                print("Error.. no es un numero valido.")
                return None
        elif name == 'rectangulo':
            height = input("Ingresa la altura: ")
            width = input("Ingresa el ancho:")
            try:
                return Rectangle(int(height), int(width))
            except ValueError:
                print("Error.. no valido:")
                return None
        elif name == 'cuadrado':
            width = input("Ingresa el ancho:")
            try:
                return Square(int(width))
            except ValueError:
                print("Error.. no es un numero valido.")
                return None
        else:
            print("Error... no es una figura valida!!")
            return None


if __name__ == "__main__":
    factory = ShapeFactory()
    shape_name = input("Ingresa la figura que deseas: ")
    shape = factory.create_shape(shape_name)

    if shape:
        print(f"Area: {shape.calculate_area()}")
        print(f"Perimetro: {shape.calculate_perimeter()}")
