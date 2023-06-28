class FizzBuzz:
    def calculate(self, number):
        result = ""
        if number % 3 == 0:
            result += "Fizz"
        if number % 5 == 0:
            result += "Buzz"
        return result if result else str(number)

if __name__ == '__main__':
    fb = FizzBuzz()
    for i in range(1, 101):
        print(fb.calculate(i))