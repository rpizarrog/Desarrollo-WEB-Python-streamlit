"""
=========================================================
ARCHIVO
CInterpretador.py

AUTOR
Rubén Pizarro Gurrola

FECHA
Agosto 2026

DESCRIPCIÓN

La clase Interpretador genera una interpretación
automática de los estadísticos descriptivos mediante
reglas de inferencia.

No utiliza Inteligencia Artificial.

Las reglas implementadas están basadas en conceptos
estadísticos utilizados en cursos de nivel superior.

La interpretación generada servirá posteriormente para:

• Compararse contra la IA.
• Compararse contra el estudiante.
• Evaluar similitud semántica.
=========================================================
"""


#=========================================================
# CLASE
#=========================================================

class Interpretador:

    """
    Motor de inferencia basado en reglas.
    """

    #=====================================================
    # CONSTRUCTOR
    #=====================================================

    def __init__(self):

        pass


    #=====================================================
    # GENERAR INTERPRETACIÓN
    #=====================================================

    def f_generar_interpretacion(
            self,
            est):
        """
        Genera una interpretación completa.
        """

        texto = ""

        texto += self.f_interpretar_variable(est)

        texto += self.f_interpretar_tendencia_central(est)

        texto += self.f_interpretar_dispersion(est)

        texto += self.f_interpretar_rango(est)

        texto += self.f_interpretar_cuartiles(est)

        texto += self.f_interpretar_atipicos(est)

        texto += self.f_interpretar_asimetria(est)

        texto += self.f_interpretar_curtosis(est)

        texto += self.f_interpretar_normalidad(est)

        texto += self.f_generar_conclusion(est)

        return texto


    #=====================================================
    # VARIABLE
    #=====================================================

    def f_interpretar_variable(
            self,
            est):
        """
        Describe el contexto de la variable.
        """

        texto = ""

        texto += (
            f"Se analizaron "
            f"{est['n']} observaciones "
            f"correspondientes a la variable "
            f"'{est['variable']}'. "
        )

        if len(est["contexto"]) > 0:

            texto += (
                f"El contexto de estudio corresponde a "
                f"{est['contexto']}. "
            )

        texto += "\n\n"

        return texto


    #=====================================================
    # TENDENCIA CENTRAL
    #=====================================================

    def f_interpretar_tendencia_central(
            self,
            est):
        """
        Interpreta media, mediana y moda.
        """

        media = est["media"]

        mediana = est["mediana"]

        moda = est["moda"]

        texto = ""

        texto += (
            "Las medidas de tendencia central indican "
            f"que la media es de {media:.2f}, "
            f"la mediana es de {mediana:.2f}"
        )

        if len(moda) == 1:

            texto += (
                f" y la moda corresponde a "
                f"{moda[0]:.2f}. "
            )

        else:

            texto += (
                ", observándose múltiples modas, "
                "por lo que la distribución es "
                "multimodal. "
            )

        diferencia = abs(
            media - mediana
        )

        if diferencia < 0.10:

            texto += (
                "La media y la mediana son "
                "prácticamente iguales, lo que "
                "sugiere una distribución bastante "
                "simétrica. "
            )

        elif diferencia < 1:

            texto += (
                "La media y la mediana presentan "
                "valores cercanos, indicando una "
                "distribución con poca asimetría. "
            )

        else:

            texto += (
                "Existe una diferencia apreciable "
                "entre la media y la mediana, "
                "lo que podría indicar cierta "
                "asimetría en la distribución. "
            )

        texto += "\n\n"

        return texto

    #=====================================================
    # DISPERSIÓN
    #=====================================================

    def f_interpretar_dispersion(
            self,
            est):
        """
        Interpreta la dispersión de los datos.
        """

        texto = ""

        texto += (
            f"La desviación estándar es de "
            f"{est['desviacion']:.2f}, "
            f"mientras que el coeficiente de variación "
            f"es de {est['cv']:.2%}. "
        )

        cv = est["cv"]

        if cv < 0.10:

            texto += (
                "El coeficiente de variación indica una "
                "dispersión baja, por lo que los datos "
                "presentan una elevada homogeneidad y se "
                "encuentran concentrados alrededor de la media. "
            )

        elif cv < 0.20:

            texto += (
                "El coeficiente de variación sugiere una "
                "dispersión moderada. Los datos presentan "
                "cierta variabilidad, aunque continúan "
                "mostrando un comportamiento relativamente "
                "homogéneo. "
            )

        elif cv < 0.30:

            texto += (
                "La dispersión es considerable. "
                "Los valores muestran diferencias "
                "importantes respecto a la media. "
            )

        else:

            texto += (
                "El coeficiente de variación es elevado, "
                "lo que indica una alta heterogeneidad y una "
                "gran dispersión de los datos. "
            )

        texto += "\n\n"

        return texto


    #=====================================================
    # RANGO
    #=====================================================

    def f_interpretar_rango(
            self,
            est):
        """
        Interpreta el rango de los datos.
        """

        texto = ""

        texto += (
            f"Los valores observados oscilan entre "
            f"{est['minimo']:.2f} y "
            f"{est['maximo']:.2f}, "
            f"obteniéndose un rango de "
            f"{est['rango']:.2f}. "
        )

        texto += (
            "El rango representa la amplitud total de los "
            "datos y permite apreciar la diferencia existente "
            "entre el menor y el mayor valor observado. "
        )

        texto += "\n\n"

        return texto


    #=====================================================
    # CUARTILES
    #=====================================================

    def f_interpretar_cuartiles(
            self,
            est):
        """
        Interpreta los cuartiles.
        """

        texto = ""

        texto += (
            f"El primer cuartil (Q1) es "
            f"{est['q1']:.2f}, "
            f"la mediana (Q2) es "
            f"{est['q2']:.2f} "
            f"y el tercer cuartil (Q3) es "
            f"{est['q3']:.2f}. "
        )

        texto += (
            f"El rango intercuartílico es de "
            f"{est['iqr']:.2f}, "
            "lo que representa la dispersión del 50 % central "
            "de los datos y proporciona una medida robusta de "
            "variabilidad al no verse afectada significativamente "
            "por valores extremos. "
        )

        texto += "\n\n"

        return texto


    #=====================================================
    # VALORES ATÍPICOS
    #=====================================================

    def f_interpretar_atipicos(
            self,
            est):
        """
        Interpreta la presencia de valores atípicos.
        """

        texto = ""

        if est["atipicos"]:

            texto += (
                f"Se identificaron "
                f"{est['numero_atipicos']} "
                "valor(es) atípico(s). "
            )

            texto += (
                "Los valores atípicos corresponden a "
            )

            texto += ", ".join(
                [
                    f"{x:.2f}"
                    for x in est["valores_atipicos"]
                ]
            )

            texto += ". "

            texto += (
                "Estos valores pueden influir sobre la media, "
                "la desviación estándar y otras medidas "
                "estadísticas, por lo que conviene revisar "
                "si corresponden a observaciones reales o "
                "a posibles errores de captura. "
            )

        else:

            texto += (
                "No se detectaron valores atípicos mediante "
                "el criterio del rango intercuartílico (IQR), "
                "lo que sugiere que las observaciones mantienen "
                "un comportamiento consistente dentro del conjunto "
                "de datos analizado. "
            )

        texto += "\n\n"

        return texto
    #=====================================================
    # ASIMETRÍA
    #=====================================================

    def f_interpretar_asimetria(
            self,
            est):
        """
        Interpreta el coeficiente de asimetría.
        """

        texto = ""

        asimetria = est["asimetria"]

        texto += (
            f"El coeficiente de asimetría es "
            f"{asimetria:.3f}. "
        )

        if abs(asimetria) < 0.20:

            texto += (
                "Este valor es muy cercano a cero, por lo que "
                "la distribución puede considerarse aproximadamente "
                "simétrica. No existe una preferencia evidente "
                "hacia valores altos o bajos. "
            )

        elif asimetria > 0:

            texto += (
                "La distribución presenta una asimetría positiva, "
                "lo que indica una ligera tendencia a concentrar "
                "los datos hacia valores bajos, con una cola que "
                "se extiende hacia la derecha. "
            )

        else:

            texto += (
                "La distribución presenta una asimetría negativa, "
                "lo que indica una ligera tendencia a concentrar "
                "los datos hacia valores altos, con una cola que "
                "se extiende hacia la izquierda. "
            )

        texto += "\n\n"

        return texto


    #=====================================================
    # CURTOSIS
    #=====================================================

    def f_interpretar_curtosis(
            self,
            est):
        """
        Interpreta el coeficiente de curtosis.
        """

        texto = ""

        curtosis = est["curtosis"]

        texto += (
            f"El coeficiente de curtosis es "
            f"{curtosis:.3f}. "
        )

        if abs(curtosis) < 0.20:

            texto += (
                "La distribución presenta un comportamiento "
                "muy similar al de una distribución normal "
                "en cuanto a concentración de datos alrededor "
                "de la media. "
            )

        elif curtosis > 0:

            texto += (
                "La distribución es leptocúrtica, "
                "caracterizada por una mayor concentración "
                "de observaciones alrededor de la media y "
                "colas relativamente más largas que una "
                "distribución normal. "
            )

        else:

            texto += (
                "La distribución es platicúrtica, "
                "presentando una menor concentración "
                "de observaciones alrededor de la media "
                "y colas relativamente más cortas que "
                "una distribución normal. "
            )

        texto += "\n\n"

        return texto


    #=====================================================
    # NORMALIDAD
    #=====================================================

    def f_interpretar_normalidad(
            self,
            est):
        """
        Interpreta la prueba de Shapiro-Wilk.
        """

        texto = ""

        texto += (
            f"La prueba de normalidad "
            f"{est['prueba']} "
            f"produjo un valor p de "
            f"{est['pvalor']:.4f}. "
        )

        if est["normal"]:

            texto += (
                "Considerando un nivel de significancia "
                "de 0.05, no existen evidencias suficientes "
                "para rechazar la hipótesis de normalidad. "
                "Por lo tanto, los datos son consistentes "
                "con una distribución aproximadamente normal. "
            )

        else:

            texto += (
                "Considerando un nivel de significancia "
                "de 0.05, existen evidencias suficientes "
                "para rechazar la hipótesis de normalidad. "
                "En consecuencia, los datos no presentan "
                "un comportamiento consistente con una "
                "distribución normal. "
            )

        texto += "\n\n"

        return texto


    #=====================================================
    # CONCLUSIÓN
    #=====================================================

    def f_generar_conclusion(
            self,
            est):
        """
        Genera una conclusión general.
        """

        texto = ""

        texto += "En conclusión, "

        if est["normal"]:

            texto += (
                "la variable analizada presenta un comportamiento "
                "estadístico adecuado para describirse mediante "
                "las medidas de tendencia central y dispersión "
                "calculadas. La ausencia o baja presencia de "
                "asimetría, junto con los resultados de la prueba "
                "de normalidad, sugieren que los datos representan "
                "una distribución aproximadamente normal. "
            )

        else:

            texto += (
                "aunque las medidas descriptivas permiten resumir "
                "adecuadamente la información, la prueba de "
                "normalidad indica que la distribución no sigue "
                "un comportamiento normal. Por ello, la interpretación "
                "de los resultados debe considerar esta característica, "
                "especialmente si posteriormente se desea aplicar "
                "métodos estadísticos paramétricos. "
            )

        if est["atipicos"]:

            texto += (
                "Se detectaron valores atípicos que podrían influir sobre la media, "
                "la desviación estándar y otras medidas descriptivas, "
                "por lo que conviene revisar si corresponden a observaciones "
                "reales o a posibles errores de captura. "
            )

        else:

            texto += (
                "No se detectaron valores atípicos mediante el criterio del rango intercuartílico (IQR), "
                "lo que sugiere que las observaciones mantienen "
                "un comportamiento consistente dentro del conjunto de datos analizado.. "
            )

        texto += "\n"

        return texto
