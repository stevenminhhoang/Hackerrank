import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        mul = Complex(self.real, self.imaginary)
        mul.real = self.real * no.real - self.imaginary * no.imaginary
        mul.imaginary = self.real * no.imaginary + self.imaginary * no.real
        return mul

    def __truediv__(self, no):
        try:
            conjugate = Complex(no.real, -(no.imaginary))
            div = self * conjugate
            div.real /= (no * conjugate).real
            div.imaginary /= (no * conjugate).real
            return div
        except ZeroDivisionError as e:
            print(e)
            return None

    def mod(self):
        return Complex(math.sqrt(pow(self.real, 2) + pow(self.imaginary, 2)), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


c = map(float, input().split())
d = map(float, input().split())
x = Complex(*c)
y = Complex(*d)
print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
