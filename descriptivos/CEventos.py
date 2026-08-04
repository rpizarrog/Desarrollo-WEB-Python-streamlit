"""
=========================================================
ARCHIVO
CEventos.py

AUTOR
Rubén Pizarro Gurrola

FECHA
Agosto 2026

DESCRIPCIÓN

Controlador principal de la aplicación.

Su responsabilidad consiste en coordinar la interacción
entre la interfaz Streamlit y las clases:

• Estadisticos
• Interpretador
• MotorIA

No realiza cálculos estadísticos.
No genera interpretaciones.
No implementa modelos de IA.

=========================================================
"""

#=========================================================
# LIBRERÍAS
#=========================================================

import streamlit as st

from CEstadisticos import Estadisticos

from CInterpretador import Interpretador

from CMotorIA import MotorIA


#=========================================================
# CLASE
#=========================================================

class Eventos:

    """
    Controlador principal.
    """


    #=====================================================
    # CONSTRUCTOR
    #=====================================================

    def __init__(self):

        self.estad = Estadisticos()

        self.interpretador = Interpretador()

        self.motorIA = None


    #=====================================================
    # SESSION STATE
    #=====================================================

    def f_inicializar(self):

        if "estadisticos" not in st.session_state:

            st.session_state["estadisticos"] = None


        if "texto_reglas" not in st.session_state:

            st.session_state["texto_reglas"] = ""


        if "texto_ia" not in st.session_state:

            st.session_state["texto_ia"] = ""


        # if "texto_estudiante" not in st.session_state:
        #
        #    st.session_state["texto_estudiante"] = ""


        if "prompt" not in st.session_state:

            st.session_state["prompt_ia"] = ""


        if "datos_cargados" not in st.session_state:

            st.session_state["datos_cargados"] = False



    #=====================================================
    # COLUMNA IZQUIERDA
    #=====================================================

    def f_columna_izquierda(self):

        st.subheader("Configuración")


        #---------------------------------------------
        # Archivo
        #---------------------------------------------

        archivo = st.file_uploader(

            "Seleccione un archivo",

            type=["csv","xlsx"]

        )


        if archivo is None:

            return


        self.estad.f_cargar_datos(

            archivo

        )


        st.session_state["datos_cargados"] = True


        #---------------------------------------------
        # Variable
        #---------------------------------------------

        variables = self.estad.f_obtener_variables()


        variable = st.selectbox(

            "Variable cuantitativa",

            variables

        )


        self.estad.f_seleccionar_variable(

            variable

        )


        #---------------------------------------------
        # Contexto
        #---------------------------------------------

        contexto = st.text_area(f"¿De qué se trata la variable de estudio? {variable}",
                                height=120,
                                placeholder=(
                        "Por ejemplo: Edad de pacientes, Temperatura máxima diaria, "
                        "Ventas mensuales, Tiempo de espera, Nivel de glucosa, "
                        "Promedio final de estudiantes, entre otras." ))

        self.estad.f_contexto(

            contexto)


        st.divider()


        #---------------------------------------------
        # MODELO IA
        #---------------------------------------------

        st.subheader("Modelo de IA")


        proveedor = st.radio(

            "Proveedor",

            (

                "Ollama",

                "Groq"

            )

        )


        api_key = ""


        if proveedor == "Groq":

            api_key = st.text_input(

                "API Key",

                type="password"

            )


        if proveedor == "Ollama":

            modelo_default = "qwen2.5:3b"

        else:

            modelo_default = "llama-3.3-70b-versatile"


        modelo = st.text_input(

            "Modelo",

            value=modelo_default

        )


        self.motorIA = MotorIA(

            proveedor=proveedor,

            modelo=modelo,

            api_key=api_key

        )


        st.divider()


        #---------------------------------------------
        # BOTÓN PRINCIPAL
        #---------------------------------------------

        analizar = st.button(

            "Analizar datos",

            use_container_width=True,

            type="primary"

        )


        if analizar:

            #-------------------------------
            # Estadísticos
            #-------------------------------

            estadisticos = self.estad.f_calcular_estadisticos()


            normalidad = self.estad.f_prueba_shapiro()


            estadisticos["normal"] = normalidad["normal"]

            estadisticos["pvalor"] = normalidad["pvalor"]

            estadisticos["prueba"] = normalidad["prueba"]


            st.session_state["estadisticos"] = estadisticos


            #-------------------------------
            # Sistema Experto
            #-------------------------------

            st.session_state["texto_reglas"] = (

                self.interpretador.f_generar_interpretacion(

                    estadisticos

                )

            )

            #-------------------------------
            # Gráficas
            #-------------------------------
            # Genear los graficos
            histograma = self.estad.f_generar_histograma() 
            caja = self.estad.f_generar_caja()             
            qqplot = self.estad.f_generar_qqplot()

            graficas = [

                {
                    "nombre": "Histograma",
                    "figura": histograma
                },

                {
                    "nombre": "Diagrama de caja",
                    "figura": caja
                },

                {
                    "nombre": "QQPlot",
                    "figura": qqplot
                }]

            #-------------------------------
            # IA
            #-------------------------------

            resultado = self.motorIA.f_generar_interpretacion(

                estadisticos,

                graficas

            )
            st.session_state["texto_ia"] = resultado["respuesta"]

            st.session_state["prompt_ia"] = resultado["prompt"]

    #=====================================================
    # COLUMNA CENTRAL
    #=====================================================

    def f_columna_central(self):
        """
        Panel central de la aplicación.

        Contiene:

        • Datos
        • Gráficas
        • Interpretaciones
        • Evaluación
        """

        #---------------------------------------------
        # No hay datos
        #---------------------------------------------

        if not st.session_state["datos_cargados"]:

            st.info("Seleccione un archivo para comenzar.")

            return


        #=================================================
        # DATOS
        #=================================================

        st.subheader("Datos")

        st.dataframe(

            self.estad.datos,

            use_container_width=True,

            height=250

        )


        #=================================================
        # GRÁFICAS
        #=================================================

        st.subheader("Representaciones gráficas")

        col1, col2, col3 = st.columns(3)

        # Genear los graficos
        histograma = self.estad.f_generar_histograma() 
        caja = self.estad.f_generar_caja()             
        qqplot = self.estad.f_generar_qqplot()

        with col1:

            st.pyplot(

                histograma,

                use_container_width=True

            )           

        with col2:

            st.pyplot(

                caja,

                use_container_width=True

            )

        with col3:

            st.pyplot(

                qqplot,

                use_container_width=True

            )


        #=================================================
        # INTERPRETACIONES
        #=================================================

        st.subheader("Interpretaciones")

        c1, c2 = st.columns(2)


        #---------------------------------------------
        # SISTEMA EXPERTO
        #---------------------------------------------

        with c1:

            st.text_area(

                "Sistema Experto",

                value=st.session_state["texto_reglas"],

                height=350,

                disabled=True

            )


        #---------------------------------------------
        # IA
        #---------------------------------------------

        with c2:

            st.text_area(

                "Interpretación IA",

                value=st.session_state["texto_ia"],

                height=350,

                disabled=True

            )
        
        with st.expander("Prompt utilizado por la IA",
                            expanded=False):

            st.code(

                st.session_state["prompt_ia"],

                language="text"

            )


        #=================================================
        # PROMPT
        #=================================================

        # st.subheader("Prompt")

        # st.text_area(
        #     "Prompt",

        #    value=st.session_state["prompt_ia"],

        #    height=180,

        #    disabled=True
        #)
    #=====================================================
    # COLUMNA DERECHA
    #=====================================================

    def f_columna_derecha(self):
        """
        Panel derecho.

        Contiene:

        • Estadísticos descriptivos.
        • Resultados de la prueba de normalidad.
        """

        if st.session_state["estadisticos"] is None:

            st.info("Sin resultados.")

            return


        est = st.session_state["estadisticos"]


        #=================================================
        # ESTADÍSTICOS
        #=================================================

        st.subheader("Estadísticos")

        tabla = {

            "Estadístico": [

                "Variable",

                "Observaciones",

                "Media",

                "Mediana",

                "Moda",

                "Desv. estándar",

                "Varianza",

                "Coef. variación",

                "Mínimo",

                "Máximo",

                "Rango",

                "Q1",

                "Q2",

                "Q3",

                "IQR",

                "Asimetría",

                "Curtosis"

            ],

            "Valor":[

                est["variable"],

                est["n"],

                f"{est['media']:.2f}",

                f"{est['mediana']:.2f}",

                ", ".join(

                    [

                        f"{x:.2f}"

                        for x in est["moda"]

                    ]

                ),

                f"{est['desviacion']:.2f}",

                f"{est['varianza']:.2f}",

                f"{est['cv']:.2%}",

                f"{est['minimo']:.2f}",

                f"{est['maximo']:.2f}",

                f"{est['rango']:.2f}",

                f"{est['q1']:.2f}",

                f"{est['q2']:.2f}",

                f"{est['q3']:.2f}",

                f"{est['iqr']:.2f}",

                f"{est['asimetria']:.3f}",

                f"{est['curtosis']:.3f}"

            ]

        }


        st.dataframe(

            tabla,

            use_container_width=True,

            height=430,

            hide_index=True

        )


        st.divider()


        #=================================================
        # NORMALIDAD
        #=================================================

        st.subheader("Prueba de normalidad")


        st.write(

            "**Prueba:**",

            est["prueba"]

        )


        st.write(

            "**Valor p:**",

            f"{est['pvalor']:.4f}"

        )


        st.write(

            "**Distribución normal:**",

            "Sí"

            if est["normal"]

            else

            "No"

        )


        st.divider()


        #=================================================
        # ATÍPICOS
        #=================================================

        st.subheader("Valores atípicos")


        if est["atipicos"]:

            st.success(

                f"Se detectaron "

                f"{est['numero_atipicos']} "

                f"valor(es) atípico(s)."

            )

        else:

            st.info(

                "No se detectaron "

                "valores atípicos."

            )

    #=====================================================
    # INTERFAZ
    #=====================================================

    def f_interfaz(self):
        """
        Construye la interfaz principal.
        """

        #---------------------------------------------
        # Inicializar Session State
        #---------------------------------------------

        self.f_inicializar()


        #---------------------------------------------
        # Título
        #---------------------------------------------

        st.title(
            "Análisis Descriptivo con Inteligencia Artificial"
        )

        st.caption(
            "Exploración e interpretación de datos de una variable cuantitativa mediante Sistema Experto e Inteligencia Artificial."
        )


        #---------------------------------------------
        # Diseño de tres columnas
        #---------------------------------------------

        izquierda, centro, derecha = st.columns(

            [

                1.2,

                3.8,

                1.4

            ],

            gap="medium"

        )


        #---------------------------------------------
        # Columna izquierda
        #---------------------------------------------

        with izquierda:

            self.f_columna_izquierda()


        #---------------------------------------------
        # Columna central
        #---------------------------------------------

        with centro:

            self.f_columna_central()


        #---------------------------------------------
        # Columna derecha
        #---------------------------------------------

        with derecha:

            self.f_columna_derecha()