"""
=========================================================
ARCHIVO
CEstadisticos.py

AUTOR
Rubén Pizarro Gurrola

FECHA
Agosto 2026
=========================================================
"""

from io import StringIO

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Estadisticos:

    #=====================================================
    # f_generar_normales()
    # Genera números aleatorios con distribución Normal
    #=====================================================

    def f_generar_normales(
            self,
            n=30,
            media=0,
            desviacion=1,
            semilla=None,
            etiqueta="Números"):

        """
        Genera números aleatorios con distribución Normal.

        Parámetros
        ----------
        n : int
            Cantidad de números a generar.

        media : float
            Media de la distribución.

        desviacion : float
            Desviación estándar.

        semilla : int
            Semilla para reproducibilidad.

        etiqueta : str
            Nombre de la variable.

        Regresa
        --------
        datos : numpy.ndarray

        etiqueta : str
        """

        if semilla is not None:

            np.random.seed(semilla)

        datos = np.round(

            np.random.normal(

                loc=media,
                scale=desviacion,
                size=n

            ),

            2

        )

        return datos, etiqueta


    #=====================================================
    # f_convertir_df()
    # Convierte un vector a DataFrame
    #=====================================================

    def f_convertir_df(
            self,
            datos,
            variables=None):

        if variables is None:

            variables = "Variable"

        datos = pd.DataFrame(
            datos,
            columns=[variables]
        )

        return datos


    #=====================================================
    # f_describir_datos()
    # Obtiene estadísticos descriptivos y estructura
    #=====================================================

    def f_describir_datos(
            self,
            datos):

        describe = datos.describe()

        buffer = StringIO()

        datos.info(buf=buffer)

        structure = buffer.getvalue()

        return {

            "describe": describe,

            "structure": structure

        }

    #=====================================================
    # f_redondear_datos()
    #=====================================================
    def f_redondear_datos(
            self,
            datos,
            decimales=0):

        return datos.round(decimales)

    #=====================================================
    # f_generar_histograma()
    #=====================================================

    def f_generar_histograma(
        self,
        datos,
        variable):

        media = datos[variable].mean()
        mediana = datos[variable].median()
        desviacion = datos[variable].std()

        fig, ax = plt.subplots(figsize=(7,5))

        ax.hist(
            datos[variable],
            bins=10,
            edgecolor="black"
        )

        ax.set_title(
            f"Histograma de {variable}",
            fontsize=14,
            fontweight="bold"
        )

        ax.set_xlabel(variable)
        ax.set_ylabel("Frecuencia")

        ax.text(
            0.5,
            -0.18,
            f"μ = {media:.2f}    Me = {mediana:.2f}    σ = {desviacion:.2f}",
            transform=ax.transAxes,
            ha="center",
            fontsize=10
        )

        fig.tight_layout()

        return fig


    #=====================================================
    # f_generar_caja()
    #=====================================================
    def f_generar_caja(
            self,
            datos,
            variable):

        media = datos[variable].mean()
        mediana = datos[variable].median()
        desviacion = datos[variable].std()

        fig, ax = plt.subplots(figsize=(7,5))

        ax.boxplot(
            datos[variable],
            vert=False
        )

        ax.set_title(
            f"Diagrama de Caja de {variable}",
            fontsize=14,
            fontweight="bold"
        )

        ax.set_ylabel(variable)

        ax.text(
            0.5,
            -0.18,
            f"μ = {media:.2f}    Me = {mediana:.2f}    σ = {desviacion:.2f}",
            transform=ax.transAxes,
            ha="center",
            fontsize=10
        )

        fig.tight_layout()

        return fig