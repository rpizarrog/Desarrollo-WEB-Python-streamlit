# Machine Learning Studio
# Regresión Bivariada con Python

Aplicación Web desarrollada en **Python** y **Streamlit** para construir, evaluar e interpretar modelos de **Regresión Bivariada** mediante técnicas de **Machine Learning**, **Estadística** y **Sistemas Expertos**.

La aplicación permite construir diferentes tipos de modelos de regresión, evaluar su desempeño mediante indicadores estadísticos, verificar los principales supuestos del modelo y generar interpretaciones automáticas utilizando un **Sistema Experto** y **Modelos de Inteligencia Artificial**.

---

# Autor

**Rubén Pizarro Gurrola**

Instituto Tecnológico de Durango

México

---

# Características

La aplicación incorpora las siguientes funcionalidades:

- Carga de archivos CSV y Excel.
- Selección de variables independientes y dependientes.
- Construcción automática de modelos de regresión.
- Visualización gráfica del modelo ajustado.
- Obtención de la ecuación matemática.
- Interpretación de coeficientes.
- Evaluación del modelo mediante indicadores estadísticos.
- Verificación de supuestos de regresión.
- Interpretación mediante Sistema Experto.
- Interpretación mediante Inteligencia Artificial.
- Generación automática de reportes.

---

# Modelos de Regresión Disponibles

Actualmente se encuentran implementados los siguientes modelos:

- Regresión Lineal
- Regresión Polinomial
- Regresión Exponencial
- Regresión Logarítmica
- Regresión Potencial

---

# Indicadores de Evaluación

La aplicación calcula automáticamente:

- Coeficiente de Determinación (R²)
- R² Ajustado
- Error Cuadrático Medio (MSE)
- Raíz del Error Cuadrático Medio (RMSE)
- Error Absoluto Medio (MAE)
- Error Porcentual Absoluto Medio (MAPE)
- Criterio de Información de Akaike (AIC)
- Criterio de Información Bayesiano (BIC)

---

# Verificación de Supuestos

La aplicación permite verificar los principales supuestos de un modelo de regresión mediante:

- Ramsey RESET (Adecuación de la forma funcional)
- Shapiro-Wilk (Normalidad)
- Breusch-Pagan (Homocedasticidad)
- Durbin-Watson (Independencia de residuos)

---

# Sistema Experto

La aplicación incorpora un Sistema Experto desarrollado específicamente para interpretar modelos de regresión.

Entre otras funciones interpreta:

- Tipo de modelo
- Ecuación matemática
- Coeficientes
- Calidad del ajuste
- Métricas de evaluación
- Supuestos del modelo
- Conclusiones

---

# Inteligencia Artificial

La aplicación puede conectarse a diferentes proveedores de IA para enriquecer la interpretación estadística.

Actualmente se encuentra implementada la integración con:

- Groq

Modelos compatibles:

- openai/gpt-oss-120b
- qwen/qwen3.6-27b
- groq/compound
- groq/compound-mini

Próximamente:

- Ollama
- OpenAI

---

# Tecnologías utilizadas

- Python
- Streamlit
- Pandas
- NumPy
- SciPy
- Scikit-learn
- Statsmodels
- Matplotlib
- Groq API
- python-docx

---

# Instalación

Crear un entorno virtual

```bash
python -m venv .venv
```

Activar el entorno

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Ejecución

```bash
streamlit run app_regresion.py
```

---

# Estructura del Proyecto

```
regresion_bivariada/

│
├── app_regresion.py
│
├── CEventos.py
├── CEstadisticos.py
├── CRegresion.py
├── CInterpretador.py
├── CMotorIA.py
├── CProyecto.py
│
├── requirements.txt
├── README.md
│
└── datos/
```

---

# Aplicaciones futuras

Este proyecto forma parte de **Machine Learning Studio**, una colección de aplicaciones académicas para el aprendizaje de Machine Learning.

Entre las aplicaciones planeadas se encuentran:

- Estadística Descriptiva
- Regresión Bivariada
- Regresión Múltiple
- Clasificación
- Clustering
- Reducción de Dimensionalidad
- Series de Tiempo
- Redes Neuronales

---

# Licencia

Proyecto desarrollado con fines académicos y de investigación.

© Rubén Pizarro Gurrola