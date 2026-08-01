#=========================================================
# CLASE
# CValidaciones
#=========================================================

class Validaciones:

    def validar_numeros(self, numero1, numero2):

        # 1. No vacíos
        self.validar_vacio(numero1, "Primer número")
        self.validar_vacio(numero2, "Segundo número")

        # 2. Convertir a float
        try:

            a = float(numero1)
            b = float(numero2)

        except ValueError:

            raise ValueError(
                "Los dos valores deben ser numéricos."
            )

        # 3. Validar positivos
        self.validar_positivo(a, "Primer número")
        self.validar_positivo(b, "Segundo número")

        # 4. Validar NO CERO segundo numero
        self.validar_no_cero_segundo(b, "Segundo número")

        # 5. Regresar valores válidos
        return a, b

    def validar_vacio(self, dato, nombre):
        if str(dato).strip() == "":
            raise ValueError(f"{nombre} está vacío.")


    def validar_positivo(self, numero, nombre):
        if numero < 0:
            raise ValueError(f"{nombre} debe ser positivo.")
    def validar_no_cero_segundo(self, numero, nombre):
        if numero == 0:
            raise ValueError(f"{nombre} No debe ser 0.")
