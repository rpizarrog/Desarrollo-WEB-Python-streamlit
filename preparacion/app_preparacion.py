#=========================================================
# ARCHIVO
# app_preparacion.py
#
# AUTOR
# Rubén Pizarro Gurrola
#
# FECHA
# Agosto 2026
#
# DESCRIPCIÓN
#
# Aplicación para preparar datos antes de su análisis.
#
# Instalar en el entonro virtual pip install streamlit pandas openpyxl
#=========================================================

#=========================================================
# ARCHIVO
# app_preparacion.py
#
# AUTOR
# Rubén Pizarro Gurrola
#
# FECHA
# Agosto 2026
#
#=========================================================

import streamlit as st

from CPreparador import Preparador


#=========================================================
# CONFIGURACIÓN
#=========================================================

st.set_page_config(

    page_title="Preparación de Datos",

    page_icon="🧹",

    layout="wide"

)


#=========================================================
# TÍTULO
#=========================================================

st.title("🧹 Preparación de Datos")

st.caption(

    "Herramienta para preparar conjuntos de datos antes del análisis."

)


#=========================================================
# OBJETO
#=========================================================

preparador = Preparador()


#=========================================================
# CARGAR ARCHIVO
#=========================================================

archivo = st.file_uploader(

    "Seleccione un archivo",

    type=["csv", "xlsx"]

)


if archivo is not None:

    #-----------------------------------------------------
    # Cargar datos
    #-----------------------------------------------------

    datos = preparador.f_cargar_datos(

        archivo

    )

    #-----------------------------------------------------
    # Mostrar originales
    #-----------------------------------------------------

    st.subheader(

        "Datos originales"

    )

    st.dataframe(

        datos,

        use_container_width=True,

        height=200

    )

    st.divider()

    #-----------------------------------------------------
    # Botón
    #-----------------------------------------------------

    if st.button(

        "Preparar datos",

        use_container_width=True,

        type="primary"

    ):

        #---------------------------------------------
        # Preparar
        #---------------------------------------------

        datos_limpios = preparador.f_preparar_datos(

            datos

        )

        st.success(

            "Datos preparados correctamente."

        )


        #---------------------------------------------
        # Mostrar resultado
        #---------------------------------------------

        st.subheader(

            "Datos preparados"

        )

        st.dataframe(

            datos_limpios,

            use_container_width=True,

            height=350

        )

        st.divider()

        #---------------------------------------------
        # Descargar
        #---------------------------------------------
        csv, nombre_salida = preparador.f_guardar(

            datos_limpios,

            archivo

        )

        st.download_button(

            label="Descargar datos preparados",

            data=csv,

            file_name=nombre_salida,

            mime="text/csv",

            use_container_width=True

        )