"""
=========================================================
ARCHIVO
CEventos.py

AUTOR
Rubén Pizarro Gurrola

FECHA
Agosto 2026

DESCRIPCIÓN

Administra la interfaz de usuario
de la aplicación Regresión Bivariada.

Versión 1.0

Parte A

Inicialización del sistema.

=========================================================
"""

#=========================================================
# LIBRERÍAS
#=========================================================

import streamlit as st

from CEstadisticos import Estadisticos
from CRegresion import Regresion

from CInterpretador import Interpretador
from CMotorIA import MotorIA

from st_copy_to_clipboard import st_copy_to_clipboard




#=========================================================
# CLASE
#=========================================================

class Eventos:


    #=====================================================
    # CONSTRUCTOR
    #=====================================================

    def __init__(self):

        self.estad = Estadisticos()
        self.interpretador = Interpretador()
        self.motorIA = MotorIA()

        if "regresion" not in st.session_state:

            st.session_state["regresion"] = Regresion()

        self.regresion = st.session_state["regresion"]

        self.f_inicializar_estado()

    #=====================================================
    # SESSION STATE
    #=====================================================

    def f_inicializar_estado(self):
        """
        Inicializa las variables
        de session_state.
        """

        if "datos_cargados" not in st.session_state:

            st.session_state["datos_cargados"] = False

        if "modelo_construido" not in st.session_state:

            st.session_state["modelo_construido"] = False

        if "datos" not in st.session_state:

            st.session_state["datos"] = None




    #=====================================================
    # CARGAR DATOS
    #=====================================================

    def f_cargar_datos(self):
        """
        Permite cargar un archivo
        CSV o Excel.
        """

        archivo = st.file_uploader(

            "Seleccione un archivo",

            type=["csv", "xlsx"]

        )


        if archivo is not None:

            datos = self.estad.f_cargar_datos(
                archivo
            )

            st.session_state["datos"] = datos

            st.session_state["datos_cargados"] = True

            self.regresion.f_asignar_datos(

                datos

            )



    #=====================================================
    # INTERFAZ
    #=====================================================
    
    def f_interfaz(self):

        col1, col2, col3 = st.columns([1,2,1])

        with col1:

            self.f_panel_configuracion()

        with col2:

            self.f_panel_datos()

        with col3:

            self.f_panel_analisis()

    def f_panel_configuracion(self):

        self.f_bloque_datos()

        st.divider()

        self.f_bloque_modelo()

        st.divider()

        self.f_bloque_ejecutar()

        st.divider()
        
        self.f_bloque_ia()

    def f_panel_datos(self):

        st.subheader("📄 Conjunto de Datos")

        if st.session_state["datos_cargados"]:
            
            resumen = self.estad.f_resumen()

            col1, col2 = st.columns(2)

            with col1:

                st.metric(

                    "Observaciones",

                    resumen["Observaciones"]

                )

            with col2:

                st.metric(

                    "Variables",

                    resumen["Variables"]

                )

            st.dataframe(

                self.estad.f_obtener_datos(),

                height=400,

                use_container_width=True,

                hide_index=True

            )

            #-----------------------------------------
            # Gráfica del modelo
            #-----------------------------------------

            if st.session_state["modelo_construido"]:

                st.divider()

                st.subheader("📈 Modelo Ajustado")

                resultado = self.regresion.f_generar_grafica_modelo()

                st.pyplot(
                    resultado["figura"],
                    use_container_width=True
                )


                #-----------------------------------------
                # Botón Interpretar Modelo IA
                #-----------------------------------------

                if st.button(
                    "🧠 Interpretar Regresión con Experto e IA",
                    use_container_width=True
                ):

                    #-----------------------------------------
                    # Configurar Motor IA
                    #-----------------------------------------

                    self.motorIA.f_configurar(

                        proveedor = st.session_state["proveedor"],

                        modelo = st.session_state["modelo"],

                        api_key = st.session_state["api_key"],

                        servidor = st.session_state["servidor"]

                    )

                    st.session_state["interpretacion_generada"] = True


                if st.session_state.get(
                    "interpretacion_generada",
                    False
                ):

                    self.f_interpretacion()

            
    
                
    #=====================================================
    # PANEL ANÁLISIS
    #=====================================================

    def f_panel_analisis(self):

        st.subheader("📊 Análisis de Regresión")

        if not st.session_state["modelo_construido"]:

            st.info(
                "Configure y construya un modelo para visualizar el análisis."
            )

            return

        self.f_modelo()

        self.f_evaluacion()

        # self.f_graficas()

        self.f_postulados()

        # self.f_sistema_experto()

        # self.f_ia()

        # self.f_reportes()

    #=====================================================
    # Estos bloques son para panel de configuracion    
    #=====================================================
    # BLOQUE DATOS
    #=====================================================

    def f_bloque_datos(self):
        """
        Permite cargar un conjunto de datos.
        """

        st.markdown("### 📂 Cargar Datos")

        archivo = st.file_uploader(

            "Seleccione un archivo",

            type=["csv", "xlsx"]

        )

        if archivo is not None:

            datos = self.estad.f_cargar_datos(

                archivo

            )

            self.regresion.f_asignar_datos(

                datos

            )

            st.session_state["datos"] = datos

            st.session_state["datos_cargados"] = True

    #=====================================================
    # BLOQUE MODELO
    #=====================================================

    def f_bloque_modelo(self):
        """
        Configuración del modelo de regresión.
        """

        st.markdown("### 📐 Modelo de Regresión")

        if not st.session_state["datos_cargados"]:

            st.info(

                "Primero cargue un conjunto de datos."

            )

            return


        variables = self.estad.f_obtener_variables_numericas()


        tipo = st.selectbox(

            "Tipo de regresión",

            [

                "Lineal",

                "Polinomial",

                "Exponencial",

                "Logarítmica",

                "Potencial"

            ]

        )


        variable_x = st.selectbox(

            "Variable independiente (X)",

            variables

        )


        variable_y = st.selectbox(

            "Variable dependiente (Y)",

            variables,

            index=1 if len(variables)>1 else 0

        )


        grado = 1

        if tipo == "Polinomial":

            grado = st.selectbox(

                "Grado",

                [2,3,4,5]

            )


        entrenamiento = st.slider(

            "Entrenamiento (%)",

            50,

            90,

            80

        )


        st.session_state["tipo"] = tipo

        st.session_state["variable_x"] = variable_x

        st.session_state["variable_y"] = variable_y

        st.session_state["grado"] = grado

        st.session_state["entrenamiento"] = entrenamiento

    #=====================================================
    # BLOQUE IA
    #=====================================================

    def f_bloque_ia(self):
        """
        Configuración del modelo
        de Inteligencia Artificial.
        """

        st.markdown("### 🤖 Inteligencia Artificial")


        proveedor = st.selectbox(

            "Proveedor IA",

            [

                "Ninguno",

                "Groq",

                "Ollama",

                "OpenAI"

            ]

        )

        #-----------------------------------------
        # Inicializar variables
        #-----------------------------------------

        api_key = ""

        servidor = ""

        modelo = ""

        if proveedor == "Groq":

            modelo = st.selectbox(

                "Modelo",

                [

                    "openai/gpt-oss-120b",

                    "qwen/qwen3.6-27b",

                    "groq/compound",

                    "groq/compound-mini"

                ]

            )

            api_key = st.text_input(

                "API Key",

                type="password"

            )

        if proveedor == "Ollama":

            servidor = st.text_input(

                "Servidor",

                "http://localhost:11434"

            )

        if proveedor == "OpenAI":

            modelo = st.selectbox(

                "Modelo IA",

                [

                    "gpt-5",

                    "gpt-5-mini",

                    "gpt-4.1"

                ]

            )

            api_key = st.text_input(

                "API Key",

                type="password"

            )


        st.session_state["proveedor"] = proveedor

        st.session_state["modelo"] = modelo

        st.session_state["api_key"] = api_key

        st.session_state["servidor"] = servidor

    #=====================================================
    # BLOQUE EJECUTAR
    #=====================================================

    def f_bloque_ejecutar(self):
        """
        Ejecuta la construcción
        del modelo.
        """

        st.markdown("### ▶ Ejecutar")


        if st.button(

            "Construir Modelo de Regresión",

            use_container_width=True

        ):

            self.f_construir_modelo() # Esta construye el modelo
            ## st.session_state["modelo_construido"] = True



    #=====================================================
    # Estas funciones son para el panel de analisis de la derecha
    #=====================================================
    # MODELO
    #=====================================================

    def f_modelo(self):

        with st.expander(
            "📐 Modelo de Reg. Matemático",
            expanded=True
        ):

            resumen = self.regresion.f_resumen()

            ecuacion = self.regresion.f_ecuacion()

            st.write(f"**Tipo:** {resumen['Modelo']}")

            if resumen["Grado"] > 1:

                st.write(f"**Grado:** {resumen['Grado']}")

            st.write(f"**Variable X:** {resumen['Variable X']}")

            st.write(f"**Variable Y:** {resumen['Variable Y']}")

            st.write(
                f"**Entrenamiento:** "
                f"{resumen['Entrenamiento (%)']} %"
            )

            st.write(
                f"**Validación:** "
                f"{resumen['Validación (%)']} %"
            )

            st.write("---")

            st.write("### Ecuación")

            st.code(

                ecuacion["ecuacion"]

            )
    #=====================================================
    # EVALUACIÓN
    #=====================================================

    def f_evaluacion(self):

        with st.expander("📈 Evaluación del Modelo de Reg."):

            evaluacion = self.regresion.f_evaluacion_modelo()

            for k, v in evaluacion.items():

                st.write(f"**{k}:** {v}")

    # Creo que esta función es obsoleta, no se usa
    # def f_graficas(self):
    #     grafica = st.selectbox(

    #        "Seleccione una gráfica",

    #        [

    #            "Modelo",

    #            "Residuos",

    #            "QQPlot"

    #        ] )

    #=====================================================
    # POSTULADOS DEL MODELO
    #=====================================================

    def f_postulados(self):
        """
        Permite visualizar la verificación
        de los postulados del modelo de
        regresión.
        """

        with st.expander(
            "📋 Verificación de Supuestos"
        ):

            st.caption(
                "Seleccione los supuestos que desea analizar."
            )

            col1, col2 = st.columns(2)

            with col1:

                linealidad = st.checkbox(
                    "Linealidad"
                )

                normalidad = st.checkbox(
                    "Normalidad"
                )

            with col2:

                homocedasticidad = st.checkbox(
                    "Homocedasticidad"
                )

                independencia = st.checkbox(
                    "Independencia"
                )

            #-----------------------------------------
            # LINEALIDAD
            #-----------------------------------------
            if linealidad:

                st.markdown(
                    "### 📈 Adecuación de la Forma Funcional"
                )

                resultado = self.regresion.f_verificar_linealidad()

                # st.write(resultado)

                st.write(
                    f"**Prueba:** {resultado['Prueba']}"
                )

                st.write(
                    f"**Estadístico F:** {resultado['F']}"
                )

                st.write(
                    f"**Valor-p:** {resultado['p_valor']}"
                )

                st.divider()

                if resultado["p_valor"] > 0.05:

                    st.success(

                        "No existe evidencia estadísticamente "
                        "significativa para rechazar la forma "
                        "funcional del modelo. El supuesto puede "
                        "considerarse satisfecho."

                    )

                else:

                    st.error(

                        "Existe evidencia de una posible mala "
                        "especificación del modelo. Se recomienda "
                        "evaluar otra forma funcional."

                    )

            #-----------------------------------------
            # NORMALIDAD
            #-----------------------------------------

            if normalidad:

                st.markdown("### 📊 Normalidad")

                resultado = self.regresion.f_generar_QQPlot()

                st.write(
                    f"W = {resultado['W']}"
                )

                st.write(
                    f"p-valor = {resultado['p_valor']}"
                )

                st.pyplot(
                    resultado["figura"]
                )

            #-----------------------------------------
            # HOMOCEDASTICIDAD
            #-----------------------------------------

            if homocedasticidad:

                st.markdown("### 📉 Homocedasticidad")

                resultado = self.regresion.f_generar_residuos()

                st.write(
                    f"LM = {resultado['LM']}"
                )

                st.write(
                    f"p-valor = {resultado['LM_pvalor']}"
                )

                st.pyplot(
                    resultado["figura"]
                )

            #-----------------------------------------
            # INDEPENDENCIA
            #-----------------------------------------

            if independencia:

                st.markdown("### 📌 Independencia")

                resultado = self.regresion.f_independencia_residuos()

                st.write(
                    f"Durbin-Watson = "
                    f"{resultado['Durbin_Watson']}"
                )

    #=====================================================
    # CONSTRUIR MODELO
    #=====================================================

    def f_construir_modelo(self):
        """
        Construye el modelo de regresión a partir
        de la configuración seleccionada por
        el usuario.
        """

        try:

            #-----------------------------------------
            # Recuperar configuración
            #-----------------------------------------

            tipo = st.session_state["tipo"]

            grado = st.session_state["grado"]

            variable_x = st.session_state["variable_x"]

            variable_y = st.session_state["variable_y"]

            entrenamiento = st.session_state["entrenamiento"]


            #-----------------------------------------
            # Configurar Regresión
            #-----------------------------------------

            self.regresion.f_asignar_variables(

                variable_x,

                variable_y

            )

            self.regresion.f_asignar_modelo(

                tipo,

                grado

            )

            self.regresion.f_asignar_particion(

                entrenamiento

            )


            #-----------------------------------------
            # Construcción del modelo
            #-----------------------------------------

            self.regresion.f_dividir_datos()


            self.regresion.f_crear_modelo()

            self.regresion.f_predecir()

            self.regresion.f_evaluacion_modelo()


            #-----------------------------------------
            # Modelo listo
            #-----------------------------------------

            st.session_state["modelo_construido"] = True

            st.success(

                "Modelo de Regesión construido correctamente."

            )


        except Exception as e:

            st.session_state["modelo_construido"] = False

            st.error(str(e))

    def f_interpretacion(self):

        st.divider()

        st.header(

            "🧠 Interpretación del Modelo de Regresión"

        )
        st.caption("El Sistema Experto y la Inteligencia Artificial analizan automáticamente el modelo " \
        "de regresión construido para generar una interpretación estadística y una explicación en " \
        "lenguaje natural."
        )

        st.caption("El Sistema Experto será un asistente de interpretación estadística de los modelos de regresión.")
        st.caption("La interpretación que genera el modelo de IA elegido,  "\
                   "enriquece lo que se genera con el experto.")


        # interpretacion = "" # variable local de la función o método
        

        if st.session_state["modelo_construido"]:
            #-----------------------------------------
            # Sistema Experto
            #-----------------------------------------

            interpretacion_experto = self.interpretador.f_generar_interpretacion(

                        self.regresion

                    )

            #-----------------------------------------
            # Inteligencia Artificial
            #-----------------------------------------

            resultado_ia = self.motorIA.f_generar_interpretacion_ia(

                self.regresion

            )

            interpretacion_ia = resultado_ia["interpretacion"]
            
            prompt = resultado_ia["prompt"]

        col1, col2 = st.columns(2)

        #-----------------------------------------
        # Sistema Experto
        #-----------------------------------------

        with col1:

            st.subheader(

                "📋 Sistema Experto"

            )
            st_copy_to_clipboard(interpretacion_experto)
            st.text_area(

                label="",

                value=interpretacion_experto,

                height=350,

                key="interpretacion_experto"

            )

        #-----------------------------------------
        # Inteligencia Artificial
        #-----------------------------------------

        with col2:

            st.subheader(

                "🤖 Inteligencia Artificial"

            )
            st_copy_to_clipboard(interpretacion_ia)
            st.text_area(

                label="",

                value=interpretacion_ia,

                height=350,

                key="interpretacion_ia"

            )

        #-----------------------------------------
        # Prompt
        #-----------------------------------------

        st.divider()

        with st.expander(

            "🤖 Prompt enviado a IA",

            expanded=False

        ):

            st.code(

                prompt,

                language="text"

            )
