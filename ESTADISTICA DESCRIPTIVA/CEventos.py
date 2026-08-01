"""
CEventos.py
RUBEN PIZARRO GURROLA
AGOWSTO 2026
"""

import streamlit as st

class Eventos:

    # CONSTRUCTOR

    def __init__(self):
        pass

    # f_solicitar_parametros()
    def f_solicitar_parametros(self):
        st.subheader("Generación de números aleatorios")
        n = st.number_input(
            "Cantidad de observaciones",
            min_value=1,
            value=30,
            step=1
        )
        media = st.number_input(
            "Media",
            value=80.0,
            step=1.0
        )
        desviacion = st.number_input(
            "Desviación estándar",
            min_value=0.01,
            value=5.0,
            step=0.5
        )
        semilla = st.number_input(
            "Semilla",
            min_value=0,
            value=2026,
            step=1
        )
        etiqueta = st.text_input(
            "Etiqueta de los datos",
            value="Promedios"
        )
        return (
            int(n),
            float(media),
            float(desviacion),
            int(semilla),
            etiqueta
        )

    def f_boton_generar(self):
        return st.button(
            "Generar datos",
            use_container_width=True
        )    

    def f_boton_limpiar(self):

        return st.button(
            "Limpiar",
            use_container_width=True
        )
    def f_mostrar_dataframe(self, datos):
        st.dataframe(
            datos,
            use_container_width=True
        )

    def f_tipo_salida(self):
        st.subheader("Estructura de datos")
        return st.radio(
        "Mostrar datos como:",
        ["Texto", "DataFrame"],
        index=0,
        horizontal=True
        )


    #=====================================================
    # f_visualizaciones_graficas()
    #=====================================================
    def f_opciones_graficas(self):

        st.divider()

        st.subheader("Visualizaciones")

        c1, c2 = st.columns(2)

        histograma = c1.checkbox(
            "Histograma",
            value=True
        )

        caja = c2.checkbox(
            "Diagrama de Caja",
            value=False
        )

        st.divider()

        return histograma, caja

    # Redondear para contexto
    def f_opcion_redondear(self):

        st.subheader("Formato de los datos")

        redondear = st.checkbox(
            "Redondear valores",
            value=False
        )

        decimales = st.number_input(
            "Número de decimales",
            min_value=0,
            max_value=10,
            value=2,
            step=1,
            disabled=not redondear
        )

        return redondear, decimales
#