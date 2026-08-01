
# app.py Es el programa principal
# Autor: RUBEN PIZARRO GURROLA
# Fecha: Julio 2026
# Objetivo: Crear calculadora sencilla WEB con streamlit y clsaes personalziadas

# Se importan los archivos con las clases

# IMPORTAR CLASES
from CCalculadora import Calculadora
from CValidaciones import Validaciones

# CREAR OBJETOS
calc = Calculadora()
valid = Validaciones()

# DATOS DE PRUEBA

numero1 = 10
numero2 = 4

# VALIDAR LOS DATOS
try:

    a, b = valid.validar_numeros(numero1, numero2)
    # OPERACIONES

    print(f"Suma            : {calc.sumar(a,b)}")
    print(f"Resta           : {calc.restar(a,b)}")
    print(f"Multiplicación  : {calc.multiplicar(a,b)}")
    print(f"División        : {calc.dividir(a,b)}")
    print(f"Potencia        : {calc.potencia(a,b)}")
    print(f"Raíz            : {calc.raiz(a,b)}")

except Exception as e:
    print(f"ERROR: {e}")