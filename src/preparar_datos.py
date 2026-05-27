import pandas as pd


# ============================================================
# PREPARACIÓN Y LIMPIEZA DE DATOS
# ============================================================
# Este archivo toma la tabla Home/Away de FBref y la convierte
# en una tabla limpia, con nombres de columnas simples.
#
# Luego calcula variables derivadas necesarias para el análisis:
# - puntos por partido de local
# - puntos por partido de visitante
# - diferencia de puntos local - visitante
# - goles por partido de local
# - goles por partido de visitante
# - eficacia local
# - porcentajes de victorias, empates y derrotas
# ============================================================


def seleccionar_tabla_home_away(tablas):
    """
    Selecciona automáticamente la tabla Home/Away de FBref.

    En el HTML descargado, la tabla correcta es la que contiene columnas
    de rendimiento local y visitante.
    """

    for tabla in tablas:
        columnas = tabla.columns

        if isinstance(columnas, pd.MultiIndex):
            columnas_texto = [f"{a}_{b}" for a, b in columnas]

            tiene_home = any("Home" in col for col in columnas_texto)
            tiene_away = any("Away" in col for col in columnas_texto)
            tiene_pts = any("Pts" in col for col in columnas_texto)

            if tiene_home and tiene_away and tiene_pts:
                return tabla

    raise ValueError("No se encontró la tabla Home/Away en el archivo HTML.")


def limpiar_tabla_home_away(tabla):
    """
    Limpia la tabla Home/Away.

    FBref trae columnas con doble encabezado, por ejemplo:
    ('Home', 'MP'), ('Home', 'W'), ('Away', 'Pts').

    Esta función las convierte en nombres simples:
    Home_MP, Home_W, Away_Pts, etc.
    """

    df = tabla.copy()

    if isinstance(df.columns, pd.MultiIndex):
        nuevas_columnas = []

        for nivel_1, nivel_2 in df.columns:
            if "Unnamed" in str(nivel_1):
                nuevas_columnas.append(str(nivel_2))
            else:
                nuevas_columnas.append(f"{nivel_1}_{nivel_2}")

        df.columns = nuevas_columnas

    # Renombramos Squad a Equipo para trabajar en español
    df = df.rename(columns={"Squad": "Equipo"})

    # Eliminamos columnas que no necesitamos para el análisis
    columnas_necesarias = [
        "Equipo",
        "Home_MP", "Home_W", "Home_D", "Home_L", "Home_GF", "Home_GA", "Home_GD", "Home_Pts", "Home_Pts/MP",
        "Away_MP", "Away_W", "Away_D", "Away_L", "Away_GF", "Away_GA", "Away_GD", "Away_Pts", "Away_Pts/MP",
    ]

    df = df[columnas_necesarias]

    # Convertimos columnas numéricas
    columnas_numericas = [col for col in df.columns if col != "Equipo"]

    for col in columnas_numericas:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


def agregar_variables_derivadas(df):
    """
    Agrega variables calculadas a partir de los datos reales.

    Estas variables son las que después vamos a usar para gráficos,
    intervalos de confianza, pruebas de hipótesis y conclusiones.
    """

    df = df.copy()

    # Puntos por partido
    df["Pts_PJ_Local"] = df["Home_Pts"] / df["Home_MP"]
    df["Pts_PJ_Visitante"] = df["Away_Pts"] / df["Away_MP"]

    # Diferencia principal del proyecto
    df["Delta_Pts_PJ"] = df["Pts_PJ_Local"] - df["Pts_PJ_Visitante"]

    # Goles por partido
    df["GF_PJ_Local"] = df["Home_GF"] / df["Home_MP"]
    df["GF_PJ_Visitante"] = df["Away_GF"] / df["Away_MP"]
    df["Delta_GF_PJ"] = df["GF_PJ_Local"] - df["GF_PJ_Visitante"]

    # Eficacia de localía
    df["Eficacia_Local_%"] = (df["Home_Pts"] / (3 * df["Home_MP"])) * 100
    df["Eficacia_Visitante_%"] = (df["Away_Pts"] / (3 * df["Away_MP"])) * 100

    # Porcentajes de resultados
    df["Pct_Victorias_Local"] = (df["Home_W"] / df["Home_MP"]) * 100
    df["Pct_Empates_Local"] = (df["Home_D"] / df["Home_MP"]) * 100
    df["Pct_Derrotas_Local"] = (df["Home_L"] / df["Home_MP"]) * 100

    df["Pct_Victorias_Visitante"] = (df["Away_W"] / df["Away_MP"]) * 100
    df["Pct_Empates_Visitante"] = (df["Away_D"] / df["Away_MP"]) * 100
    df["Pct_Derrotas_Visitante"] = (df["Away_L"] / df["Away_MP"]) * 100

    return df


def preparar_base_limpia(tablas):
    """
    Función general que:
    1. Selecciona la tabla Home/Away.
    2. Limpia sus columnas.
    3. Agrega variables derivadas.
    """

    tabla_home_away = seleccionar_tabla_home_away(tablas)
    df_limpio = limpiar_tabla_home_away(tabla_home_away)
    df_final = agregar_variables_derivadas(df_limpio)

    return df_final
