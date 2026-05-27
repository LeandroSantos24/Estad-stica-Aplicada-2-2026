import pandas as pd

from src.config import HTML_FBREF, VALORES_PLANTILLA


# ============================================================
# CARGA DE DATOS
# ============================================================
# En este archivo se leen las fuentes originales del proyecto.
#
# Fuente principal:
# - HTML descargado desde FBref con la tabla Home/Away
#   de la Liga Profesional Argentina 2023.
#
# Fuente complementaria:
# - CSV con valores de plantilla 2023.
#
# El objetivo de separar esta parte es que, si en el futuro
# cambia la fuente de datos, solamente tengamos que tocar este archivo.
# ============================================================


def verificar_archivos():
    """
    Verifica que existan los archivos necesarios para ejecutar el proyecto.
    Si falta alguno, muestra un error claro.
    """

    if not HTML_FBREF.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo HTML de FBref:\n{HTML_FBREF}\n\n"
            "Solución: guardá el archivo de FBref dentro de la carpeta datos/ "
            "con el nombre fbref_lpf_2023.html"
        )

    if not VALORES_PLANTILLA.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo de valores de plantilla:\n{VALORES_PLANTILLA}\n\n"
            "Solución: creá el archivo datos/valores_plantilla_2023.csv"
        )


def cargar_tablas_fbref():
    """
    Lee todas las tablas disponibles dentro del archivo HTML de FBref.

    pandas.read_html() busca automáticamente todas las tablas HTML
    y las devuelve como una lista de DataFrames.
    """

    verificar_archivos()

    tablas = pd.read_html(HTML_FBREF)

    print("\nTABLAS ENCONTRADAS EN EL HTML DE FBREF")
    print("--------------------------------------")
    print(f"Cantidad de tablas encontradas: {len(tablas)}")

    for i, tabla in enumerate(tablas):
        print(f"\nTabla {i}")
        print(f"Filas: {tabla.shape[0]} | Columnas: {tabla.shape[1]}")
        print("Columnas:")
        print(list(tabla.columns))

    return tablas


def cargar_valores_plantilla():
    """
    Lee el archivo CSV con valores de mercado de plantillas 2023.

    Este archivo se usará más adelante para analizar si el valor económico
    del plantel se relaciona con el rendimiento de local.
    """

    verificar_archivos()

    df_valores = pd.read_csv(VALORES_PLANTILLA)

    print("\nARCHIVO DE VALORES DE PLANTILLA")
    print("--------------------------------")
    print(df_valores.head())

    return df_valores

