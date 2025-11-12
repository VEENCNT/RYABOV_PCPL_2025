from lab_python_oop.rectangle import Rectangle

class Square(Rectangle):
    figure_type = "Квадрат"

    @classmethod
    def get_figure_type(obj):
        return obj.figure_type

    def __init__(self, side, color):
        self._side = side
        super().__init__(self._side, self._side, color)
    
    def square(self):
        return self._width * self._width
    
    def __repr__(self):
        return '{} {} со стороной {} и площадью {}'.format(
            self._color.value,
            Square.get_figure_type(),
            self._side,
            self.square()
        )
