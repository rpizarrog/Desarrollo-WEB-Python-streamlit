"""
=========================================================
ARCHIVO
CProyecto.py

AUTOR
Rubén Pizarro Gurrola

FECHA
Agosto 2026

DESCRIPCIÓN

Clase coordinadora del proyecto de Regresión Bivariada.

Almacena la configuración general del proyecto y
coordina la comunicación entre las demás clases.

=========================================================
"""


#=========================================================
# CLASE
#=========================================================

class Proyecto:


    #=====================================================
    # CONSTRUCTOR
    #=====================================================

    def __init__(self):

        self.nombre = "Machine Learning. Regresión Bivariada"

        self.datos = None

        self.variable_independiente = None

        self.variable_dependiente = None

        self.contexto = ""

        self.modelo = "Lineal"

        self.entrenamiento = 80

        self.validacion = 20

        self.motor_ia = "Ollama"

        self.api_key = ""

        self.resultados = {}



    #=====================================================
    # DATOS
    #=====================================================

    def f_asignar_datos(self, datos):

        self.datos = datos


    def f_obtener_datos(self):

        return self.datos



    #=====================================================
    # CONTEXTO
    #=====================================================

    def f_asignar_contexto(self, contexto):

        self.contexto = contexto


    def f_obtener_contexto(self):

        return self.contexto



    #=====================================================
    # VARIABLES
    #=====================================================

    def f_asignar_variables(
            self,
            independiente,
            dependiente):

        self.variable_independiente = independiente

        self.variable_dependiente = dependiente


    def f_obtener_variable_independiente(self):

        return self.variable_independiente


    def f_obtener_variable_dependiente(self):

        return self.variable_dependiente



    #=====================================================
    # MODELO
    #=====================================================

    def f_asignar_modelo(self, modelo):

        self.modelo = modelo


    def f_obtener_modelo(self):

        return self.modelo



    #=====================================================
    # PARTICIÓN
    #=====================================================

    def f_asignar_particion(self, entrenamiento):

        self.entrenamiento = entrenamiento

        self.validacion = 100 - entrenamiento


    def f_obtener_entrenamiento(self):

        return self.entrenamiento


    def f_obtener_validacion(self):

        return self.validacion



    #=====================================================
    # MOTOR IA
    #=====================================================

    def f_asignar_motor_ia(self, motor):

        self.motor_ia = motor


    def f_obtener_motor_ia(self):

        return self.motor_ia



    #=====================================================
    # API KEY
    #=====================================================

    def f_asignar_api_key(self, api):

        self.api_key = api


    def f_obtener_api_key(self):

        return self.api_key



    #=====================================================
    # RESULTADOS
    #=====================================================

    def f_asignar_resultados(self, resultados):

        self.resultados = resultados


    def f_obtener_resultados(self):

        return self.resultados



    #=====================================================
    # RESUMEN DEL PROYECTO
    #=====================================================

    def f_resumen(self):

        return {

            "Proyecto" : self.nombre,

            "Modelo" : self.modelo,

            "Variable independiente" :
                self.variable_independiente,

            "Variable dependiente" :
                self.variable_dependiente,

            "Entrenamiento (%)" :
                self.entrenamiento,

            "Validación (%)" :
                self.validacion,

            "Motor IA" :
                self.motor_ia

        }