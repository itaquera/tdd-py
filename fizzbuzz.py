class FizzBuzz:

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