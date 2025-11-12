import sys

def get_coefficient(coefficient_index, coefficient_name):
    coefficient = 0

    try:
        coefficient = float(sys.argv[coefficient_index])
    except:
        while True:
            try:
                coefficient = float(input(f"Введите коэффициент {coefficient_name}: "))
                break
            except ValueError:
                print("Введите действительное число")
    
    return coefficient

def solve_biquadrate_equation(a, b, c):
    roots = set()

    discriminant = b * b - 4.0 * a * c

    if discriminant == 0.0:
        root = -b / (2.0 * a)
        if root >= 0:
            roots.add(root ** 0.5)
            roots.add(-1 * (root ** 0.5))
    elif discriminant > 0:
        squared_discriminant = discriminant ** 0.5

        first_root = (-b + squared_discriminant)/(2.0 * a)
        second_root = (-b - squared_discriminant)/(2.0 * a)

        if first_root >= 0:
            roots.add(first_root ** 0.5)
            roots.add(-1 * (first_root ** 0.5))
        
        if second_root >= 0:
            roots.add(second_root ** 0.5)
            roots.add(-1 * (second_root ** 0.5))

    return roots

def main():
    a = get_coefficient(1, "A")
    b = get_coefficient(2, "B")
    c = get_coefficient(3, "C")

    roots = solve_biquadrate_equation(a, b, c)

    roots_amount = len(roots)

    if roots_amount == 0:
        print("Корней нет")
    elif roots_amount == 1:
        print(f"Корень уравнения: {roots[0]}")
    else:
        print(f"Корни уравнения:", *roots, sep=" ")

if __name__ == "__main__":
    main()

