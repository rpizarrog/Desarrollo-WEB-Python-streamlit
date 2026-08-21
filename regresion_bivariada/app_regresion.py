import streamlit as st

from CEventos import Eventos

st.set_page_config(
    page_title="Machine Learning",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Machine Learning")

st.subheader("Regresión Bivariada con Inteligencia Artificial")

st.info(
    """
    Esta aplicación permite construir, evaluar e interpretar modelos de
    regresión bivariada mediante diferentes técnicas de regresión,
    incorporando un Sistema Experto y modelos de Inteligencia Artificial 
    para su Interprtación.
    """
)

#=====================================================
# INTERFAZ
#=====================================================

eventos = Eventos()

eventos.f_interfaz()