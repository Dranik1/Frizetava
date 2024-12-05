class Calc:
    def __init__(self):
        try:
            self.num1=float(input())
            self.num2=float(input())
        except ValueError:
            print()

    def add(self):
        self.res=self.num1+self.num2

    def substract(self):
        self.res=self.num1-self.num2

    def multiplication(self):
        self.res=self.num1*self.num2

    def devision(self):
        try:
            self.res=self.num1/self.num2
        except ZeroDivisionError:
            print()
        