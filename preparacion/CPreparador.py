#=========================================================
# ARCHIVO
# CPreparador.py
#
# AUTOR
# Rubén Pizarro Gurrola
#
# FECHA
# Agosto 2026
#
# DESCRIPCIÓN
#
# Script independiente para limpiar archivos CSV.
#
# Caso de estudio:
#
# Muebleria.csv
#
#=========================================================

import pandas as pd

import numpy as np

import streamlit as st

from pathlib import Path


#=========================================================
# CLASE
#=========================================================

class Preparador:


    #=====================================================
    # CONSTRUCTOR
    #=====================================================

    def __init__(self):

        pass


    #=====================================================
    # CARGAR DATOS
    #=====================================================

    def f_cargar_datos(
            self,
            archivo):

        nombre = archivo.name.lower()

        if nombre.endswith(".csv"):

            try:

                datos = pd.read_csv(
                    archivo,
                    encoding="utf-8"
                )

            except:

                datos = pd.read_csv(
                    archivo,
                    encoding="latin1"
                )

        elif nombre.endswith(".xlsx"):

            datos = pd.read_excel(
                archivo,
                engine="openpyxl"
            )

        elif nombre.endswith(".xls"):

            datos = pd.read_excel(
                archivo
            )

        else:

            raise ValueError(
                "Formato no soportado."
            )

        return datos
    
    #=====================================================
    # LIMPIAR ENCABEZADOS
    #=====================================================

    def f_limpiar_encabezados(
            self,
            datos):

        datos = datos.copy()

        datos.columns = (

            datos.columns

                .astype(str)

                .str.strip()

                .str.replace(

                    r"\s+",

                    "_",

                    regex=True

                )

        )

        return datos

    #=====================================================
    # CONVERTIR COLUMNAS MONETARIAS
    #=====================================================
    def f_convertir_columnas_monetarias(self, datos):

        datos = datos.copy()

        for columna in datos.columns:

            texto = datos[columna].astype(str)

            if texto.str.contains(r"\$", na=False).any():

                datos[columna] = (
                    texto
                        .str.replace("$", "", regex=False)
                        .str.replace(",", "", regex=False)
                )

                datos[columna] = pd.to_numeric(
                    datos[columna],
                    errors="coerce"
                )

            # Tomar una muestra de valores no vacíos
            muestra = texto[texto != ""].head(20)

            if len(muestra) == 0:
                continue

            # ¿La mayoría comienza con $?
            porcentaje = muestra.str.startswith("$").mean()

            if porcentaje >= 0.80:

                datos[columna] = (
                    texto
                        .str.replace("$", "", regex=False)
                        .str.replace(",", "", regex=False)
                )

                datos[columna] = pd.to_numeric(
                    datos[columna],
                    errors="coerce"
                )

        return datos

    #=====================================================
    # CONVERTIR FECHAS
    #=====================================================

    def f_convertir_fechas(
            self,
            datos):

        datos = datos.copy()

        for columna in datos.columns:

            if datos[columna].dtype != object:

                continue

            convertido = pd.to_datetime(

                datos[columna],

                dayfirst=True,

                errors="coerce"

            )

            porcentaje = convertido.notna().mean()

            if porcentaje > 0.80:

                print(f"Convirtiendo fecha: {columna}")

                datos[columna] = convertido

        return datos


    #=====================================================
    # RESUMEN
    #=====================================================

    def f_resumen(
            self,
            datos):

        print("\n")

        print("="*70)

        print("COLUMNAS")

        print("="*70)

        print(datos.columns.tolist())

        print("\n")

        print("="*70)

        print("TIPOS")

        print("="*70)

        print(datos.dtypes)

        print("\n")

        print("="*70)

        print("PRIMEROS REGISTROS")

        print("="*70)

        print(datos.head())


    #=====================================================
    # GUARDAR
    #=====================================================


    def f_guardar(
            self,
            datos,
            archivo):

        nombre = Path(archivo.name)

        nombre_salida = f"{nombre.stem}_limpio.csv"

        csv = datos.to_csv(

            index=False,

            encoding="utf-8-sig"

        )

        return csv, nombre_salida

    #=====================================================
    # PREPARAR DATOS
    #=====================================================

    def f_preparar_datos(
            self,
            datos):
        """
        Prepara un DataFrame.

        Se utiliza desde Streamlit.
        """

        datos1 = self.f_limpiar_encabezados(datos)

        # st.write("Después de limpiar encabezados")
        # st.write(datos1.columns.tolist())

        datos2 = self.f_convertir_columnas_monetarias(datos1)

        # st.write("Después de convertir moneda")
        # st.write(datos2["Precio"].head())

        datos3 = self.f_convertir_fechas(datos2)

        # st.write("Después de convertir fechas")
        # st.write(datos3.head())

        return datos3



    # Preparar el archivo de salida
    def f_preparar_archivo(
            self,
            archivo_entrada,
            archivo_salida):

        datos = self.f_cargar_datos(archivo_entrada)

        print("\nANTES")
        self.f_resumen(datos)

        datos = self.f_preparar_datos(datos)

        print("\nDESPUÉS")
        self.f_resumen(datos)

        self.f_guardar(datos, archivo_salida)


#=========================================================
# PRINCIPAL
#=========================================================

if __name__ == "__main__":

    preparador = Preparador()

    preparador.f_preparar(

        "datos/Muebleria.csv",

        "datos/Muebleria_limpio_desdeAPP.csv"

    )