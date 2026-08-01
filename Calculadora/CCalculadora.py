#=========================================================
# calculadora.py
# Lógica de negocio
#=========================================================

class Calculadora:

    #-----------------------------------------
    # VALIDAR
    #-----------------------------------------

    def validar(self, numero1, numero2):

        try:

            a = float(numero1)
            b = float(numero2)

            return a, b

        except:

            raise ValueError(
                "Los dos valores deben ser numéricos."
            )

    #-----------------------------------------

    def sumar(self, a, b):

        return a + b

    #-----------------------------------------

    def restar(self, a, b):

        return a - b

    #-----------------------------------------

    def multiplicar(self, a, b):

        return a * b

    #-----------------------------------------

    def dividir(self, a, b):

        if b == 0:

            raise ValueError(
                "No es posible dividir entre cero."
            )

        return a / b

    #-----------------------------------------

    def potencia(self, a, b):

        return a ** b

    #-----------------------------------------

    def raiz(self, a, b):

        if b == 0:

            raise ValueError(
                "El índice de la raíz no puede ser cero."
            )

        if a < 0 and int(b) % 2 == 0:

            raise ValueError(
                "No existe raíz par de un número negativo."
            )

        return a ** (1 / b)