import sys

class Coefficient:
    def __init__(self, index, name):
        self.index = index
        self.name = name

        try:
            self.value = float(sys.argv[self.index])
        except:
            while True:
                try:
                    self.value = float(input(f"Введите коэффициент {self.name}: "))
                    break
                except ValueError:
                    print("Введите действительное число")

class BiquadrateEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        roots = set()

        discriminant = self.b.value * self.b.value - 4.0 * self.a.value * self.c.value

        if discriminant == 0.0:
            root = -self.b.value / (2.0 * self.a.value)
            if root >= 0:
                squered_root = root ** 0.5
                roots.add(squered_root)
                roots.add(-1 * squered_root)
        elif discriminant > 0:
            squared_discriminant = discriminant ** 0.5

            first_root = (-self.b.value + squared_discriminant)/(2.0 * self.a.value)
            second_root = (-self.b.value - squared_discriminant)/(2.0 * self.a.value)

            if first_root >= 0:
                squared_first_root = first_root ** 0.5
                roots.add(squared_first_root)
                roots.add(-1 * squared_first_root)
            
            if second_root >= 0:
                squared_second_root = second_root ** 0.5
                roots.add(squared_second_root)
                roots.add(-1 * squared_second_root)

        return roots
    
def main():
    a = Coefficient(1, "A")
    b = Coefficient(2, "B")
    c = Coefficient(3, "C")

    equation = BiquadrateEquation(a, b, c)

    roots = equation.solve()
    roots_amount = len(roots)

    if roots_amount == 0:
        print("Корней нет")
    elif roots_amount == 1:
        print(f"Корень уравнения: {roots[0]}")
    else:
        print(f"Корни уравнения:", *roots, sep=" ")

if __name__ == "__main__":
    main()