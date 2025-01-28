from calculator.complex_number import ComplexNumber

class ComplexNumberFactory:
    @staticmethod
    def create(real: float, imaginary: float) -> ComplexNumber:
        return ComplexNumber(real, imaginary)
