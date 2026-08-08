# 🧹 Preparación de Datos

Aplicación desarrollada con **Python** y **Streamlit** para preparar conjuntos de datos antes de realizar análisis estadísticos o de aprendizaje automático.

El objetivo es automatizar las tareas más comunes de limpieza y transformación de datos, permitiendo obtener archivos listos para su análisis.

---

## Características

La aplicación permite:

- 📂 Cargar archivos **CSV** y **Excel (.xlsx)**.
- 👀 Visualizar el conjunto de datos original.
- 🧹 Limpiar encabezados de columnas.
- 💲 Convertir columnas monetarias a variables numéricas.
- 📅 Convertir columnas con fechas.
- 📥 Descargar un nuevo archivo limpio con el nombre:

```
NombreArchivo_limpio.csv
```

Por ejemplo:

```
Muebleria.csv
```

se descarga como

```
Muebleria_limpio.csv
```

---

## Tecnologías

- Python 3.12+
- Streamlit
- Pandas
- NumPy
- OpenPyXL

---

## Instalación

Clonar el repositorio

```bash
git clone https://github.com/USUARIO/preparacion.git
```

Entrar a la carpeta

```bash
cd preparacion
```

Crear entorno virtual

Windows

```bash
python -m venv .venv
```

Activar

```bash
.venv\Scripts\activate
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecutar la aplicación

```bash
streamlit run app_preparacion.py
```

---

## Funcionalidades implementadas

### Carga de datos

- CSV
- Excel (.xlsx)

### Preparación

- Limpieza de encabezados
- Eliminación de espacios
- Sustitución de espacios por "_"
- Conversión de columnas monetarias
- Conversión de fechas

### Salida

- Visualización de los datos preparados
- Descarga del archivo limpio

---

## Estructura del proyecto

```
preparacion/

│
├── app_preparacion.py
├── CPreparador.py
├── requirements.txt
├── README.md
└── datos/
```

---

## Ejemplo de uso

1. Seleccionar un archivo CSV o Excel.
2. Visualizar los datos originales.
3. Presionar **Preparar datos**.
4. Revisar el resultado.
5. Descargar el archivo limpio.

---

## Próximas funcionalidades

Se tiene previsto incorporar:

- Eliminación de filas duplicadas.
- Tratamiento de valores faltantes.
- Tratamiento de datos atipicos
- Conversión automática de variables categóricas.
- Conversión de variables lógicas (Sí/No, True/False).
- Conversión automática de porcentajes.
- Conversión automática de separadores decimales.
- Reporte de las transformaciones realizadas.
- Detección automática de tipos de datos.
- Escalamiento de datos
- Estandarizacion de datos

---

## Autor

**Rubén Pizarro Gurrola**

Instituto Tecnológico de Durango

Tecnológico Nacional de México

2026