class FizzBuzz:
    def __init__(self):
        self.rules = [self.fizz, self.buzz]

    def fizz(self, number):
        if number % 3 == 0:
            return "Fizz"
        return ""

    def buzz(self, number):
        if number % 5 == 0:
            return "Buzz"
        return ""

    def calculate(self, number):
        result = "".join(rule(number) for rule in self.rules)
        return result if result else str(number)

if __name__ == '__main__':
    fb = FizzBuzz()
    for i in range(1, 101):
        print(fb.calculate(i))