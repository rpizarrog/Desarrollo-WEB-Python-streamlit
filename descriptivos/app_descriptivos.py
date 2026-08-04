"""
=========================================================

Rubén Pizarro Gurrola
Agosto 2026

ARCHIVO
app_descriptivos.py
=========================================================
"""

import streamlit as st

from CEventos import Eventos


st.set_page_config(

    page_title="Estadística Descriptiva",

    page_icon="📊",

    layout="wide"

)


eventos = Eventos()

eventos.f_interfaz()