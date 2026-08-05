"""
=========================================================
ARCHIVO
CReporte.py

CLASE
Reporte

AUTOR
Rubén Pizarro Gurrola

FECHA
Agosto 2026

DESCRIPCIÓN

Clase para visualizar reportes académicos generados por
las aplicaciones de Ciencia de Datos.

Versión 1.

Visualiza un reporte compuesto por:

• Objetivo
• Análisis descriptivo
• Interpretación

=========================================================
"""

#=========================================================
# LIBRERÍA
#=========================================================

import streamlit as st


#=========================================================
# CLASE
#=========================================================

class Reporte:


    #=====================================================
    # CONSTRUCTOR
    #=====================================================

    def __init__(self):

        pass


    #=====================================================
    # GENERAR OBJETIVO
    #=====================================================

    def f_generar_objetivo(
            self,
            estadisticos):
        """
        Genera el objetivo y el contexto del reporte.
        """

        variable = estadisticos.get(

            "variable",

            "Variable"

        )

        contexto = estadisticos.get(

            "contexto",

            ""

        )

        n = estadisticos.get(

            "n",

            0

        )

        objetivo = (

            f"Realizar un análisis descriptivo de la variable "

            f"\"{variable}\", utilizando una muestra de "

            f"{n} observaciones con el propósito de describir "

            f"su comportamiento mediante medidas de tendencia "

            f"central, dispersión, posición, forma y una "

            f"prueba de normalidad."

        )

        return {

            "objetivo": objetivo,

            "contexto": contexto

        }

    #=====================================================
    # GENERAR TABLA
    #=====================================================

    def f_generar_tabla(
            self,
            estadisticos):
        """
        Genera una tabla académica compacta
        de cuatro columnas.
        """

        #-------------------------------------------------
        # Etiquetas amigables
        #-------------------------------------------------

        etiquetas = {

            "n": "Observaciones",

            "media": "Media",

            "mediana": "Mediana",

            "moda": "Moda",

            "desviacion": "Desv. estándar",

            "varianza": "Varianza",

            "cv": "Coef. variación",

            "minimo": "Mínimo",

            "maximo": "Máximo",

            "q1": "Q1",

            "q3": "Q3",

            "rango": "Rango",

            "asimetria": "Asimetría",

            "curtosis": "Curtosis",

            "prueba": "Prueba",

            "pvalor": "Valor-p",

            "normal": "Normalidad",

            "numero_atipicos": "Núm. atípicos",

            "valores_atipicos": "Valores atípicos"

        }


        #-------------------------------------------------
        # Orden de aparición
        #-------------------------------------------------

        orden = [

            "n",

            "media",

            "mediana",

            "moda",

            "desviacion",

            "varianza",

            "cv",

            "minimo",

            "maximo",

            "q1",

            "q3",

            "rango",

            "asimetria",

            "curtosis",

            "prueba",

            "pvalor",

            "normal",

            "numero_atipicos",

            "valores_atipicos"

        ]


        #-------------------------------------------------
        # Formatear valores
        #-------------------------------------------------

        elementos = []

        for clave in orden:

            if clave not in estadisticos:

                continue

            valor = estadisticos[clave]


            #-------------------------
            # Booleanos
            #-------------------------

            if isinstance(valor, bool):

                valor = "Sí" if valor else "No"


            #-------------------------
            # Coeficiente variación
            #-------------------------

            elif clave == "cv":

                valor = f"{valor*100:.2f} %"


            #-------------------------
            # Moda
            #-------------------------

            elif clave == "moda":

                # Si ya viene como texto (ej. "Multimodal")
                if isinstance(valor, str):

                    pass

                # Si viene como lista
                elif isinstance(valor, list):

                    if len(valor) == 1:

                        valor = f"{float(valor[0]):.2f}"

                    elif len(valor) == 2:

                        valor = (

                            f"{float(valor[0]):.2f}, "

                            f"{float(valor[1]):.2f}"

                        )

                    else:

                        valor = "Multimodal"


            #-------------------------
            # Valores atípicos
            #-------------------------

            elif clave == "valores_atipicos":

                if isinstance(valor, list):

                    valor = ", ".join(

                        f"{float(v):.2f}"

                        for v in valor

                    )


            #-------------------------
            # Numéricos
            #-------------------------

            elif isinstance(valor, float):

                valor = f"{valor:.3f}"


            elementos.append(

                (

                    etiquetas[clave],

                    valor

                )

            )


        #-------------------------------------------------
        # Dividir en dos columnas
        #-------------------------------------------------

        mitad = (len(elementos)+1)//2

        izquierda = elementos[:mitad]

        derecha = elementos[mitad:]


        while len(derecha) < len(izquierda):

            derecha.append(

                ("","")

            )


        #-------------------------------------------------
        # Construir tabla
        #-------------------------------------------------

        lineas = []

        lineas.append("-"*84)

        lineas.append(

            f"{'Estadístico':<24}"

            f"{'Valor':>12}"

            f"    "

            f"{'Estadístico':<24}"

            f"{'Valor':>12}"

        )

        lineas.append("-"*84)


        for (e1,v1),(e2,v2) in zip(

                izquierda,

                derecha):

            lineas.append(

                f"{e1:<24}"

                f"{str(v1):>12}"

                f"    "

                f"{e2:<24}"

                f"{str(v2):>12}"

            )


        lineas.append("-"*84)

        return "\n".join(lineas)


    #=====================================================
    # VISUALIZAR GRÁFICAS
    #=====================================================

    def f_visualizar_graficas(
            self,
            graficas):
        """
        Visualiza las gráficas del reporte.
        """

        if not graficas:

            return

        st.header(

            "Representaciones gráficas"

        )

        columnas = st.columns(

            len(graficas)

        )

        for columna, grafica in zip(

                columnas,

                graficas):

            with columna:

                st.pyplot(

                    grafica["figura"],

                    use_container_width=True

                )

                st.caption(

                    grafica["nombre"]

                )

        st.divider()

    #=====================================================
    # VISUALIZAR REPORTE
    #=====================================================

    def f_visualizar_reporte(
            self,
            titulo,
            objetivo,
            estadisticos,
            interpretacion,
            graficas=None):
        """
        Visualiza un reporte académico.
        """

        st.title(titulo)

        st.divider()

        #-----------------------------------------
        # Objetivo
        #-----------------------------------------

        texto = self.f_generar_objetivo(

            estadisticos

        )

        st.header("Objetivo")

        st.markdown(

            texto["objetivo"]

        )

        st.divider()

        #-----------------------------------------
        # Contexto
        #-----------------------------------------

        st.header("Contexto")

        st.markdown(

            texto["contexto"]

        )

        st.divider()
        #-----------------------------------------
        # Análisis descriptivo
        #-----------------------------------------

        st.header("Análisis descriptivo")

        tabla = self.f_generar_tabla(

            estadisticos

        )

        st.code(

            tabla,

            language=None

        )

        #-----------------------------------------
        # Gráficas
        #-----------------------------------------

        self.f_visualizar_graficas(

            graficas

        )

        st.divider()
        #-----------------------------------------
        # Interpretación
        #-----------------------------------------

        st.header("Interpretación")

        st.markdown(

            interpretacion

        )

        st.divider()

        st.caption(

            "Reporte generado automáticamente por la aplicación."

        )