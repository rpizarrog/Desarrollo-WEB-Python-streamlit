"""
=========================================================
ARCHIVO
app.py

AUTOR
Rubén Pizarro Gurrola

FECHA
Agosto 2026
=========================================================
"""

import streamlit as st

from CEstadisticos import Estadisticos
from CEventos import Eventos

#=========================================================
# CREAR OBJETOS
#=========================================================

estad = Estadisticos()
eventos = Eventos()

#=========================================================
# TÍTULO
#=========================================================

st.title("Estadística Descriptiva")
st.write("Generación de números aleatorios con distribución Normal")
st.divider()

tipo_salida = eventos.f_tipo_salida()

redondear, decimales = eventos.f_opcion_redondear()

histograma, caja = eventos.f_opciones_graficas()



#=========================================================
# SOLICITAR PARÁMETROS
#=========================================================

n, media, desviacion, semilla, etiqueta = \
    eventos.f_solicitar_parametros()


#=========================================================
# BOTÓN
#=========================================================

btn_generar = st.button(
    "Generar datos",
    use_container_width=True
)

#=========================================================
# GENERAR DATOS
#=========================================================

if btn_generar:

    #---------------------------------------------
    # Generar números
    #---------------------------------------------

    datos, etiqueta = estad.f_generar_normales(
        n,
        media,
        desviacion,
        semilla,
        etiqueta
    )


    if redondear:
        datos = estad.f_redondear_datos(
            datos,
            decimales
        )

    st.subheader("Datos generados")

    #---------------------------------------------
    # Mostrar según formato seleccionado
    #---------------------------------------------

    if tipo_salida == "Texto":
        st.text(", ".join(map(str, datos)))
    else:
        datos = estad.f_convertir_df(
            datos,
            etiqueta
        )
        st.dataframe(
            datos,
            use_container_width=True
        )

    #---------------------------------------------
    # Estadísticos descriptivos
    #---------------------------------------------

    if tipo_salida == "Texto":
        datos_df = estad.f_convertir_df(
            datos,
            etiqueta
        )
    else:
        datos_df = datos
    resultado = estad.f_describir_datos(
        datos_df
    )

    st.subheader("Estadísticos descriptivos")
    st.dataframe(
        resultado["describe"],
        use_container_width=True
    )


    #=========================================================
    # VISUALIZACIONES
    #=========================================================

    # Ambos gráficos
    if histograma and caja:
        col1, col2 = st.columns(2)

        with col1:

            fig = estad.f_generar_histograma(
                datos_df,
                etiqueta
            )

            st.pyplot(fig)

        with col2:

            fig = estad.f_generar_caja(
                datos_df,
                etiqueta
            )

            st.pyplot(fig)

    # Solo Histograma
    elif histograma:
        fig = estad.f_generar_histograma(
            datos_df,
            etiqueta
        )

        st.pyplot(fig)

    # Solo Caja
    elif caja:
        fig = estad.f_generar_caja(
            datos_df,
            etiqueta
        )

        st.pyplot(fig)

    # Ninguna seleccionada
    else:
        st.info(
            "Seleccione al menos una visualización."
        )
