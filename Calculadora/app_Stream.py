import streamlit as st

from CCalculadora import Calculadora
from CValidaciones import Validaciones
from CEventos import Eventos

calc = Calculadora()
valid = Validaciones()
eventos = Eventos()

eventos.inicializar()

st.text_input("Primer número", key="numero1")
st.text_input("Segundo número", key="numero2")

st.divider()
# Los botones
c1,c2,c3 = st.columns(3)
btn_sumar = c1.button("➕ Sumar")
btn_restar = c2.button("➖ Restar")
btn_multi = c3.button("✖ Multiplicar")

c4,c5,c6 = st.columns(3)
btn_dividir = c4.button("➗ Dividir")
btn_potencia = c5.button("xʸ Potencia")
btn_raiz = c6.button("√ Raíz")

st.divider()

# BOTONES DE CONTROL

c1, c2, c3 = st.columns(3)
c1.button(
    "🧹 Limpiar",
    on_click=eventos.limpiar)

c2.button(
    "⇄ Intercambiar",
    on_click=eventos.intercambiar)

btn_salir = c3.button(
    "❌ Salir", 
    on_click=eventos.salir)


#=========================================================
# OBTENER VALORES
#=========================================================

numero1, numero2 = eventos.obtener_valores()

#=========================================================
# OPERACIONES
#=========================================================

if (
    btn_sumar or
    btn_restar or
    btn_multi or
    btn_dividir or
    btn_potencia or
    btn_raiz
):

    try:

        #-----------------------------------------
        # VALIDAR DATOS
        #-----------------------------------------

        a, b = valid.validar_numeros(
            numero1,
            numero2
        )

        #-----------------------------------------
        # OPERACIONES
        #-----------------------------------------

        if btn_sumar:

            resultado = calc.sumar(a, b)

        elif btn_restar:

            resultado = calc.restar(a, b)

        elif btn_multi:

            resultado = calc.multiplicar(a, b)

        elif btn_dividir:

            resultado = calc.dividir(a, b)

        elif btn_potencia:

            resultado = calc.potencia(a, b)

        elif btn_raiz:

            resultado = calc.raiz(a, b)

        #-----------------------------------------
        # MOSTRAR RESULTADO
        #-----------------------------------------

        st.success(f"Resultado = {resultado:.6f}")

    except Exception as e:

        st.error(e)

