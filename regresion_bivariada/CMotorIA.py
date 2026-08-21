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

        prompt = f"""
    Actúa como un profesor universitario con experiencia
    en Machine Learning, Estadística y Ciencia de Datos.

    Interpreta el siguiente modelo de regresión bivariada.

    No repitas únicamente los valores numéricos.

    Explica:

    - el tipo de regresión;
    - el significado de la ecuación;
    - la calidad del ajuste;
    - la capacidad predictiva;
    - recomendaciones;
    - conclusión.

    --------------------------------------------------

    Tipo de regresión:
    {regresion.tipo}

    Variable independiente:
    {regresion.variable_x}

    Variable dependiente:
    {regresion.variable_y}

    Ecuación:

    {ecuacion}

    R² = {m["R2"]}

    R² Ajustado = {m["R2_Ajustado"]}

    RMSE = {m["RMSE"]}

    MAE = {m["MAE"]}

    MAPE = {m["MAPE"]}

    AIC = {m["AIC"]}

    BIC = {m["BIC"]}

    --------------------------------------------------

    Regresa el contenido:
    - en formato markdown
    - Titulos de enacabezado de # primer nivel  
    - # Objetivo
    - # Metodología
    - # Resultados
    - # Conclusiones
    - resto del texto en modo normal
    - en donde haya fórmulas regesa con $$formula$$ por ejemplo $$f(y)= a+bx$$

    """

        return prompt