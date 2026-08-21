"""
=========================================================
ARCHIVO
CInterpretador.py

AUTOR
Rubén Pizarro Gurrola

FECHA
Agosto 2026

DESCRIPCIÓN

Clase que interrpeta modelos de
Regresión Bivariada. Tanto por Experto como por IA

Versión 1.0

Parte A

Interpretación.

=========================================================
"""

import numpy as np

class Interpretador:

    def __init__(self):

        pass

    #=====================================================
    # GENERAR INTERPRETACIÓN
    #=====================================================
    def f_generar_interpretacion(
            self,
            regresion):

        texto = ""

        texto += self.f_modelo(regresion)

        texto += self.f_ecuacion(regresion)

        texto += self.f_coeficientes(regresion)

        texto += self.f_r2(regresion)

        texto += self.f_metricas(regresion)

        texto += self.f_supuestos(regresion)

        texto += self.f_conclusion(regresion)

        return texto            

    #=====================================================
    # INTERPRETACIÓN DEL MODELO
    #=====================================================

    def f_modelo(
            self,
            regresion):
        """
        Interpreta el tipo de modelo de
        regresión construido.
        """

        texto = ""

        texto += "MODELO CONSTRUIDO\n"
        texto += "==============================\n\n"

        texto += (
            f"Se construyó un modelo de regresión "
            f"{regresion.tipo.lower()}"
        )

        if regresion.tipo.lower() == "polinomial":

            texto += (
                f" de grado {regresion.grado}"
            )

        texto += (
            " para estudiar la relación entre la variable "
            f"independiente '{regresion.variable_x}' y la "
            f"variable dependiente '{regresion.variable_y}'.\n\n"
        )

        #---------------------------------------------
        # Interpretación según el tipo de modelo
        #---------------------------------------------

        tipo = regresion.tipo.lower()

        if tipo == "lineal":

            texto += (
                "Este modelo supone que la relación entre ambas "
                "variables puede representarse mediante una línea "
                "recta, por lo que el cambio esperado en la variable "
                "dependiente es aproximadamente constante por cada "
                "unidad de incremento en la variable independiente.\n\n"
            )

        elif tipo == "polinomial":

            texto += (
                "El modelo polinomial permite representar relaciones "
                "curvilíneas entre las variables. Al incorporar "
                f"términos hasta el grado {regresion.grado}, puede "
                "describir cambios de tendencia, máximos, mínimos o "
                "curvaturas que un modelo lineal no sería capaz de "
                "representar adecuadamente.\n\n"
            )

        elif tipo == "exponencial":

            texto += (
                "El modelo exponencial describe procesos en los que "
                "la variable dependiente presenta un crecimiento o "
                "decrecimiento acelerado. Es apropiado cuando la tasa "
                "de cambio depende del valor actual de la variable.\n\n"
            )

        elif tipo == "logarítmica":

            texto += (
                "El modelo logarítmico representa relaciones en las "
                "que la variable dependiente cambia rápidamente para "
                "valores pequeños de la variable independiente y "
                "posteriormente dicho cambio se vuelve cada vez más "
                "lento.\n\n"
            )

        elif tipo == "potencial":

            texto += (
                "El modelo potencial representa relaciones de la forma "
                "Y = aXᵇ, ampliamente utilizadas para describir "
                "fenómenos biológicos, físicos y económicos donde la "
                "respuesta varía proporcionalmente a una potencia de "
                "la variable independiente.\n\n"
            )

        #---------------------------------------------
        # Información de entrenamiento
        #---------------------------------------------

        texto += (
            f"Para construir el modelo se utilizó el "
            f"{regresion.entrenamiento}% de los datos "
            "como conjunto de entrenamiento y el "
            f"{regresion.validacion}% restante para "
            "la validación del desempeño predictivo.\n\n"
        )

        return texto

    #=====================================================
    # ECUACIÓN
    #=====================================================

    # Interpretar ecuación
    #=====================================================
    # INTERPRETACIÓN DE LA ECUACIÓN
    #=====================================================

    def f_ecuacion(
            self,
            regresion):
        """
        Interpreta la ecuación matemática
        del modelo de regresión.
        """

        ecuacion = regresion.f_ecuacion()

        texto = ""

        texto += "ECUACIÓN DEL MODELO\n"
        texto += "==============================\n\n"

        texto += (
            "La relación matemática estimada entre las "
            "variables se representa mediante la siguiente "
            "ecuación:\n\n"
        )

        texto += f"{ecuacion['ecuacion']}\n\n"

        tipo = regresion.tipo.lower()

        #---------------------------------------------
        # Interpretación
        #---------------------------------------------

        if tipo == "lineal":

            texto += (
                "La ecuación representa una relación lineal entre "
                "las variables, donde el efecto de la variable "
                "independiente sobre la variable dependiente se "
                "mantiene aproximadamente constante a lo largo "
                "del rango de observación.\n\n"
            )

        elif tipo == "polinomial":

            texto += (
                "La ecuación incorpora términos polinomiales que "
                "permiten representar curvaturas y cambios en la "
                "tendencia de los datos. Esto proporciona una "
                "mayor flexibilidad para describir relaciones "
                "no lineales.\n\n"
            )

        elif tipo == "exponencial":

            texto += (
                "La ecuación describe un comportamiento exponencial, "
                "por lo que pequeños cambios en la variable "
                "independiente pueden producir incrementos o "
                "decrementos acelerados en la variable dependiente.\n\n"
            )

        elif tipo == "logarítmica":

            texto += (
                "La ecuación representa una relación logarítmica, "
                "caracterizada por cambios rápidos al inicio y una "
                "disminución gradual de la tasa de crecimiento a "
                "medida que aumenta la variable independiente.\n\n"
            )

        elif tipo == "potencial":

            texto += (
                "La ecuación corresponde a una función potencial, "
                "utilizada para representar fenómenos donde la "
                "respuesta cambia proporcionalmente a una potencia "
                "de la variable independiente.\n\n"
            )

        return texto
    #=====================================================
    # COEFICIENTES
    #=====================================================

    # Interpretar coeficientes
    #=====================================================
    # INTERPRETACIÓN DE LOS COEFICIENTES
    #=====================================================

    def f_coeficientes(
            self,
            regresion):
        """
        Interpreta los coeficientes del
        modelo de regresión.
        """

        coef = regresion.f_coeficientes()

        texto = ""

        texto += "INTERPRETACIÓN DE LOS COEFICIENTES\n"
        texto += "==============================\n\n"

        tipo = regresion.tipo.lower()

        #---------------------------------------------
        # LINEAL
        #---------------------------------------------

        if tipo == "lineal":

            b0 = coef["intercepto"]
            b1 = coef["b1"]

            texto += (
                f"El intercepto ({b0:.4f}) representa el valor "
                "esperado de la variable dependiente cuando la "
                "variable independiente toma el valor cero. "
                "Dependiendo del contexto del problema, este "
                "valor puede o no tener interpretación práctica.\n\n"
            )

            if b1 > 0:

                texto += (
                    f"La pendiente ({b1:.4f}) es positiva, lo que "
                    "indica una relación directa entre las variables. "
                    "En promedio, por cada unidad adicional de la "
                    "variable independiente, la variable dependiente "
                    f"aumenta aproximadamente {abs(b1):.4f} unidades.\n\n"
                )

            elif b1 < 0:

                texto += (
                    f"La pendiente ({b1:.4f}) es negativa, lo que "
                    "indica una relación inversa entre las variables. "
                    "En promedio, por cada unidad adicional de la "
                    "variable independiente, la variable dependiente "
                    f"disminuye aproximadamente {abs(b1):.4f} unidades.\n\n"
                )

            else:

                texto += (
                    "La pendiente es prácticamente nula, por lo que "
                    "no se observa una relación lineal apreciable "
                    "entre las variables.\n\n"
                )

        #---------------------------------------------
        # POLINOMIAL
        #---------------------------------------------

        elif tipo == "polinomial":

            texto += (
                "Los coeficientes polinomiales determinan la forma "
                "y curvatura de la función ajustada. La combinación "
                "de estos parámetros permite representar cambios de "
                "tendencia, máximos, mínimos y puntos de inflexión "
                "que no pueden describirse mediante un modelo lineal.\n\n"
            )

        #---------------------------------------------
        # EXPONENCIAL
        #---------------------------------------------

        elif tipo == "exponencial":

            b = coef["b1"]

            if b > 0:

                texto += (
                    "El coeficiente exponencial positivo indica un "
                    "crecimiento acelerado de la variable dependiente "
                    "conforme aumenta la variable independiente.\n\n"
                )

            else:

                texto += (
                    "El coeficiente exponencial negativo indica un "
                    "decrecimiento exponencial de la variable "
                    "dependiente conforme aumenta la variable "
                    "independiente.\n\n"
                )

        #---------------------------------------------
        # LOGARÍTMICA
        #---------------------------------------------

        elif tipo == "logarítmica":

            b = coef["b1"]

            if b > 0:

                texto += (
                    "El coeficiente positivo indica que la variable "
                    "dependiente aumenta rápidamente para valores "
                    "pequeños de la variable independiente y luego "
                    "el crecimiento se desacelera.\n\n"
                )

            else:

                texto += (
                    "El coeficiente negativo indica una disminución "
                    "rápida al inicio que posteriormente tiende a "
                    "estabilizarse.\n\n"
                )

        #---------------------------------------------
        # POTENCIAL
        #---------------------------------------------

        elif tipo == "potencial":

            b = coef["b1"]

            texto += (
                f"El exponente estimado ({b:.4f}) determina la "
                "forma en que la variable dependiente responde a "
                "cambios en la variable independiente.\n\n"
            )

            if b > 1:

                texto += (
                    "Un exponente mayor que uno indica que la "
                    "respuesta crece más rápidamente que la propia "
                    "variable independiente.\n\n"
                )

            elif 0 < b < 1:

                texto += (
                    "Un exponente comprendido entre cero y uno "
                    "indica un crecimiento cada vez más lento "
                    "conforme aumenta la variable independiente.\n\n"
                )

            elif b < 0:

                texto += (
                    "Un exponente negativo indica una relación "
                    "inversa entre ambas variables.\n\n"
                )

        return texto

    
    # Interprtar r2
    #=====================================================
    # INTERPRETACIÓN DEL R²
    #=====================================================

    def f_r2(
            self,
            regresion):
        """
        Interpreta el coeficiente de determinación
        y el coeficiente de determinación ajustado.
        """

        r2 = regresion.metricas["R2"]
        r2a = regresion.metricas["R2_Ajustado"]

        texto = ""

        texto += "CALIDAD DEL AJUSTE DEL MODELO\n"
        texto += "==============================\n\n"

        texto += (
            f"El coeficiente de determinación obtenido "
            f"(R² = {r2:.4f}) indica que aproximadamente "
            f"el {r2*100:.2f}% de la variabilidad observada "
            f"en la variable dependiente puede ser explicada "
            f"por el modelo de regresión.\n\n"
        )

        #-----------------------------------------
        # Interpretación de R²
        #-----------------------------------------

        if r2 < 0.30:

            texto += (
                "El nivel de explicación del modelo es muy bajo. "
                "La variable independiente explica únicamente una "
                "pequeña parte del comportamiento de la variable "
                "dependiente, por lo que el ajuste no puede "
                "considerarse satisfactorio.\n\n"
            )

        elif r2 < 0.50:

            texto += (
                "El modelo presenta un nivel de explicación bajo. "
                "Aunque existe cierta relación entre las variables, "
                "una proporción importante de la variabilidad aún "
                "permanece sin explicar.\n\n"
            )

        elif r2 < 0.70:

            texto += (
                "El modelo presenta un ajuste moderado. "
                "Explica una parte importante de la variabilidad "
                "observada, aunque todavía existe margen para "
                "mejorar su capacidad explicativa.\n\n"
            )

        elif r2 < 0.90:

            texto += (
                "El modelo presenta un buen nivel de ajuste. "
                "La mayor parte de la variabilidad observada es "
                "explicada por la relación estimada entre las "
                "variables.\n\n"
            )

        else:

            texto += (
                "El modelo presenta un ajuste excelente. "
                "Prácticamente toda la variabilidad observada en "
                "la variable dependiente es explicada por el "
                "modelo construido.\n\n"
            )

        #-----------------------------------------
        # R² Ajustado
        #-----------------------------------------

        texto += (
            f"El coeficiente de determinación ajustado "
            f"(R² Ajustado = {r2a:.4f}) considera el número "
            "de parámetros utilizados por el modelo y permite "
            "evaluar si la complejidad incorporada se encuentra "
            "justificada.\n\n"
        )

        diferencia = abs(r2 - r2a)

        if diferencia < 0.02:

            texto += (
                "La diferencia entre R² y R² Ajustado es muy "
                "pequeña, lo que sugiere que la complejidad del "
                "modelo es adecuada y no existe evidencia de "
                "sobreajuste.\n\n"
            )

        elif diferencia < 0.05:

            texto += (
                "La diferencia entre ambos coeficientes es "
                "moderada. Aunque el modelo mantiene un buen "
                "desempeño, conviene interpretar los resultados "
                "considerando su nivel de complejidad.\n\n"
            )

        else:

            texto += (
                "Existe una diferencia importante entre R² y "
                "R² Ajustado. Esto puede indicar que el modelo "
                "es más complejo de lo necesario o que incorpora "
                "parámetros con escasa contribución al ajuste.\n\n"
            )

        return texto
    
    #=====================================================
    # INTERPRETACIÓN DE LAS MÉTRICAS
    #=====================================================

    def f_metricas(
            self,
            regresion):
        """
        Interpreta las principales métricas
        de evaluación del modelo.
        """

        m = regresion.metricas

        texto = ""

        texto += "EVALUACIÓN DEL MODELO\n"
        texto += "==============================\n\n"

        #-------------------------------------------------
        # MSE
        #-------------------------------------------------

        texto += (
            f"El Error Cuadrático Medio (MSE = {m['MSE']:.4f}) "
            "representa el promedio de los errores al cuadrado "
            "entre los valores observados y los valores "
            "predichos por el modelo. Valores pequeños indican "
            "una mejor capacidad de ajuste.\n\n"
        )

        #-------------------------------------------------
        # RMSE
        #-------------------------------------------------

        texto += (
            f"El Error Cuadrático Medio Raíz (RMSE = {m['RMSE']:.4f}) "
            "expresa el error promedio de predicción en las mismas "
            "unidades de la variable dependiente.\n\n"
        )

        #-------------------------------------------------
        # MAE
        #-------------------------------------------------

        texto += (
            f"El Error Absoluto Medio (MAE = {m['MAE']:.4f}) "
            "indica que, en promedio, las predicciones difieren "
            f"aproximadamente {m['MAE']:.4f} unidades respecto a "
            "los valores observados.\n\n"
        )

        #-------------------------------------------------
        # MAPE
        #-------------------------------------------------

        if np.isnan(m["MAPE"]):

            texto += (
                "No fue posible calcular el Error Porcentual "
                "Absoluto Medio (MAPE), debido a que existen "
                "valores iguales a cero en la variable dependiente.\n\n"
            )

        else:

            texto += (
                f"El Error Porcentual Absoluto Medio "
                f"(MAPE = {m['MAPE']:.2f}%) "
                "representa el error relativo promedio del modelo.\n\n"
            )

            if m["MAPE"] < 10:

                texto += (
                    "El porcentaje de error puede considerarse "
                    "excelente para fines predictivos.\n\n"
                )

            elif m["MAPE"] < 20:

                texto += (
                    "El porcentaje de error es bajo, indicando "
                    "una buena capacidad predictiva del modelo.\n\n"
                )

            elif m["MAPE"] < 50:

                texto += (
                    "El porcentaje de error es moderado. El modelo "
                    "puede utilizarse para predicciones, aunque con "
                    "cierta precaución.\n\n"
                )

            else:

                texto += (
                    "El porcentaje de error es elevado, lo que "
                    "indica que las predicciones presentan una "
                    "precisión limitada. Se recomienda evaluar "
                    "otros modelos de regresión.\n\n"
                )

        #-------------------------------------------------
        # AIC
        #-------------------------------------------------

        texto += (
            f"El Criterio de Información de Akaike "
            f"(AIC = {m['AIC']:.4f}) permite comparar este "
            "modelo con otros candidatos. Entre varios modelos, "
            "generalmente se prefiere aquel que presente el "
            "menor valor de AIC.\n\n"
        )

        #-------------------------------------------------
        # BIC
        #-------------------------------------------------

        texto += (
            f"El Criterio de Información Bayesiano "
            f"(BIC = {m['BIC']:.4f}) también se emplea para "
            "comparar modelos alternativos, penalizando en mayor "
            "medida la complejidad del modelo. Valores menores "
            "indican un mejor equilibrio entre ajuste y número "
            "de parámetros.\n\n"
        )

        #-------------------------------------------------
        # Dictamen general
        #-------------------------------------------------

        texto += (
            "En conjunto, estas métricas permiten evaluar la "
            "capacidad predictiva del modelo y comparar su "
            "desempeño con otras alternativas de regresión. "
            "La selección del modelo más adecuado debe considerar "
            "simultáneamente la calidad del ajuste, el tamaño de "
            "los errores de predicción y la complejidad del modelo.\n"
        )

        return texto
    
    #=====================================================
    # INTERPRETACIÓN DE LOS SUPUESTOS
    #=====================================================

    def f_supuestos(
            self,
            regresion):
        """
        Interpreta los principales supuestos
        del modelo de regresión.
        """

        texto = ""

        texto += "DIAGNÓSTICO DE LOS SUPUESTOS\n"
        texto += "==============================\n\n"

        cumplidos = 0
        total = 4

        #-------------------------------------------------
        # LINEALIDAD (RAMSEY RESET)
        #-------------------------------------------------

        linealidad = regresion.f_verificar_linealidad()

        texto += "1. Forma funcional del modelo\n"

        texto += (
            f"Prueba Ramsey RESET: "
            f"F = {linealidad['F']:.4f}, "
            f"p = {linealidad['p_valor']:.4f}\n"
        )

        if linealidad["p_valor"] > 0.05:

            cumplidos += 1

            texto += (
                "No existe evidencia estadísticamente "
                "significativa de una especificación "
                "incorrecta del modelo. La forma "
                "funcional seleccionada representa "
                "adecuadamente la relación entre las "
                "variables.\n\n"
            )

        else:

            texto += (
                "La prueba Ramsey RESET detectó evidencia "
                "de una posible especificación incorrecta "
                "del modelo. Se recomienda evaluar otras "
                "formas funcionales como modelos "
                "polinomiales, exponenciales o potenciales.\n\n"
            )

        #-------------------------------------------------
        # HOMOCEDASTICIDAD
        #-------------------------------------------------

        residuos = regresion.f_generar_residuos()

        texto += "2. Homocedasticidad\n"

        texto += (
            f"Breusch-Pagan: "
            f"LM = {residuos['LM']:.4f}, "
            f"p = {residuos['LM_pvalor']:.4f}\n"
        )

        if residuos["LM_pvalor"] > 0.05:

            cumplidos += 1

            texto += (
                "No existe evidencia de heterocedasticidad. "
                "La variabilidad de los residuos puede "
                "considerarse aproximadamente constante.\n\n"
            )

        else:

            texto += (
                "Existe evidencia de heterocedasticidad, "
                "lo que indica que la varianza de los "
                "errores no permanece constante a lo largo "
                "del rango de predicción.\n\n"
            )

        #-------------------------------------------------
        # NORMALIDAD
        #-------------------------------------------------

        normalidad = regresion.f_generar_QQPlot()

        texto += "3. Normalidad de los residuos\n"

        texto += (
            f"Shapiro-Wilk: "
            f"W = {normalidad['W']:.4f}, "
            f"p = {normalidad['p_valor']:.4f}\n"
        )

        if normalidad["p_valor"] > 0.05:

            cumplidos += 1

            texto += (
                "Los residuos presentan una distribución "
                "compatible con la normalidad, por lo que "
                "este supuesto puede considerarse satisfecho.\n\n"
            )

        else:

            texto += (
                "Los residuos muestran desviaciones "
                "estadísticamente significativas respecto "
                "a la distribución normal.\n\n"
            )

        #-------------------------------------------------
        # INDEPENDENCIA
        #-------------------------------------------------

        independencia = regresion.f_independencia_residuos()

        DW = independencia["Durbin_Watson"]

        texto += "4. Independencia de los residuos\n"

        texto += (
            f"Durbin-Watson = {DW:.4f}\n"
        )

        if 1.5 <= DW <= 2.5:

            cumplidos += 1

            texto += (
                "El estadístico Durbin-Watson se encuentra "
                "próximo a dos, lo que sugiere ausencia de "
                "autocorrelación significativa entre los "
                "residuos.\n\n"
            )

        elif DW < 1.5:

            texto += (
                "El estadístico Durbin-Watson indica una "
                "posible autocorrelación positiva entre "
                "los residuos.\n\n"
            )

        else:

            texto += (
                "El estadístico Durbin-Watson sugiere una "
                "posible autocorrelación negativa entre "
                "los residuos.\n\n"
            )

        #-------------------------------------------------
        # RESUMEN GENERAL
        #-------------------------------------------------

        texto += "DICTAMEN GENERAL\n"
        texto += "==============================\n\n"

        texto += (
            f"De los {total} supuestos evaluados, "
            f"el modelo cumple satisfactoriamente "
            f"{cumplidos}.\n\n"
        )

        if cumplidos == 4:

            texto += (
                "Todos los supuestos fundamentales de la "
                "regresión se encuentran satisfechos. "
                "Desde el punto de vista estadístico, el "
                "modelo puede considerarse adecuado para "
                "describir la relación entre las variables "
                "y realizar predicciones dentro del rango "
                "de datos analizado."
            )

        elif cumplidos == 3:

            texto += (
                "El modelo presenta un buen comportamiento "
                "general; sin embargo, uno de los supuestos "
                "no se cumple completamente. Se recomienda "
                "interpretar los resultados considerando "
                "esta limitación."
            )

        elif cumplidos == 2:

            texto += (
                "El modelo cumple únicamente una parte de "
                "los supuestos de regresión. Los resultados "
                "deben interpretarse con precaución y podría "
                "ser conveniente evaluar modelos alternativos."
            )

        else:

            texto += (
                "El modelo incumple la mayoría de los "
                "supuestos fundamentales de la regresión. "
                "No se recomienda utilizarlo para realizar "
                "inferencias o predicciones sin efectuar "
                "modificaciones al modelo."
            )

        return texto
    # Construir una conclusión

    #=====================================================
    # CONCLUSIÓN GENERAL
    #=====================================================

    def f_conclusion(
            self,
            regresion):
        """
        Genera la conclusión general del
        análisis del modelo de regresión.
        """

        r2 = regresion.metricas["R2"]
        rmse = regresion.metricas["RMSE"]
        mae = regresion.metricas["MAE"]
        mape = regresion.metricas["MAPE"]

        ramsey = regresion.f_verificar_linealidad()
        bp = regresion.f_generar_residuos()
        shapiro = regresion.f_generar_QQPlot()
        dw = regresion.f_independencia_residuos()

        texto = ""

        texto += "CONCLUSIÓN GENERAL\n"
        texto += "==============================\n\n"

        #---------------------------------------------
        # Calidad del ajuste
        #---------------------------------------------

        if r2 >= 0.90:

            texto += (
                "El modelo presenta un ajuste excelente, "
                "explicando la mayor parte de la variabilidad "
                "observada en la variable dependiente. "
            )

        elif r2 >= 0.70:

            texto += (
                "El modelo presenta un buen nivel de ajuste, "
                "explicando una proporción importante de la "
                "variabilidad observada. "
            )

        elif r2 >= 0.50:

            texto += (
                "El modelo presenta un ajuste moderado, por lo "
                "que describe parcialmente el comportamiento "
                "de los datos. "
            )

        else:

            texto += (
                "El modelo presenta un ajuste limitado, por lo "
                "que explica únicamente una parte reducida de "
                "la variabilidad observada. "
            )

        texto += "\n\n"

        #---------------------------------------------
        # Evaluación de supuestos
        #---------------------------------------------

        cumplidos = 0

        if ramsey["p_valor"] > 0.05:
            cumplidos += 1

        if bp["LM_pvalor"] > 0.05:
            cumplidos += 1

        if shapiro["p_valor"] > 0.05:
            cumplidos += 1

        if 1.5 <= dw["Durbin_Watson"] <= 2.5:
            cumplidos += 1

        texto += (
            f"Durante la evaluación estadística se verificó "
            f"el cumplimiento de {cumplidos} de los 4 "
            f"supuestos fundamentales del modelo de regresión. "
        )

        if cumplidos == 4:

            texto += (
                "Todos los supuestos fueron satisfechos, "
                "por lo que los resultados obtenidos pueden "
                "considerarse estadísticamente confiables.\n\n"
            )

        elif cumplidos == 3:

            texto += (
                "Aunque existe un supuesto que requiere "
                "atención, el comportamiento general del "
                "modelo puede considerarse adecuado.\n\n"
            )

        elif cumplidos == 2:

            texto += (
                "El incumplimiento de varios supuestos "
                "sugiere interpretar los resultados con "
                "precaución.\n\n"
            )

        else:

            texto += (
                "El modelo incumple la mayoría de los "
                "supuestos estadísticos, por lo que su "
                "uso para inferencia y predicción no es "
                "recomendable.\n\n"
            )

        #---------------------------------------------
        # Capacidad predictiva
        #---------------------------------------------

        texto += (
            f"El error promedio de predicción fue de "
            f"{mae:.4f} unidades (MAE) y un RMSE de "
            f"{rmse:.4f}."
        )

        if not np.isnan(mape):

            texto += (

                f" El error porcentual medio fue de "
                f"{mape:.2f}%."

            )

        texto += "\n\n"

        #---------------------------------------------
        # Recomendación
        #---------------------------------------------

        if r2 >= 0.70 and cumplidos >= 3:

            texto += (
                "En conjunto, el modelo puede considerarse "
                "adecuado para describir la relación entre "
                "las variables y realizar predicciones "
                "dentro del rango de datos analizado. "
                "No obstante, se recomienda evitar "
                "extrapolaciones fuera del intervalo de "
                "observación."
            )

        elif r2 >= 0.50:

            texto += (
                "El modelo resulta útil para describir la "
                "tendencia general de los datos; sin embargo, "
                "las predicciones deben interpretarse con "
                "cierta cautela debido a las limitaciones "
                "detectadas durante la evaluación."
            )

        else:

            texto += (
                "Se recomienda evaluar modelos alternativos "
                "como regresión polinomial, exponencial, "
                "logarítmica o potencial, con el propósito "
                "de obtener un mejor ajuste y una mayor "
                "capacidad predictiva."
            )

        return texto