"""
=========================================================
ARCHIVO
CEstadisticos.py

AUTOR
Rubén Pizarro Gurrola

FECHA
Agosto 2026

DESCRIPCIÓN

Clase encargada de administrar el conjunto de datos.

Versión 1.0

Permite:

• Cargar archivos CSV y Excel.
• Obtener variables numéricas.
• Seleccionar variables de análisis.
• Recuperar los datos de cualquier variable.

Esta clase será reutilizada posteriormente en
Descriptivos, Regresión, PCA, Clustering,
Clasificación y otros modelos.

=========================================================
"""

#=========================================================
# LIBRERÍAS
#=========================================================

import pandas as pd

import numpy as np



#=========================================================
# CLASE
#=========================================================

class Estadisticos:


    #=====================================================
    # CONSTRUCTOR
    #=====================================================

    def __init__(self):

        self.datos = None

        self.variables = []



    def f_cargar_datos(self, archivo):

        #-----------------------------------------
        # Ya es un DataFrame
        #-----------------------------------------

        if isinstance(archivo, pd.DataFrame):

            self.datos = archivo.copy()

            return self.datos


        #-----------------------------------------
        # Ruta o URL
        #-----------------------------------------

        if isinstance(archivo, str):

            nombre = archivo.lower()

            if nombre.startswith(("http://","https://")):

                self.datos = pd.read_csv(archivo)

                return self.datos

            if nombre.endswith(".csv"):

                self.datos = pd.read_csv(archivo)

                return self.datos

            if nombre.endswith((".xlsx",".xls")):

                self.datos = pd.read_excel(archivo)

                return self.datos

            raise ValueError("Formato no soportado.")


        #-----------------------------------------
        # Archivo Streamlit
        #-----------------------------------------

        if hasattr(archivo, "name"):

            nombre = archivo.name.lower()

            if nombre.endswith(".csv"):

                self.datos = pd.read_csv(archivo)

            elif nombre.endswith((".xlsx",".xls")):

                self.datos = pd.read_excel(archivo)

            else:

                raise ValueError("Formato no soportado.")

            return self.datos


        raise TypeError(
            "Tipo de dato no soportado para cargar datos."
        )
        #=====================================================
    # DATOS
    #=====================================================

    def f_obtener_datos(self):

        return self.datos



    #=====================================================
    # VARIABLES NUMÉRICAS
    #=====================================================

    def f_obtener_variables_numericas(self):

        if self.datos is None:

            return []


        variables = list(

            self.datos.select_dtypes(

                include=np.number

            ).columns

        )

        return variables



    #=====================================================
    # SELECCIONAR VARIABLES
    #=====================================================

    def f_seleccionar_variables(

            self,

            variables):

        """
        variables

        Lista de nombres de variables.
        """

        if self.datos is None:

            raise ValueError(

                "No existen datos cargados."

            )


        for variable in variables:

            if variable not in self.datos.columns:

                raise ValueError(

                    f"La variable "

                    f"'{variable}' "

                    f"no existe."

                )


        self.variables = variables



    #=====================================================
    # VARIABLES SELECCIONADAS
    #=====================================================

    def f_obtener_variables(self):

        return self.variables



    #=====================================================
    # DATOS DE UNA VARIABLE
    #=====================================================

    def f_obtener_variable(

            self,

            variable):

        if variable not in self.datos.columns:

            raise ValueError(

                f"La variable "

                f"'{variable}' "

                f"no existe."

            )


        return self.datos[variable]



    #=====================================================
    # NÚMERO DE OBSERVACIONES
    #=====================================================

    def f_numero_observaciones(self):

        if self.datos is None:

            return 0


        return self.datos.shape[0]



    #=====================================================
    # NÚMERO DE VARIABLES
    #=====================================================

    def f_numero_variables(self):

        if self.datos is None:

            return 0


        return self.datos.shape[1]



    #=====================================================
    # RESUMEN
    #=====================================================

    def f_resumen(self):

        return {

            "Observaciones":

                self.f_numero_observaciones(),

            "Variables":

                self.f_numero_variables(),

            "Variables numéricas":

                self.f_obtener_variables_numericas(),

            "Variables seleccionadas":

                self.variables

        }

    #=====================================================
    # ESTADÍSTICOS DESCRIPTIVOS
    #=====================================================

    def f_estadisticos(self, variable):
        """
        Calcula los principales estadísticos descriptivos
        de una variable cuantitativa.

        Parameters
        ----------
        variable : str
            Nombre de la variable.

        Returns
        -------
        dict
            Diccionario con los estadísticos descriptivos.
        """

        if self.datos is None:

            raise ValueError(
                "No existen datos cargados."
            )

        if variable not in self.datos.columns:

            raise ValueError(
                f"La variable '{variable}' no existe."
            )

        datos = self.datos[variable].dropna()

        n = len(datos)

        media = datos.mean()

        mediana = datos.median()

        desviacion = datos.std()

        varianza = datos.var()

        coeficiente_variacion = (
            desviacion / media * 100
            if media != 0 else np.nan
        )

        minimo = datos.min()

        q1 = datos.quantile(0.25)

        q3 = datos.quantile(0.75)

        maximo = datos.max()

        rango = maximo - minimo

        rango_intercuartil = q3 - q1

        asimetria = datos.skew()

        curtosis = datos.kurt()

        return {

                "variable": variable,

                "n": n,

                "media": round(media, 4),

                "mediana": round(mediana, 4),

                "desviacion": round(desviacion, 4),

                "varianza": round(varianza, 4),

                "coeficiente_variacion": round(
                    coeficiente_variacion, 4
                ),

                "minimo": float(round(minimo, 4)),

                "q1": float(round(q1, 4)),

                "q3": float(round(q3, 4)),

                "maximo": float(round(maximo, 4)),

                "rango": float(round(rango, 4)),

                "rango_intercuartil": float(round(
                    rango_intercuartil, 4
                )),

                "asimetria": float(round(asimetria, 4)),

                "curtosis": float(round(curtosis, 4))
            }

    #=====================================================
    # COVARIANZA
    #=====================================================

    def f_covarianza(
            self,
            variable_x,
            variable_y):
        """
        Calcula la covarianza entre dos variables.
        """

        datos = self.datos[[variable_x, variable_y]].dropna()

        covarianza = datos.cov().iloc[0, 1]

        return {
            "variable_x": variable_x,
            "variable_y": variable_y,
            "covarianza": float(round(covarianza, 4))
        }


    #=====================================================
    # CORRELACIÓN
    #=====================================================

    def f_correlacion(
            self,
            variable_x,
            variable_y):
        """
        Calcula el coeficiente de correlación de Pearson.
        """

        datos = self.datos[[variable_x, variable_y]].dropna()

        correlacion = datos.corr().iloc[0, 1]

        return {
            "variable_x": variable_x,
            "variable_y": variable_y,
            "correlacion": float(round(correlacion, 4))
        }


    #=====================================================
    # MATRIZ DE CORRELACIÓN
    #=====================================================

    def f_matriz_correlacion(self):
        """
        Calcula la matriz de correlación para todas las
        variables numéricas.
        """

        variables = self.f_obtener_variables_numericas()

        matriz = self.datos[variables].corr()

        return matriz.round(4)


    #=====================================================
    # DATOS BIVARIADOS
    #=====================================================

    def f_obtener_datos_bivariados(
            self,
            variable_x,
            variable_y):
        """
        Devuelve únicamente las dos variables
        seleccionadas eliminando valores faltantes.
        """

        return self.datos[
            [variable_x, variable_y]
        ].dropna()


    #=====================================================
    # RESUMEN BIVARIADO
    #=====================================================

    def f_resumen_bivariado(
            self,
            variable_x,
            variable_y):
        """
        Devuelve un resumen con la covarianza y
        correlación entre dos variables.
        """

        cov = self.f_covarianza(
            variable_x,
            variable_y
        )

        cor = self.f_correlacion(
            variable_x,
            variable_y
        )

        return {

            "variable_x": variable_x,

            "variable_y": variable_y,

            "covarianza": cov["covarianza"],

            "correlacion": cor["correlacion"]

        }
                
     