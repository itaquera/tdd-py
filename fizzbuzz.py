class FizzBuzz:
    def __init__(self):
        self.rules = [self.fizzbuzz, self.fizz, self.buzz]

    def fizz(self, number):
        if number % 3 == 0:
            return "Fizz"
        return ""

    def buzz(self, number):
        if number % 5 == 0:
            return "Buzz"
        return ""

    def fizzbuzz(self, number):
        if number % 15 == 0:
            return "FizzBuzz"
        return ""

    def calculate(self, number):
        result = "".join(rule(number) for rule in self.rules)
        return result if result else str(number)