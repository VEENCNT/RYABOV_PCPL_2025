from lab_python_oop.figure import Figure
from lab_python_oop.color import Color

class Rectangle(Figure):
    figure_type = "Прямоугольник"

    @classmethod
    def get_figure_type(obj):
        return obj.figure_type

    def __init__(self, width, height, color):
        self._width = width
        self._height = height
        self._color = Color()
        self._color.value = color

    def square(self):
        return self._width * self._height
    
    def __repr__(self):
        return "{} {} со сторонами {} и {} и площадью {}".format(
            self._color.value,
            Rectangle.get_figure_type(),
            self._width,
            self._height,
            self.square()
        )