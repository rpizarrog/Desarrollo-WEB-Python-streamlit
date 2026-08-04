"""
=========================================================
ARCHIVO
CEstadisticos.py

AUTOR
Rubén Pizarro Gurrola

FECHA
Agosto 2026

DESCRIPCIÓN

Clase responsable del análisis estadístico
de una variable cuantitativa.

FUNCIONES

• Cargar archivos CSV y Excel.
• Obtener variables numéricas.
• Seleccionar variable.
• Obtener datos.
• Calcular estadísticos descriptivos.
• Evaluar normalidad.
• Generar histograma.
• Generar diagrama de caja.
• Generar gráfico Q-Q.
=========================================================
"""

#=========================================================
# LIBRERÍAS
#=========================================================

import pandas as pd

import numpy as np

from scipy import stats

import matplotlib.pyplot as plt

from statistics import multimode

from scipy import stats


#=========================================================
# CLASE
#=========================================================

class Estadisticos:

    """
    Clase para analizar una variable cuantitativa.
    """

    #=====================================================
    # CONSTRUCTOR
    #=====================================================

    def __init__(self):

        self.datos = None

        self.variable = None

        self.contexto = ""

    #=====================================================
    # CARGAR DATOS
    #=====================================================


    def f_cargar_datos(self, archivo):
        """
        Carga un archivo CSV o Excel.

        Acepta:

        • Ruta del archivo (str o Path)
        • Archivo recibido desde Streamlit
        """

        #-----------------------------------------
        # Ruta (terminal)
        #-----------------------------------------

        if isinstance(archivo, str):

            nombre = archivo.lower()

            if nombre.endswith(".csv"):

                self.datos = pd.read_csv(archivo)

            elif nombre.endswith(".xlsx"):

                self.datos = pd.read_excel(archivo)

            else:

                raise ValueError(
                    "Formato no soportado."
                )

            return self.datos

        #-----------------------------------------
        # Streamlit
        #-----------------------------------------

        nombre = archivo.name.lower()

        if nombre.endswith(".csv"):

            self.datos = pd.read_csv(archivo)

        elif nombre.endswith(".xlsx"):

            self.datos = pd.read_excel(archivo)

        else:

            raise ValueError(
                "Formato no soportado."
            )

        return self.datos
    #=====================================================
    # VARIABLES NUMÉRICAS
    #=====================================================

    def f_obtener_variables(self):

        """
        Regresa únicamente las variables
        cuantitativas.
        """

        if self.datos is None:

            return []

        variables = self.datos.select_dtypes(

            include=np.number

        ).columns.tolist()

        return variables

    #=====================================================
    # SELECCIONAR VARIABLE
    #=====================================================

    def f_seleccionar_variable(

            self,

            variable):

        """
        Define la variable que será analizada.
        """

        if variable not in self.datos.columns:

            raise ValueError(

                "La variable no existe."
            )

        self.variable = variable

    #=====================================================
    # CONTEXTO
    #=====================================================

    def f_contexto(

            self,

            texto):

        """
        Guarda el contexto de la variable.
        """

        self.contexto = texto

    #=====================================================
    # OBTENER DATOS
    #=====================================================

    def f_obtener_datos(self):

        """
        Regresa únicamente la variable
        seleccionada.

        Elimina valores perdidos.
        """

        if self.variable is None:

            return None

        datos = self.datos[

            self.variable

        ].dropna()

        return datos

    #=====================================================
    # INFORMACIÓN
    #=====================================================

    def f_informacion(self):

        """
        Información general.
        """

        if self.datos is None:

            return None

        return {

            "registros": self.datos.shape[0],

            "variables": self.datos.shape[1],

            "nombre_variable": self.variable,

            "contexto": self.contexto}
    
    #=====================================================
    # DESCRIBIR DATOS
    #=====================================================

    def f_describir(self):
        """
        Genera los estadísticos descriptivos básicos
        mediante pandas.describe().
        """

        datos = self.f_obtener_datos()

        if datos is None:
            return None

        return datos.describe()

    #=====================================================
    # CALCULAR ESTADÍSTICOS
    #=====================================================

    def f_calcular_estadisticos(self):
        """
        Calcula los principales estadísticos descriptivos
        de la variable seleccionada.

        Regresa
        -------
        dict
            Diccionario con todos los estadísticos.
        """

        datos = self.f_obtener_datos()

        if datos is None:
            return None

        #---------------------------------------------
        # Conversión
        #---------------------------------------------

        datos = np.asarray(datos, dtype=float)

        #---------------------------------------------
        # Tamaño de muestra
        #---------------------------------------------

        n = len(datos)

        #---------------------------------------------
        # Tendencia central
        #---------------------------------------------

        media = np.mean(datos)

        mediana = np.median(datos)

        moda = multimode(datos)

        #---------------------------------------------
        # Dispersión
        #---------------------------------------------

        desviacion = np.std(
            datos,
            ddof=1
        )

        varianza = np.var(
            datos,
            ddof=1
        )

        if media != 0:
            cv = desviacion / media
        else:
            cv = np.nan

        #---------------------------------------------
        # Posición
        #---------------------------------------------

        minimo = np.min(datos)

        maximo = np.max(datos)

        rango = maximo - minimo

        q1 = np.percentile(datos, 25)

        q2 = np.percentile(datos, 50)

        q3 = np.percentile(datos, 75)

        iqr = q3 - q1

        #---------------------------------------------
        # Forma de la distribución
        #---------------------------------------------

        asimetria = stats.skew(
            datos,
            bias=False
        )

        curtosis = stats.kurtosis(
            datos,
            fisher=True,
            bias=False
        )    

        #---------------------------------------------
        # Valores atípicos
        #---------------------------------------------

        limite_inferior = q1 - 1.5 * iqr

        limite_superior = q3 + 1.5 * iqr

        valores_atipicos = datos[
            (datos < limite_inferior)
            |
            (datos > limite_superior)
        ]

        atipicos = len(valores_atipicos) > 0

        #---------------------------------------------
        # Diccionario
        #---------------------------------------------

        estadisticos = {

            "variable": self.variable,

            "contexto": self.contexto,

            "n": n,

            "media": media,

            "mediana": mediana,

            "moda": moda,

            "desviacion": desviacion,

            "varianza": varianza,

            "cv": cv,

            "minimo": minimo,

            "maximo": maximo,

            "rango": rango,

            "q1": q1,

            "q2": q2,

            "q3": q3,

            "iqr": iqr,

            "asimetria": asimetria,

            "curtosis": curtosis,

            "atipicos": atipicos,

            "numero_atipicos": len(valores_atipicos),

            "valores_atipicos": valores_atipicos.tolist()

        }

        return estadisticos

        #=====================================================
    # PRUEBA DE NORMALIDAD
    #=====================================================

    def f_prueba_shapiro(self):
        """
        Realiza la prueba de normalidad de Shapiro-Wilk.

        Regresa
        -------
        dict
        """

        datos = self.f_obtener_datos()

        if datos is None:

            return None

        W, p = stats.shapiro(datos)

        resultado = {

            "prueba": "Shapiro-Wilk",

            "W": W,

            "pvalor": p,

            "normal": p >= 0.05

        }

        return resultado

    #=====================================================
    # HISTOGRAMA
    #=====================================================
    def f_generar_histograma(self, figsize=(5,4)):
        """
        Genera un histograma de la variable
        mostrando:

        - Media
        - Mediana
        - Media ± Desviación estándar
        """

        datos = self.f_obtener_datos()

        media = datos.mean()
        mediana = datos.median()
        desviacion = datos.std()

        fig, ax = plt.subplots(figsize=figsize)

        #----------------------------------------
        # Histograma
        #----------------------------------------

        ax.hist(

            datos,

            bins="auto",

            edgecolor="black",

            alpha=0.75

        )


        #----------------------------------------
        # Media
        #----------------------------------------

        ax.axvline(

            media,

            color="red",

            linewidth=2,

            label=f"Media = {media:.2f}"

        )


        #----------------------------------------
        # Mediana
        #----------------------------------------

        ax.axvline(

            mediana,

            color="green",

            linewidth=2,

            label=f"Mediana = {mediana:.2f}"

        )


        #----------------------------------------
        # ± Desviación estándar
        #----------------------------------------

        ax.axvline(

            media - desviacion,

            color="blue",

            linestyle="--",

            linewidth=2,

            label=f"-1σ = {media-desviacion:.2f}"

        )


        ax.axvline(

            media + desviacion,

            color="blue",

            linestyle="--",

            linewidth=2,

            label=f"+1σ = {media+desviacion:.2f}"

        )


        #----------------------------------------
        # Etiquetas
        #----------------------------------------

        ax.set_title(

            f"Histograma\n{self.variable}"

        )

        ax.set_xlabel(

            self.variable

        )

        ax.set_ylabel(

            "Frecuencia"

        )


        #----------------------------------------
        # Leyenda
        #----------------------------------------

        ax.legend(

            fontsize=8,

            loc="best"

        )

        #-----------------------------------------
        # Pie de figura
        #-----------------------------------------

        n = len(datos)

        ax.text(

            0.5,

            -0.18,

            f"n = {n}      μ = {media:.2f}      Mediana = {mediana:.2f}      σ = {desviacion:.2f}",

            transform=ax.transAxes,

            ha="center",

            va="top",

            fontsize=9

        )


        plt.tight_layout()

        return fig

    #=====================================================
    # DIAGRAMA DE CAJA
    #=====================================================

    def f_generar_caja(self, figsize=(5,4)):
        """
        Genera un diagrama de caja.
        """

        datos = self.f_obtener_datos()

        fig, ax = plt.subplots(
            figsize=(5,4)
        )

        ax.boxplot(
            datos,
            vert=False
        )

        ax.set_title(
            f"Diagrama de caja\n{self.variable}"
        )

        ax.set_ylabel(self.variable)

        plt.tight_layout()

        return fig

    #=====================================================
    # QQPLOT
    #=====================================================

    def f_generar_qqplot(self, figsize=(5,4)):
        """
        Genera un gráfico Q-Q.
        """

        datos = self.f_obtener_datos()

        fig = plt.figure(
            figsize=(5,4)
        )

        ax = fig.add_subplot(111)

        stats.probplot(
            datos,
            dist="norm",
            plot=ax
        )

        ax.set_title(
            f"QQPlot\n{self.variable}"
        )

        plt.tight_layout()

        return fig

    #=====================================================
    # VISUALIZACIONES
    #=====================================================

    def f_generar_visualizaciones(self):
        """
        Genera las tres visualizaciones.

        Regresa

        dict
        """

        figuras = {

            "histograma": self.f_generar_histograma(),

            "caja": self.f_generar_caja(),

            "qqplot": self.f_generar_qqplot()

        }

        return figuras
