from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

from cowsay import cowsay

def main():
    rectangle = Rectangle(19, 19, "Синий")
    circle = Circle(19, "Зеленый")
    square = Square(19, "Красный")

    print(rectangle)
    print(circle)
    print(square)

    message = """
    There are always two roads in life: one is the first and the other is the second.

    -- Jason Statham
    """.strip()

    print(cowsay(message))

if __name__ == "__main__":
    main()