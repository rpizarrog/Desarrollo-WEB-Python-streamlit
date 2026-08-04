"""
=========================================================
ARCHIVO
CMotorIA.py

AUTOR
Rubén Pizarro Gurrola

FECHA
Agosto 2026

DESCRIPCIÓN

La clase MotorIA concentra los servicios de Inteligencia
Artificial utilizados por la aplicación.

Permite trabajar con diferentes proveedores de modelos
de lenguaje como:

• Ollama
• Groq
• OpenAI (futuro)
• Gemini (futuro)

Todos los servicios reciben como entrada un único
diccionario denominado contexto, generado previamente
por la clase Estadisticos.

SERVICIOS

• Generar interpretación.
• Evaluar interpretación.
• Generar retroalimentación.
• Generar preguntas.
• Sugerir mejoras.
=========================================================
"""

#=========================================================
# LIBRERÍAS
#=========================================================

import ollama

from groq import Groq


#=========================================================
# CLASE
#=========================================================

class MotorIA:

    """
    Clase responsable de comunicarse con motores de IA.
    """

    #=====================================================
    # CONSTRUCTOR
    #=====================================================

    def __init__(
            self,
            proveedor="ollama",
            modelo="qwen2.5:3b",
            api_key=None,
            temperatura=0.30,
            max_tokens=1000):

        self.proveedor = proveedor.lower()

        self.modelo = modelo

        self.api_key = api_key

        self.temperatura = temperatura

        self.max_tokens = max_tokens

        self.cliente = None

        self.f_conectar()


    #=====================================================
    # CONECTAR
    #=====================================================

    def f_conectar(self):
        """
        Inicializa el proveedor seleccionado.
        """

        if self.proveedor == "ollama":

            self.cliente = None

        elif self.proveedor == "groq":

            if self.api_key is None:

                raise ValueError(
                    "Debe proporcionar una API Key para Groq."
                )

            self.cliente = Groq(
                api_key=self.api_key
            )

        elif self.proveedor == "openai":

            raise NotImplementedError(
                "OpenAI aún no está implementado."
            )

        elif self.proveedor == "gemini":

            raise NotImplementedError(
                "Gemini aún no está implementado."
            )

        else:

            raise ValueError(
                f"Proveedor no soportado: {self.proveedor}"
            )


    #=====================================================
    # PROMPT INTERPRETACIÓN
    #=====================================================

    def f_generar_prompt_interpretacion(
            self,
            contexto,
            graficas=None):
        """
        Construye el prompt para interpretar
        estadísticos descriptivos.
        """

        lineas = []

        lineas.append(
            "Eres profesor universitario experto en Estadística Descriptiva."
        )

        lineas.append(
            "Genera una interpretación académica, clara y amigable."
        )

        lineas.append(
            "No excedas 250 palabras."
        )

        lineas.append("")

        lineas.append(
            f"Variable: {contexto['variable']}"
        )

        lineas.append(
            f"Contexto: {contexto['contexto']}"
        )

        lineas.append(
            f"Número de observaciones: {contexto['n']}"
        )

        lineas.append(
            f"Media: {contexto['media']:.2f}"
        )

        lineas.append(
            f"Mediana: {contexto['mediana']:.2f}"
        )

        lineas.append(
            f"Desviación estándar: {contexto['desviacion']:.2f}"
        )

        lineas.append(
            f"Coeficiente de variación: {contexto['cv']:.2%}"
        )

        lineas.append(
            f"Mínimo: {contexto['minimo']:.2f}"
        )

        lineas.append(
            f"Máximo: {contexto['maximo']:.2f}"
        )

        lineas.append(
            f"Q1: {contexto['q1']:.2f}"
        )

        lineas.append(
            f"Q3: {contexto['q3']:.2f}"
        )

        lineas.append(
            f"Asimetría: {contexto['asimetria']:.3f}"
        )

        lineas.append(
            f"Curtosis: {contexto['curtosis']:.3f}"
        )

        lineas.append(
            f"Prueba de normalidad: {contexto['prueba']}"
        )

        lineas.append(
            f"Valor p: {contexto['pvalor']:.4f}"
        )

        lineas.append(
            f"Distribución aproximadamente normal: {'Sí' if contexto['normal'] else 'No'}"
        )
        

        lineas.append(
            f"Valores atípicos: {'Sí' if contexto['atipicos'] else 'No'}"
        )

        lineas.append("")

        lineas.append(
            "Utiliza lenguaje académico."
        )

        lineas.append(
            "No escribas fórmulas."
        )

        lineas.append(
            "No dejes frases incompletas."
        )

        lineas.append(
            "Concluye siempre con un párrafo final."
        )

        lineas.append(
            "Genera entre 300 y 450 palabras."
        )        

        #-------------------------------------------------
        # GRÁFICAS DISPONIBLES
        #-------------------------------------------------

        if graficas:

            lineas.append("")

            lineas.append(
                "Además de los estadísticos descriptivos recibirás "
                "una o varias gráficas de la variable."
            )

            lineas.append(
                "Integra la información numérica con la información "
                "visual antes de emitir conclusiones."
            )

            lineas.append("")

            lineas.append(
                "Gráficas disponibles:"
            )

            for grafica in graficas:

                lineas.append(

                    f"- {grafica['nombre']}"

                )

            lineas.append("")

            lineas.append(
                "Si observas asimetría, concentración de datos, "
                "multimodalidad, valores atípicos, dispersión, "
                "sesgos o desviaciones respecto de la normalidad, "
                "explícalos relacionando los gráficos con los "
                "estadísticos descriptivos."
            )

        lineas.append("")

        lineas.append(
            "La interpretación deberá incluir:"
        )

        lineas.append(
            "1. Tendencia central."
        )

        lineas.append(
            "2. Dispersión."
        )

        lineas.append(
            "3. Cuartiles."
        )

        lineas.append(
            "4. Asimetría."
        )

        lineas.append(
            "5. Curtosis."
        )

        lineas.append(
            "6. Normalidad."
        )

        if graficas:

            lineas.append(
                "7. Interpretación integrada de las gráficas."
            )

            lineas.append(
                "8. Conclusión."
            )

        else:

            lineas.append(
                "7. Conclusión."
            )

        prompt = "\n".join(lineas)

        return prompt


    #=====================================================
    # ENVIAR CONSULTA
    # CONSULTAR MODELO
    #=====================================================

    def f_consultar(
            self,
            prompt):
        """
        Envía un prompt al proveedor seleccionado.

        Regresa
        -------
        str
            Texto generado por el modelo.
        """

        #---------------------------------------------
        # OLLAMA
        #---------------------------------------------

        if self.proveedor == "ollama":

            respuesta = ollama.chat(

                model=self.modelo,

                messages=[

                    {

                        "role": "user",

                        "content": prompt

                    }

                ],

                options={

                    "temperature": self.temperatura,

                    "num_predict": self.max_tokens

                }

            )

            return respuesta["message"]["content"]


        #---------------------------------------------
        # GROQ
        #---------------------------------------------

        elif self.proveedor == "groq":

            respuesta = self.cliente.chat.completions.create(

                model=self.modelo,

                temperature=self.temperatura,

                max_tokens=self.max_tokens,

                messages=[

                    {

                        "role": "user",

                        "content": prompt

                    }

                ]

            )

            return respuesta.choices[0].message.content


        #---------------------------------------------
        # OTROS
        #---------------------------------------------

        else:

            raise NotImplementedError(

                f"Proveedor '{self.proveedor}' aún no implementado."

            )


    #=====================================================
    # GENERAR INTERPRETACIÓN
    #=====================================================

    def f_generar_interpretacion(
            self,
            contexto,
            graficas=None):
        """
        Genera una interpretación de los
        estadísticos descriptivos.
        """

        prompt = self.f_generar_prompt_interpretacion(

            contexto,
            graficas

        )

        try:

            respuesta = self.f_consultar(

                prompt

            )

            return {

                "prompt": prompt,

                "respuesta": respuesta

            }

        except Exception as e:

            return {

                "prompt": prompt,

                "respuesta":

                    "No fue posible generar la interpretación.\n\n"

                    f"{e}"

            }

    #=====================================================
    # INFORMACIÓN DEL MOTOR
    #=====================================================

    def f_informacion(self):
        """
        Devuelve información del proveedor utilizado.
        """

        return {

            "proveedor": self.proveedor,

            "modelo": self.modelo,

            "temperatura": self.temperatura,

            "max_tokens": self.max_tokens

        }