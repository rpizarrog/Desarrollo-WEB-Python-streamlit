# Sistema Inteligente para Interpretación de Estadísticos Descriptivos
# 📊 App 1 - Estadística Descriptiva con Inteligencia Artificial

**Autor:** Rubén Pizarro Gurrola

Aplicación desarrollada en **Python + Streamlit** para el análisis descriptivo de variables cuantitativas mediante estadísticos descriptivos, representaciones gráficas, un sistema experto basado en reglas y un motor de Inteligencia Artificial.

La aplicación tiene como objetivo apoyar el aprendizaje de la Estadística Descriptiva en estudiantes de educación superior, permitiendo interpretar automáticamente un conjunto de datos desde diferentes enfoques.

---

# Características

La aplicación permite:

- Cargar archivos de datos.
- Seleccionar la variable de estudio.
- Describir el contexto de la variable.
- Calcular estadísticos descriptivos.
- Aplicar pruebas de normalidad.
- Detectar valores atípicos.
- Generar representaciones gráficas.
- Obtener una interpretación mediante reglas estadísticas.
- Obtener una interpretación utilizando Inteligencia Artificial.
- Visualizar el prompt utilizado por la IA para fines educativos.

---

# Estadísticos calculados

Entre otros:

- Número de observaciones
- Media
- Mediana
- Moda
- Varianza
- Desviación estándar
- Coeficiente de variación
- Valor mínimo
- Valor máximo
- Cuartiles
- Rango
- Rango intercuartílico
- Asimetría
- Curtosis

---

# Pruebas estadísticas

Actualmente incorpora:

- Prueba de normalidad de Shapiro-Wilk

La aplicación identifica automáticamente si la distribución puede considerarse aproximadamente normal con base en el valor-p obtenido.

---

# Representaciones gráficas

La aplicación genera automáticamente:

- Histograma
- Diagrama de caja
- QQPlot

Estas representaciones permiten complementar el análisis descriptivo e interpretar visualmente la distribución de los datos.

---

# Sistema Experto

La aplicación incorpora un sistema experto basado en reglas estadísticas que interpreta automáticamente:

- Tendencia central
- Dispersión
- Variabilidad
- Cuartiles
- Asimetría
- Curtosis
- Normalidad
- Valores atípicos

Las reglas fueron diseñadas específicamente para apoyar el aprendizaje de la Estadística Descriptiva.

---

# Inteligencia Artificial

La aplicación integra un motor de IA denominado **MotorIA**, preparado para trabajar con distintos proveedores.

Actualmente soporta:

- Ollama
- Groq

La arquitectura también fue diseñada para incorporar posteriormente:

- OpenAI
- Gemini

---

# Prompt IA

Como apoyo al aprendizaje, la aplicación permite visualizar el prompt construido automáticamente antes de enviarlo al modelo de lenguaje.

Esto permite al estudiante:

- Comprender cómo se comunica la aplicación con la IA.
- Copiar el prompt.
- Modificarlo.
- Utilizarlo en otros modelos como ChatGPT, Gemini o Claude.

---

# Arquitectura

La aplicación fue desarrollada utilizando Programación Orientada a Objetos.

Principales clases:

- CEventos
- CEstadisticos
- CInterpretador
- CMotorIA

Cada clase tiene una responsabilidad específica, facilitando el mantenimiento y la evolución del proyecto.

---

# Tecnologías utilizadas

- Python
- Streamlit
- Pandas
- NumPy
- SciPy
- Matplotlib
- Seaborn
- Ollama
- Groq

---

# Objetivo educativo

Esta aplicación no pretende sustituir el análisis realizado por un especialista.

Su propósito es apoyar el aprendizaje de la interpretación estadística mediante la integración de:

- Estadísticos descriptivos
- Representaciones gráficas
- Sistema experto
- Inteligencia Artificial

permitiendo que el estudiante compare diferentes formas de interpretar un mismo conjunto de datos.

---

# Próximas versiones

Entre las mejoras planeadas se encuentran:

- Interpretación automática de gráficas mediante modelos multimodales.
- Incorporación de nuevos proveedores de IA.
- Evaluación automática de interpretaciones elaboradas por estudiantes.
- Generación automática de preguntas.
- Retroalimentación personalizada.
- Exportación de reportes.
- Integración con futuras aplicaciones del proyecto.

---

# Licencia

Proyecto académico desarrollado con fines educativos.

Autor:

**Rubén Pizarro Gurrola**

Instituto Tecnológico de Durango

Tecnológico Nacional de México
