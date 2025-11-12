import math

from lab_python_oop.figure import Figure
from lab_python_oop.color import Color

class Circle(Figure):
    figure_type = "Круг"

    @classmethod
    def get_figure_type(obj):
        return obj.figure_type

    def __init__(self, radius, color):
        self._radius = radius
        self._color = Color()
        self._color.value = color

    def square(self):
        return math.pi * self._radius ** 2
    
    def __repr__(self):
        return "{} {} с радиусом {} и площадью {}".format(
            self._color.value,
            Circle.get_figure_type(),
            self._radius,
            self.square()
        )