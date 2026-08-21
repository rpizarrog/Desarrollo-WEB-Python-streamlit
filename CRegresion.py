"""
=========================================================
ARCHIVO
CRegresion.py

AUTOR
Rubén Pizarro Gurrola

FECHA
Agosto 2026

DESCRIPCIÓN

Clase encargada de construir modelos de
Regresión Bivariada.

Versión 1.0

Parte A

Administración del modelo.

=========================================================
"""

#=========================================================
# LIBRERÍAS
#=========================================================

import pandas as pd

import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

from sklearn.metrics import (
    r2_score,
    mean_squared_error,
    mean_absolute_error,
    mean_absolute_percentage_error
)

import matplotlib.pyplot as plt

from scipy import stats

from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.api import add_constant

from statsmodels.stats.stattools import durbin_watson

from sklearn.preprocessing import PolynomialFeatures

import streamlit as st

from statsmodels.api import OLS, add_constant
from statsmodels.stats.diagnostic import linear_reset




#=========================================================
# CLASE
#=========================================================

class Regresion:


    #=====================================================
    # CONSTRUCTOR
    #=====================================================

    def __init__(self):

        self.datos = None

        self.variable_x = None

        self.variable_y = None

        self.tipo = "Lineal"

        self.grado = 1

        self.entrenamiento = 80

        self.validacion = 20

        self.X_train = None

        self.X_test = None

        self.y_train = None

        self.y_test = None

        self.modelo = None

        self.predicciones = None

        self.metricas = {}

        self.coeficientes = {}

        self.modelo_statsmodels = None



    #=====================================================
    # DATOS
    #=====================================================

    def f_asignar_datos(
            self,
            datos):

        self.datos = datos.copy()




    #=====================================================
    # VARIABLES
    #=====================================================

    def f_asignar_variables(
            self,
            variable_x,
            variable_y):

        self.variable_x = variable_x

        self.variable_y = variable_y



    def f_obtener_variable_x(self):

        return self.variable_x



    def f_obtener_variable_y(self):

        return self.variable_y


    #=====================================================
    # MODELO
    #=====================================================

    def f_asignar_modelo(
            self,
            tipo="Lineal",
            grado=1):

        self.tipo = tipo

        self.grado = grado



    def f_obtener_modelo(self):

        return {

            "tipo": self.tipo,

            "grado": self.grado

        }



    #=====================================================
    # PARTICIÓN
    #=====================================================

    def f_asignar_particion(
            self,
            entrenamiento=80):

        self.entrenamiento = entrenamiento

        self.validacion = 100 - entrenamiento



    #=====================================================
    # DIVISIÓN ENTRENAMIENTO / VALIDACIÓN
    #=====================================================

    def f_dividir_datos(self):

        if self.datos is None:

            raise ValueError(
                "No existen datos cargados."
            )


        X = self.datos[[self.variable_x]]

        y = self.datos[self.variable_y]


        self.X_train, self.X_test, \
        self.y_train, self.y_test = train_test_split(

            X,

            y,

            train_size=
            self.entrenamiento / 100,

            random_state=1234

        )



    #=====================================================
    # DATOS ENTRENAMIENTO
    #=====================================================

    def f_obtener_entrenamiento(self):

        return self.X_train, self.y_train



    #=====================================================
    # DATOS VALIDACIÓN
    #=====================================================

    def f_obtener_validacion(self):

        return self.X_test, self.y_test



    #=====================================================
    # RESUMEN
    #=====================================================

    def f_resumen(self):

        return {

            "Modelo": self.tipo,

            "Grado": self.grado,

            "Variable X": self.variable_x,

            "Variable Y": self.variable_y,

            "Entrenamiento (%)":
                self.entrenamiento,

            "Validación (%)":
                self.validacion,

            "Observaciones":
                len(self.datos)

        }
    

    #=====================================================
    # CREAR MODELO
    #=====================================================

    def f_crear_modelo(self):
        """
        Construye el modelo de regresión
        seleccionado por el usuario.
        """

        st.session_state["modelo_construido"] = True

        st.session_state["interpretacion_generada"] = False
        st.session_state["interpretacion_experto"] = ""

        st.session_state["interpretacion_ia"] = ""

        st.session_state["prompt_ia"] = ""

        #=================================================
        # REGRESIÓN LINEAL
        #=================================================

        if self.tipo.lower() == "lineal":

            self.transformador = None

            self.modelo = LinearRegression()

            self.modelo.fit(

                self.X_train,

                self.y_train

            )

            X = add_constant(self.X_train)

            self.modelo_statsmodels = OLS(

                self.y_train,

                X

            ).fit()

        #=================================================
        # REGRESIÓN POLINOMIAL
        #=================================================

        elif self.tipo.lower() == "polinomial":

            self.transformador = PolynomialFeatures(

                degree=self.grado,

                include_bias=False

            )

            X_train_poly = self.transformador.fit_transform(

                self.X_train

            )

            self.modelo = LinearRegression()

            self.modelo.fit(

                X_train_poly,

                self.y_train

            )

            X = add_constant(X_train_poly)

            self.modelo_statsmodels = OLS(

                self.y_train,

                X

            ).fit()

        #=================================================
        # REGRESIÓN EXPONENCIAL
        #=================================================

        elif self.tipo.lower() == "exponencial":

            y_train_log = np.log(self.y_train)

            self.modelo = LinearRegression()

            self.modelo.fit(

                self.X_train,

                y_train_log

            )

            X = add_constant(self.X_train)

            self.modelo_statsmodels = OLS(

                y_train_log,

                X

            ).fit()

        #=================================================
        # REGRESIÓN LOGARÍTMICA
        #=================================================

        elif self.tipo.lower() == "logarítmica":

            if np.any(self.X_train <= 0):

                raise ValueError(
                    "La regresión logarítmica requiere X > 0."
                )

            X_train_log = np.log(self.X_train)

            self.modelo = LinearRegression()

            self.modelo.fit(

                X_train_log,

                self.y_train

            )

            X = add_constant(X_train_log)

            self.modelo_statsmodels = OLS(

                self.y_train,

                X

            ).fit()

        #=================================================
        # REGRESIÓN POTENCIAL
        #=================================================

        elif self.tipo.lower() == "potencial":

            if np.any(self.X_train <= 0):

                raise ValueError(
                    "La regresión potencial requiere X > 0."
                )

            if np.any(self.y_train <= 0):

                raise ValueError(
                    "La regresión potencial requiere Y > 0."
                )

            X_log = np.log(self.X_train)

            y_log = np.log(self.y_train)

            self.modelo = LinearRegression()

            self.modelo.fit(

                X_log,

                y_log

            )

            X = add_constant(X_log)

            self.modelo_statsmodels = OLS(

                y_log,

                X

            ).fit()

        #=================================================
        # MODELO NO SOPORTADO
        #=================================================

        else:

            raise ValueError(

                f"Modelo '{self.tipo}' no soportado."

            )

    #=====================================================
    # PREDICCIONES
    #=====================================================

    def f_predecir(self):
        """
        Genera las predicciones del modelo para
        los conjuntos de entrenamiento y validación.
        """

        if self.modelo is None:

            raise ValueError(
                "Primero debe construir el modelo."
            )

        #-----------------------------------------
        # Predicciones
        #-----------------------------------------

        pred_train = self.f_predict_regresiones(

            self.X_train

        )

        pred_test = self.f_predict_regresiones(

            self.X_test

        )

        #-----------------------------------------
        # Almacenar predicciones
        #-----------------------------------------

        self.predicciones = {

            "entrenamiento": pred_train,

            "validacion": pred_test

        }

        return self.predicciones
    
    #=====================================================
    # COEFICIENTES
    #=====================================================

    def f_coeficientes(self):
        """
        Obtiene los coeficientes del modelo
        de regresión.

        Compatible con:

        • Lineal
        • Polinomial
        • Exponencial
        • Logarítmica
        • Potencial
        """

        if self.modelo is None:

            raise ValueError(
                "No existe un modelo entrenado."
            )

        #-----------------------------------------
        # REGRESIÓN EXPONENCIAL
        #-----------------------------------------

        if self.tipo.lower() == "exponencial":

            return {

                "intercepto": round(

                    float(np.exp(
                        self.modelo.intercept_
                    )),

                    4

                ),

                "b1": round(

                    float(
                        self.modelo.coef_[0]
                    ),

                    4

                )

            }

        #-----------------------------------------
        # REGRESIÓN POTENCIAL
        #-----------------------------------------

        elif self.tipo.lower() == "potencial":

            return {

                "intercepto": round(

                    float(np.exp(
                        self.modelo.intercept_
                    )),

                    4

                ),

                "b1": round(

                    float(
                        self.modelo.coef_[0]
                    ),

                    4

                )

            }

        #-----------------------------------------
        # LINEAL, POLINOMIAL Y LOGARÍTMICA
        #-----------------------------------------

        else:

            coeficientes = {

                "intercepto": round(

                    float(
                        self.modelo.intercept_
                    ),

                    4

                )

            }

            for i, coef in enumerate(

                self.modelo.coef_,

                start=1

            ):

                coeficientes[f"b{i}"] = round(

                    float(coef),

                    4

                )

            return coeficientes

    #=====================================================
    # ECUACIÓN DEL MODELO
    #=====================================================

    def f_ecuacion(self):
        """
        Devuelve la ecuación del modelo
        de regresión.

        Compatible con:

        • Lineal
        • Polinomial
        • Exponencial
        • Logarítmica
        • Potencial
        """

        coef = self.f_coeficientes()

        #-----------------------------------------
        # REGRESIÓN LINEAL
        #-----------------------------------------

        if self.tipo.lower() == "lineal":

            ecuacion = (

                f"ŷ = {coef['intercepto']} "

                f"+ {coef['b1']}x"

            )

        #-----------------------------------------
        # REGRESIÓN POLINOMIAL
        #-----------------------------------------

        elif self.tipo.lower() == "polinomial":

            ecuacion = (

                f"ŷ = {coef['intercepto']}"

            )

            for i in range(1, self.grado + 1):

                ecuacion += (

                    f" + {coef[f'b{i}']}x^{i}"

                )

        #-----------------------------------------
        # REGRESIÓN EXPONENCIAL
        #-----------------------------------------

        elif self.tipo.lower() == "exponencial":

            ecuacion = (

                f"ŷ = {coef['intercepto']}"

                f"·e^({coef['b1']}x)"

            )

        #-----------------------------------------
        # REGRESIÓN LOGARÍTMICA
        #-----------------------------------------

        elif self.tipo.lower() == "logarítmica":

            a = coef["intercepto"]

            b = coef["b1"]

            ecuacion = (

                f"ŷ = {a:.4f}"

                f" {'+' if b>=0 else '-'} "

                f"{abs(b):.4f}·ln(x)"

            )


        #-----------------------------------------
        # REGRESIÓN POTENCIAL
        #-----------------------------------------

        elif self.tipo.lower() == "potencial":

            a = coef["intercepto"]
            b = coef["b1"]

            ecuacion = (

                f"ŷ = {a:.4f}·x^{b:.4f}"

            )
            

        else:

            ecuacion = "Modelo no soportado."

        return {

            "ecuacion": ecuacion

        }
    #=====================================================
    # EVALUACIÓN DEL MODELO
    #=====================================================

    def f_evaluacion_modelo(self):
        """
        Calcula las principales métricas de evaluación
        del modelo de regresión.
        """

        if self.modelo is None:

            raise ValueError(
                "No existe un modelo entrenado."
            )

        #-----------------------------------------
        # Valores reales y predichos
        #-----------------------------------------

        y_real = self.y_test

        y_pred = self.predicciones["validacion"]

        #-----------------------------------------
        # Número de parámetros del modelo
        #-----------------------------------------

        if self.tipo.lower() == "lineal":

            p = 1

        elif self.tipo.lower() == "polinomial":

            p = self.grado

        else:

            # Exponencial, Logarítmico y Potencial
            p = 1

        #-----------------------------------------
        # Métricas
        #-----------------------------------------

        r2 = r2_score(
            y_real,
            y_pred
        )

        n = len(y_real)

        r2_ajustado = (

            1 -

            ((1-r2)*(n-1))

            /

            (n-p-1)

        )

        mse = mean_squared_error(
            y_real,
            y_pred
        )

        rmse = np.sqrt(mse)

        mae = mean_absolute_error(
            y_real,
            y_pred
        )

        if np.any(y_real == 0):

            mape = np.nan

        else:

            mape = (

                mean_absolute_percentage_error(

                    y_real,

                    y_pred

                ) * 100

            )

        #-----------------------------------------
        # RSS
        #-----------------------------------------

        rss = np.sum(

            (y_real-y_pred)**2

        )

        #-----------------------------------------
        # AIC
        #-----------------------------------------

        aic = (

            n*np.log(rss/n)

            +

            2*(p+1)

        )

        #-----------------------------------------
        # BIC
        #-----------------------------------------

        bic = (

            n*np.log(rss/n)

            +

            np.log(n)*(p+1)

        )

        #-----------------------------------------
        # Guardar métricas
        #-----------------------------------------

        self.metricas = {

            "R2":
                round(float(r2),4),

            "R2_Ajustado":
                round(float(r2_ajustado),4),

            "MSE":
                round(float(mse),4),

            "RMSE":
                round(float(rmse),4),

            "MAE":
                round(float(mae),4),

            "MAPE":
                round(float(mape),4)
                if not np.isnan(mape)
                else np.nan,

            "AIC":
                round(float(aic),4),

            "BIC":
                round(float(bic),4)

        }

        return self.metricas

    #=====================================================
    # MODELO COMPLETO
    #=====================================================

    def f_modelo(self):
        """
        Devuelve toda la información del modelo
        en un único diccionario.
        """

        return {

            "modelo":

                self.f_obtener_modelo(),

            "coeficientes":

                self.f_coeficientes(),

            "ecuacion":

                self.f_ecuacion(),

            "metricas":

                self.metricas

        }


    #=====================================================
    # GRÁFICA DEL MODELO
    #=====================================================

    def f_generar_grafica_modelo(
            self,
            titulo=None,
            mostrar_ecuacion=False,
            mostrar_R2=True,
            mostrar_n=True,
            mostrar_grid=True,
            figsize=(8,6)):
        """
        Genera la gráfica del modelo de regresión.

        Compatible con:

        • Lineal
        • Polinomial
        • Exponencial
        """

        if self.modelo is None:

            raise ValueError(
                "Primero debe construir el modelo."
            )

        #-------------------------------------------------
        # Datos entrenamiento y validación
        #-------------------------------------------------

        X_train = self.X_train
        y_train = self.y_train

        X_test = self.X_test
        y_test = self.y_test

        #-------------------------------------------------
        # Curva del modelo
        #-------------------------------------------------

        X_grafica = np.linspace(

            self.datos[self.variable_x].min(),

            self.datos[self.variable_x].max(),

            300

        ).reshape(-1,1)

        #-------------------------------------------------
        # Predicciones del modelo
        #-------------------------------------------------

        Y_grafica = self.f_predict_regresiones(

            X_grafica

        )

        #-------------------------------------------------
        # Figura
        #-------------------------------------------------

        fig, ax = plt.subplots(

            figsize=figsize

        )

        #-------------------------------------------------
        # Entrenamiento
        #-------------------------------------------------

        ax.scatter(

            X_train,

            y_train,

            s=18,

            alpha=0.45,

            color="steelblue",

            edgecolors="none",

            label="Entrenamiento",

            zorder=1

        )

        #-------------------------------------------------
        # Validación
        #-------------------------------------------------

        ax.scatter(

            X_test,

            y_test,

            s=24,

            alpha=0.80,

            color="darkorange",

            edgecolors="black",

            linewidth=0.30,

            label="Validación",

            zorder=2

        )

        #-------------------------------------------------
        # Curva ajustada
        #-------------------------------------------------

        ax.plot(

            X_grafica.ravel(),

            Y_grafica,

            color="red",

            linewidth=3,

            label="Modelo",

            zorder=3

        )

        #-------------------------------------------------
        # Título
        #-------------------------------------------------

        if titulo is None:

            if self.tipo.lower() == "polinomial":

                titulo = (

                    f"Regresión Polinomial "
                    f"grado {self.grado}"

                )

            else:

                titulo = (

                    f"Regresión {self.tipo}"

                )

        ax.set_title(

            titulo,

            fontsize=20,

            fontweight="bold"

        )

        #-------------------------------------------------
        # Etiquetas
        #-------------------------------------------------

        ax.set_xlabel(

            self.variable_x,

            fontsize=15,

            fontweight="bold"

        )

        ax.set_ylabel(

            self.variable_y,

            fontsize=15,

            fontweight="bold"

        )

        #-------------------------------------------------
        # Cuadrícula
        #-------------------------------------------------

        if mostrar_grid:

            ax.grid(

                linestyle="--",

                alpha=0.35

            )

        #-------------------------------------------------
        # Información
        #-------------------------------------------------

        texto = ""

        if mostrar_ecuacion:

            texto += self.f_ecuacion()["ecuacion"]

        if mostrar_R2:

            texto += (

                f"\n\nR² = {self.metricas['R2']}"

            )

        if mostrar_n:

            texto += (

                f"\n\nn_train = {len(X_train)}"

                f"\n"

                f"n_test = {len(X_test)}"

            )

        if texto != "":

            ax.text(

                0.72,

                0.94,

                texto,

                transform=ax.transAxes,

                fontsize=11,

                verticalalignment="top",

                bbox=dict(

                    facecolor="white",

                    edgecolor="black",

                    alpha=0.95,

                    boxstyle="round,pad=0.6"

                )

            )

        #-------------------------------------------------
        # Leyenda
        #-------------------------------------------------

        ax.legend()

        #-------------------------------------------------
        # Pie
        #-------------------------------------------------

        ax.text(

            0.50,

            -0.12,

            f"Entrenamiento: {self.entrenamiento}%     "

            f"Validación: {self.validacion}%",

            transform=ax.transAxes,

            ha="center",

            fontsize=10

        )

        #-------------------------------------------------
        # Ajuste final
        #-------------------------------------------------

        plt.tight_layout()

        return {

            "figura": fig

        }

    #=====================================================
    # VERIFICAR ESPECIFICACIÓN DEL MODELO
    #=====================================================
    
    def f_verificar_linealidad(self):
        """
        Evalúa la adecuación de la forma funcional
        mediante la prueba Ramsey RESET.
        """

        resultado = linear_reset(

            self.modelo_statsmodels,

            power=2,

            use_f=True

        )

        return {

            "Prueba": "Ramsey RESET",

            "F": round(float(resultado.fvalue), 4),

            "p_valor": round(float(resultado.pvalue), 4)

        } 


    #=====================================================
    # GRÁFICA DE RESIDUOS
    #=====================================================

    def f_generar_residuos(
            self,
            titulo="Gráfico de Residuos",
            mostrar_grid=True,
            figsize=(8,6)):
        """
        Genera el gráfico de residuos del modelo.

        Compatible con cualquier modelo
        de regresión bivariada.
        """

        if self.modelo is None:

            raise ValueError(
                "Primero debe construir el modelo."
            )

        #-------------------------------------------------
        # Valores reales y predichos
        #-------------------------------------------------

        y_real = self.y_test

        y_pred = self.f_predict_regresiones(self.X_test)

        residuos = y_real - y_pred


        #-------------------------------------------------
        # Prueba de Breusch-Pagan
        #-------------------------------------------------

        X_bp = add_constant(
            self.X_test
        )

        LM, LM_pvalor, F, F_pvalor = het_breuschpagan(

            residuos,

            X_bp

        )

        LM = float(round(LM,4))

        LM_pvalor = float(round(LM_pvalor,4))

        F = float(round(F,4))

        F_pvalor = float(round(F_pvalor,4))


        #-------------------------------------------------
        # Figura
        #-------------------------------------------------

        fig, ax = plt.subplots(

            figsize=figsize

        )


        #-------------------------------------------------
        # Residuos
        #-------------------------------------------------

        ax.scatter(

            y_pred,

            residuos,

            s=18,

            alpha=0.55,

            color="steelblue"

        )


        #-------------------------------------------------
        # Línea horizontal en cero
        #-------------------------------------------------

        ax.axhline(

            y=0,

            color="red",

            linestyle="--",

            linewidth=2

        )


        #-------------------------------------------------
        # Título
        #-------------------------------------------------

        ax.set_title(

            titulo,

            fontsize=18,

            fontweight="bold"

        )


        #-------------------------------------------------
        # Etiquetas
        #-------------------------------------------------

        ax.set_xlabel(

            "Valores predichos",

            fontsize=14,

            fontweight="bold"

        )

        ax.set_ylabel(

            "Residuos",

            fontsize=14,

            fontweight="bold"

        )


        #-------------------------------------------------
        # Cuadrícula
        #-------------------------------------------------

        if mostrar_grid:

            ax.grid(

                linestyle="--",

                alpha=0.35

            )


        #-------------------------------------------------
        # Caja de información
        #-------------------------------------------------

        texto = (

            "Breusch-Pagan\n\n"

            f"LM = {LM}\n"

            f"p = {LM_pvalor}"

        )


        ax.text(

            0.72,

            0.94,

            texto,

            transform=ax.transAxes,

            fontsize=11,

            verticalalignment="top",

            bbox=dict(

                facecolor="white",

                edgecolor="black",

                alpha=0.95,

                boxstyle="round,pad=0.6"

            )

        )


        #-------------------------------------------------
        # Pie de figura
        #-------------------------------------------------

        ax.text(

            0.50,

            -0.12,

            "Los residuos deberían distribuirse aleatoriamente alrededor de cero.",

            transform=ax.transAxes,

            ha="center",

            fontsize=10

        )


        plt.tight_layout()


        #-------------------------------------------------
        # Resultado
        #-------------------------------------------------

        return {

            "figura": fig,

            "LM": LM,

            "LM_pvalor": LM_pvalor,

            "F": F,

            "F_pvalor": F_pvalor

        }
    
    #=====================================================
    # QQPLOT DE LOS RESIDUOS
    #=====================================================

    def f_generar_QQPlot(
            self,
            titulo="QQPlot de los Residuos",
            mostrar_grid=True,
            figsize=(8,6)):
        """
        Genera el QQPlot de los residuos del modelo.

        Compatible con cualquier modelo
        de regresión bivariada.
        """

        if self.modelo is None:

            raise ValueError(
                "Primero debe construir el modelo."
            )


        #-------------------------------------------------
        # Valores reales y predichos
        #-------------------------------------------------

        y_real = self.y_test

        y_pred = self.predicciones["validacion"]

        #-------------------------------------------------
        # Residuos
        #-------------------------------------------------

        residuos = y_real - y_pred


        #-------------------------------------------------
        # Prueba Shapiro-Wilk
        #-------------------------------------------------

        W, p_valor = stats.shapiro(

            residuos

        )


        #-------------------------------------------------
        # Figura
        #-------------------------------------------------

        fig, ax = plt.subplots(

            figsize=figsize

        )


        #-------------------------------------------------
        # QQPlot
        #-------------------------------------------------

        stats.probplot(

            residuos,

            dist="norm",

            plot=ax

        )


        #-------------------------------------------------
        # Personalizar puntos y línea
        #-------------------------------------------------

        if len(ax.get_lines()) >= 2:

            # Puntos

            ax.get_lines()[0].set_marker("o")

            ax.get_lines()[0].set_markersize(5)

            ax.get_lines()[0].set_markerfacecolor("steelblue")

            ax.get_lines()[0].set_markeredgecolor("steelblue")

            ax.get_lines()[0].set_linestyle("")


            # Línea de referencia

            ax.get_lines()[1].set_color("red")

            ax.get_lines()[1].set_linewidth(2)


        #-------------------------------------------------
        # Título
        #-------------------------------------------------

        ax.set_title(

            titulo,

            fontsize=18,

            fontweight="bold"

        )


        #-------------------------------------------------
        # Etiquetas
        #-------------------------------------------------

        ax.set_xlabel(

            "Cuantiles Teóricos",

            fontsize=14,

            fontweight="bold"

        )

        ax.set_ylabel(

            "Cuantiles Observados",

            fontsize=14,

            fontweight="bold"

        )


        #-------------------------------------------------
        # Cuadrícula
        #-------------------------------------------------

        if mostrar_grid:

            ax.grid(

                linestyle="--",

                alpha=0.35

            )


        #-------------------------------------------------
        # Caja de información
        #-------------------------------------------------

        texto = (

            f"Shapiro-Wilk\n\n"

            f"W = {W:.4f}\n"

            f"p = {p_valor:.4f}"

        )


        ax.text(

            0.70,

            0.95,

            texto,

            transform=ax.transAxes,

            fontsize=11,

            verticalalignment="top",

            bbox=dict(

                facecolor="white",

                edgecolor="black",

                alpha=0.95,

                boxstyle="round,pad=0.6"

            )

        )


        #-------------------------------------------------
        # Pie de figura
        #-------------------------------------------------

        ax.text(

            0.50,

            -0.12,

            "Los puntos deberían aproximarse a la línea de referencia.",

            transform=ax.transAxes,

            ha="center",

            fontsize=10

        )


        #-------------------------------------------------
        # Ajuste final
        #-------------------------------------------------

        plt.tight_layout()

        return {

            "figura": fig,

            "W": float(round(W,4)),

            "p_valor": float(round(p_valor,4))

        }


    #=====================================================
    # INDEPENDENCIA DE LOS RESIDUOS
    #=====================================================

    def f_independencia_residuos(self):
        """
        Calcula el estadístico de Durbin-Watson
        para verificar la independencia
        de los residuos.

        Compatible con cualquier modelo
        de regresión bivariada.
        """

        if self.modelo is None:

            raise ValueError(
                "Primero debe construir el modelo."
            )

        #-----------------------------------------
        # Valores reales y predichos
        #-----------------------------------------

        y_real = self.y_test

        y_pred = self.f_predict_regresiones(

            self.X_test

        )

        #-----------------------------------------
        # Residuos
        #-----------------------------------------

        residuos = y_real - y_pred

        #-----------------------------------------
        # Durbin-Watson
        #-----------------------------------------

        DW = float(

            round(

                durbin_watson(

                    residuos

                ),

                4

            )

        )

        #-----------------------------------------
        # Resultado
        #-----------------------------------------

        return {

            "Durbin_Watson": DW

        }

    #=====================================================
    # PREDICCIÓN INTERNA
    #=====================================================

    def f_predict_regresiones(self, X):
        """
        Realiza predicciones considerando
        automáticamente el tipo de modelo de regresión
        """

        if self.tipo.lower() == "lineal":

            return self.modelo.predict(X)

        elif self.tipo.lower() == "polinomial":

            X_poly = self.transformador.transform(X)

            return self.modelo.predict(X_poly)
        elif self.tipo.lower() == "exponencial":

            y_log = self.modelo.predict(X)

            return np.exp(y_log)
        elif self.tipo.lower() == "logarítmica":

            if np.any(X <= 0):

                raise ValueError(
                    "La regresión logarítmica requiere X > 0."
                )

            X_log = np.log(X)

            return self.modelo.predict(X_log)
        elif self.tipo.lower() == "potencial":

            if np.any(X <= 0):

                raise ValueError(
                    "La regresión potencial requiere X > 0."
                )

            X_log = np.log(X)

            y_log = self.modelo.predict(

                X_log

            )

            return np.exp(y_log)

        else:

            raise ValueError(
                f"Modelo '{self.tipo}' no soportado."
            )