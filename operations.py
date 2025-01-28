from calculator.complex_number import ComplexNumber

class Operations:
    @staticmethod
    def add(a: ComplexNumber, b: ComplexNumber) -> ComplexNumber:
        return ComplexNumber(a.real + b.real, a.imaginary + b.imaginary)

    @staticmethod
    def multiply(a: ComplexNumber, b: ComplexNumber) -> ComplexNumber:
        real = a.real * b.real - a.imaginary * b.imaginary
        imaginary = a.real * b.imaginary + a.imaginary * b.real
        return ComplexNumber(real, imaginary)

    @staticmethod
    def divide(a: ComplexNumber, b: ComplexNumber) -> ComplexNumber:
        if b.real == 0 and b.imaginary == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        denominator = b.real**2 + b.imaginary**2
        real = (a.real * b.real + a.imaginary * b.imaginary) / denominator
        imaginary = (a.imaginary * b.real - a.real * b.imaginary) / denominator
        return ComplexNumber(real, imaginary)
