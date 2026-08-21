"""
=========================================================
ARCHIVO
CMotorIA.py

AUTOR
Rubén Pizarro Gurrola

DESCRIPCIÓN

Motor de Inteligencia Artificial para
interpretar modelos de Regresión
Bivariada.

Utiliza Groq.

=========================================================
"""


from groq import Groq

class MotorIA:

    #=====================================================
    # CONSTRUCTOR
    #=====================================================

    def __init__(self):

        self.proveedor = None

        self.modelo = None

        self.api_key = None

        self.servidor = None

        self.temperature = 0.20

        self.max_tokens = 2500

        self.cliente = None

    #=====================================================
    # CONFIGURAR IA
    #=====================================================

    def f_configurar(
            self,
            proveedor,
            modelo,
            api_key="",
            servidor=""):

        self.proveedor = proveedor

        self.modelo = modelo

        self.api_key = api_key

        self.servidor = servidor

        #-----------------------------------------
        # GROQ
        #-----------------------------------------

        if proveedor == "Groq":

            self.cliente = Groq(

                api_key=self.api_key

            )

        #-----------------------------------------
        # OLLAMA
        #-----------------------------------------

        elif proveedor == "Ollama":

            self.cliente = None

        #-----------------------------------------
        # OPENAI
        #-----------------------------------------

        elif proveedor == "OpenAI":

            self.cliente = None

    #=====================================================
    # CONSULTAR GROQ
    #=====================================================

    def f_consultar_groq(
            self,
            prompt):
        """
        Envía un prompt al modelo Groq
        y devuelve la respuesta.
        """

        respuesta = self.cliente.chat.completions.create(

            model=self.modelo,

            messages=[

                {
                    "role": "system",
                    "content":
                    "Eres un profesor universitario "
                    "especialista en Machine Learning, "
                    "Estadística y Ciencia de Datos."
                },

                {
                    "role": "user",
                    "content": prompt
                }

            ],

            temperature=self.temperature,

            max_completion_tokens=self.max_tokens

        )

        return respuesta.choices[0].message.content


    #=====================================================
    # CONSULTAR IA
    #=====================================================

    def f_consultar_ia(
            self,
            prompt):
        """
        Consulta el proveedor de IA seleccionado.
        """

        if self.proveedor == "Groq":

            return self.f_consultar_groq(
                prompt
            )

        elif self.proveedor == "Ollama":

            return "Pendiente implementación Ollama."

        elif self.proveedor == "OpenAI":

            return "Pendiente implementación OpenAI."

        else:

            return "No se seleccionó proveedor."

    #=====================================================
    # GENERAR INTERPRETACIÓN IA
    #=====================================================

    def f_generar_interpretacion_ia(
            self,
            regresion):
        """
        Genera la interpretación mediante
        Inteligencia Artificial.
        """


        prompt = self.f_generar_prompt(
            regresion
        )

        prompt = self.f_generar_prompt(regresion)


        respuesta = self.f_consultar_ia(
            prompt
        )

        respuesta = self.f_consultar_ia(prompt)


        return {

            "prompt": prompt,

            "interpretacion": respuesta

        }

    #=====================================================
    # GENERAR PROMPT
    #=====================================================

    def f_generar_prompt(
            self,
            regresion):
        """
        Construye el prompt que será enviado
        a la Inteligencia Artificial.
        """

        ecuacion = regresion.f_ecuacion()["ecuacion"]

        m = regresion.metricas

        #-----------------------------------------
        # SUPUESTOS
        #-----------------------------------------

        linealidad = regresion.f_verificar_linealidad()

        normalidad = regresion.f_generar_QQPlot()

        homocedasticidad = regresion.f_generar_residuos()

        independencia = regresion.f_independencia_residuos()


        prompt = f"""
    Actúa como un profesor universitario con amplia experiencia
    en Machine Learning, Estadística, Ciencia de Datos
    y Modelos de Regresión.

    Tu tarea consiste en interpretar un modelo de regresión
    bivariada desde una perspectiva estadística y de
    aprendizaje automático.

    No repitas únicamente los valores numéricos.

    Relaciona las métricas entre sí y explica sus
    implicaciones prácticas.

    Redacta la interpretación como si formara parte de
    un artículo científico o de un informe técnico.

    ==================================================
    MODELO DE REGRESIÓN
    ==================================================

    Tipo de regresión:

    {regresion.tipo}

    Variable independiente (X):

    {regresion.variable_x}

    Variable dependiente (Y):

    {regresion.variable_y}

    Ecuación del modelo:

    {ecuacion}

    ==================================================
    INDICADORES DE EVALUACIÓN
    ==================================================

    Coeficiente de Determinación (R²)

    {m["R2"]}

    Coeficiente de Determinación Ajustado (R² Ajustado)

    {m["R2_Ajustado"]}

    Raíz del Error Cuadrático Medio (RMSE)

    {m["RMSE"]}

    Error Absoluto Medio (MAE)

    {m["MAE"]}

    Error Porcentual Absoluto Medio (MAPE)

    {m["MAPE"]}

    Criterio de Información de Akaike (AIC)

    {m["AIC"]}

    Criterio de Información Bayesiano (BIC)

    {m["BIC"]}

    ==================================================
    VERIFICACIÓN DE LOS SUPUESTOS
    ==================================================

    Adecuación de la forma funcional

    Prueba:
    {linealidad["Prueba"]}

    Estadístico F:

    {linealidad["F"]}

    Valor-p:

    {linealidad["p_valor"]}


    ------------------------------------------

    Normalidad de los residuos

    Prueba:
    Shapiro-Wilk

    Estadístico W:

    {normalidad["W"]}

    Valor-p:

    {normalidad["p_valor"]}


    ------------------------------------------

    Homocedasticidad

    Prueba:
    Breusch-Pagan

    LM:

    {homocedasticidad["LM"]}

    Valor-p:

    {homocedasticidad["LM_pvalor"]}


    ------------------------------------------

    Independencia de los residuos

    Prueba:
    Durbin-Watson

    Estadístico:

    {independencia["Durbin_Watson"]}


    ==================================================
    INSTRUCCIONES
    ==================================================

    Genera la respuesta en formato Markdown.

    Utiliza exactamente los siguientes encabezados
    de primer nivel:

    # Objetivo

    Describe el objetivo del modelo construido y
    la relación que intenta representar entre las variables.

    # Metodología

    Explica:

    - el tipo de regresión seleccionado;
    - el significado de la ecuación;
    - la interpretación general de los coeficientes;
    - por qué este tipo de modelo puede ser adecuado
    para representar la relación entre las variables.

    Cuando escribas una ecuación utiliza siempre
    el formato:

    $$
    f(y)=a+bx
    $$

    # Resultados

    Interpreta:

    - el significado de la ecuación;
    - la calidad del ajuste utilizando R² y R² Ajustado;
    - la precisión del modelo utilizando RMSE,
    MAE y MAPE;
    - la complejidad del modelo mediante AIC y BIC;
    - la capacidad predictiva del modelo.

    No repitas únicamente los valores.

    Explica su significado y relaciónalos entre sí.

    Incluye un apartado denominado

    ## Verificación de los supuestos

    Para cada prueba estadística:

    - explica qué supuesto verifica;
    - interpreta el estadístico obtenido;
    - interpreta el valor-p cuando exista;
    - determina si el supuesto puede considerarse
    satisfecho utilizando α = 0.05;
    - explica las implicaciones sobre la validez
    del modelo.

    No inventes información distinta a la
    proporcionada por las pruebas.

    # Conclusiones

    Presenta una conclusión general indicando:

    - si el modelo puede considerarse adecuado;
    - cuáles son sus fortalezas;
    - cuáles son sus limitaciones;
    - en qué situaciones podría utilizarse;
    - qué recomendaciones propondrías para mejorar
    el modelo.

    ==================================================
    REGLAS
    ==================================================

    - Escribe únicamente en español.

    - Utiliza lenguaje académico claro,
    objetivo y profesional.

    - No inventes información que no pueda
    deducirse de los resultados.

    - No repitas la misma idea en distintas secciones.

    - No utilices tablas.

    - Utiliza listas únicamente cuando
    aporten claridad.

    - Cuando escribas una ecuación utiliza
    siempre el formato:

    $$
    ecuación
    $$

    - No reproduzcas literalmente los datos;
    interprétalos.

    """

        return prompt