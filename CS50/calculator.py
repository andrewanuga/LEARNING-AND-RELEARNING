def main():
    while True:
        try:
            x = int(input("x: "))
            y = int(input("y: "))
            break
        except ValueError:
            print("Please enter valid integers.")

    calculate = Calculator(x, y)
    two_sum = calculate.sum()
    two_difference = calculate.difference()
    two_product = calculate.product()
    two_quotient = calculate.quotient()
    two_squares = calculate.square()

    print(f"{x} + {y} = {two_sum:,}") #`:,` is a format specifier that adds a comma as a thousands separator in the output. This makes it easier to read large numbers by grouping digits into sets of three.
    print(f"{x} - {y} = {two_difference:,}")
    print(f"{x} * {y} = {two_product:,}")
    print(f"{x} / {y} = {two_quotient:,}")
    print(f"{x}^2 = {two_squares[0]:,}")
    print(f"{y}^2 = {two_squares[1]:,}")


class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self):
        return self.x + self.y

    def difference(self):
        return self.x - self.y

    def product(self):
        return self.x * self.y

    def quotient(self):
        z = self.x / self.y
        return round(z)

    def square(self):
        return [self.x ** 2, self.y ** 2]


main()