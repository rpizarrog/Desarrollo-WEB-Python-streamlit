#=========================================================
# CLASE
# CEventos
#=========================================================

import streamlit as st


class Eventos:

    #-----------------------------------------------------
    # CONSTRUCTOR
    #-----------------------------------------------------

    def __init__(self):
        pass

    #-----------------------------------------------------
    # INICIALIZAR VARIABLES
    #-----------------------------------------------------

    def inicializar(self):

        if "numero1" not in st.session_state:
            st.session_state.numero1 = ""

        if "numero2" not in st.session_state:
            st.session_state.numero2 = ""

    #-----------------------------------------------------
    # LIMPIAR
    #-----------------------------------------------------

    def limpiar(self):

        st.session_state.numero1 = ""
        st.session_state.numero2 = ""

    #-----------------------------------------------------
    # INTERCAMBIAR
    #-----------------------------------------------------

    def intercambiar(self):

        (
            st.session_state.numero1,
            st.session_state.numero2
        ) = (

            st.session_state.numero2,
            st.session_state.numero1

        )

    #-----------------------------------------------------
    # OBTENER VALORES
    #-----------------------------------------------------

    def obtener_valores(self):

        return (
            st.session_state.numero1,
            st.session_state.numero2
        )



    def salir(self):
        st.warning(
            "La aplicación ha finalizado.\n\n"
            "Puede cerrar esta pestaña del navegador."
        )
        st.stop()
