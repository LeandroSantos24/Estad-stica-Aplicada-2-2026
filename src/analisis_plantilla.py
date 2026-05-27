import re

import numpy as np
import pandas as pd
from scipy import stats

from src.config import HTML_TRANSFERMARKT


# ============================================================
# ANÁLISIS DE VALOR DE PLANTILLA
# ============================================================
# Este archivo agrega una nueva dimensión al proyecto:
# el valor económico de cada plantel.
#
# Objetivo:
# analizar si existe relación entre el valor de mercado del equipo
# y su rendimiento como local o su ventaja de localía.
# ============================================================


def normalizar_nombre_equipo(nombre):
    """
    Normaliza nombres de equipos para poder unir FBref con Transfermarkt.

    FBref y Transfermarkt no siempre escriben igual los clubes.
    Por ejemplo:
    - Talleres–C vs CA Talleres
    - Estudiantes–LP vs Club Estudiantes de La Plata
    - Cen. Córdoba–SdE vs Central Córdoba SdE
    """

    if pd.isna(nombre):
        return nombre

    nombre = str(nombre).strip()

    reemplazos = {
        "CA River Plate": "River Plate",
        "River Plate": "River Plate",

        "CA Boca Juniors": "Boca Juniors",
        "Boca Juniors": "Boca Juniors",

        "Racing Club": "Racing Club",

        "CA Vélez Sarsfield": "Vélez Sarsfield",
        "Vélez Sarsfield": "Vélez Sarsfield",

        "CA Colón": "Colón",
        "Colón": "Colón",

        "CA Lanús": "Lanús",
        "Lanús": "Lanús",

        "CA Talleres": "Talleres–C",
        "Talleres": "Talleres–C",
        "Talleres de Córdoba": "Talleres–C",

        "Club Estudiantes de La Plata": "Estudiantes–LP",
        "Estudiantes de La Plata": "Estudiantes–LP",
        "Estudiantes": "Estudiantes–LP",

        "CA San Lorenzo de Almagro": "San Lorenzo",
        "San Lorenzo de Almagro": "San Lorenzo",
        "San Lorenzo": "San Lorenzo",

        "CA Tigre": "Tigre",
        "Tigre": "Tigre",

        "CA Huracán": "Huracán",
        "Huracán": "Huracán",

        "CA Banfield": "Banfield",
        "Banfield": "Banfield",

        "CA Newell's Old Boys": "Newell's Old Boys",
        "Newell's Old Boys": "Newell's Old Boys",
        "Newells Old Boys": "Newell's Old Boys",

        "CA Rosario Central": "Rosario Central",
        "Rosario Central": "Rosario Central",

        "CA Independiente": "Independiente",
        "Independiente": "Independiente",

        "Defensa y Justicia": "Defensa y Justicia",

        "AA Argentinos Juniors": "Arg Juniors",
        "Argentinos Juniors": "Arg Juniors",
        "Arg Juniors": "Arg Juniors",

        "Sarmiento (Junín)": "Sarmiento–J",
        "CA Sarmiento": "Sarmiento–J",
        "Sarmiento": "Sarmiento–J",
        "Sarmiento Junin": "Sarmiento–J",

        "Instituto AC Córdoba": "Instituto",
        "Instituto AC Cordoba": "Instituto",
        "Instituto": "Instituto",

        "CA Platense": "Platense",
        "Platense": "Platense",

        "Atlético Tucumán": "Atlé Tucumán",
        "Atletico Tucumán": "Atlé Tucumán",
        "Atletico Tucuman": "Atlé Tucumán",
        "CA Tucumán": "Atlé Tucumán",
        "Atlético de Tucumán": "Atlé Tucumán",

        "Barracas Central": "Barracas Central",

        "Arsenal FC": "Arsenal",
        "Arsenal de Sarandí": "Arsenal",
        "Arsenal de Sarandi": "Arsenal",
        "Arsenal": "Arsenal",

        "Gimnasia y Esgrima La Plata": "Gimnasia–LP",
        "Gimnasia La Plata": "Gimnasia–LP",
        "Gimnasia y Esgrima": "Gimnasia–LP",

        "Unión de Santa Fe": "Unión",
        "Union de Santa Fe": "Unión",
        "CA Unión": "Unión",
        "CA Union": "Unión",
        "Unión": "Unión",
        "Union": "Unión",

        "CA Belgrano": "Belgrano",
        "Belgrano": "Belgrano",

        "Central Córdoba SdE": "Cen. Córdoba–SdE",
        "Central Córdoba": "Cen. Córdoba–SdE",
        "Central Cordoba SdE": "Cen. Córdoba–SdE",
        "Central Cordoba": "Cen. Córdoba–SdE",

        "Godoy Cruz Antonio Tomba": "Godoy Cruz",
        "Godoy Cruz": "Godoy Cruz",

        "CSD Defensa y Justicia": "Defensa y Justicia",
        "Club Atlético Tucumán": "Atlé Tucumán",
        "CA Unión (Santa Fe)": "Unión",
        "CA Central Córdoba (SdE)": "Cen. Córdoba–SdE",
        "Club de Gimnasia y Esgrima La Plata": "Gimnasia–LP",
        "Instituto ACC": "Instituto",
        "CD Godoy Cruz Antonio Tomba": "Godoy Cruz",
        "CA Barracas Central": "Barracas Central",
        "CA Sarmiento (Junín)": "Sarmiento–J",
    }

    return reemplazos.get(nombre, nombre)


def convertir_valor_mercado(valor):
    """
    Convierte valores de Transfermarkt a millones de euros.

    Ejemplos:
    - "134,85 mill. €" -> 134.85
    - "850 mil €" -> 0.85
    """

    if pd.isna(valor):
        return np.nan

    texto = str(valor).strip().lower()

    texto = texto.replace("€", "")
    texto = texto.replace(" ", "")
    texto = texto.replace(",", ".")

    numero = re.findall(r"\d+\.?\d*", texto)

    if not numero:
        return np.nan

    numero = float(numero[0])

    if "mil" in texto and "mill" not in texto:
        return numero / 1000

    return numero


def cargar_tabla_transfermarkt():
    """
    Lee el HTML de Transfermarkt y busca la tabla de clubes.

    La tabla correcta detectada en nuestro HTML tiene columnas:
    ['Club', 'Club.1', 'name', 'Equipo', 'Edad', 'Extranjeros',
     'Valor de mercado medio', 'Valor de mercado total']
    """

    if not HTML_TRANSFERMARKT.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo de Transfermarkt:\n{HTML_TRANSFERMARKT}\n\n"
            "Solución: guardá la página en datos/transfermarkt_lpf_2023.html"
        )

    tablas = pd.read_html(HTML_TRANSFERMARKT)

    print("\nTABLAS ENCONTRADAS EN TRANSFERMARKT")
    print("-----------------------------------")
    print(f"Cantidad de tablas encontradas: {len(tablas)}")

    for i, tabla in enumerate(tablas):
        print(f"Tabla {i}: filas={tabla.shape[0]} columnas={tabla.shape[1]}")
        print(list(tabla.columns))

    for tabla in tablas:
        columnas = [str(c) for c in tabla.columns]

        tiene_valor_total = any("Valor de mercado total" in col for col in columnas)
        tiene_name = any(col == "name" for col in columnas)

        if tiene_valor_total and tiene_name:
            return tabla

    raise ValueError(
        "No se encontró la tabla de clubes con valor de mercado total. "
        "Revisar si se guardó la página correcta de Transfermarkt."
    )


def preparar_valores_plantilla():
    """
    Limpia la tabla de Transfermarkt y deja:
    - Equipo
    - ValorPlantillaM

    En el HTML guardado, Transfermarkt quedó con columnas desplazadas:
    - 'Club.1' contiene el nombre real del club.
    - 'Valor de mercado medio' contiene el valor total de mercado.
    """

    tabla = cargar_tabla_transfermarkt()

    df = tabla.copy()

    if "Club.1" not in df.columns:
        raise ValueError(
            "No se encontró la columna 'Club.1' en la tabla de Transfermarkt."
        )

    if "Valor de mercado medio" not in df.columns:
        raise ValueError(
            "No se encontró la columna 'Valor de mercado medio' en la tabla de Transfermarkt."
        )

    df = df[["Club.1", "Valor de mercado medio"]].copy()

    df.columns = ["Equipo_Transfermarkt", "ValorPlantillaTexto"]

    df["Equipo_Transfermarkt"] = df["Equipo_Transfermarkt"].astype(str)

    df["Equipo"] = df["Equipo_Transfermarkt"].apply(normalizar_nombre_equipo)
    df["ValorPlantillaM"] = df["ValorPlantillaTexto"].apply(convertir_valor_mercado)

    df = df[
        [
            "Equipo",
            "Equipo_Transfermarkt",
            "ValorPlantillaTexto",
            "ValorPlantillaM",
        ]
    ]

    df = df.dropna(subset=["ValorPlantillaM"])

    # Quitamos la fila total de Transfermarkt
    df = df[df["Equipo_Transfermarkt"] != "nan"]
    df = df[df["Equipo_Transfermarkt"].str.lower() != "nan"]

    # Quitamos duplicados si los hubiera
    df = df.drop_duplicates(subset=["Equipo"])

    print("\nVALORES DE PLANTILLA LIMPIOS")
    print("----------------------------")
    print(df)

    return df


def unir_localia_con_plantilla(df_localia):
    """
    Une la base de localía de FBref con los valores de plantilla de Transfermarkt.
    """

    df_valores = preparar_valores_plantilla()

    df_localia = df_localia.copy()
    df_valores = df_valores.copy()

    # Aseguramos que ambas columnas de unión sean texto
    df_localia["Equipo"] = df_localia["Equipo"].astype(str)
    df_valores["Equipo"] = df_valores["Equipo"].astype(str)

    df = df_localia.merge(
        df_valores,
        on="Equipo",
        how="left"
    )

    faltantes = df[df["ValorPlantillaM"].isna()]["Equipo"].tolist()

    if faltantes:
        print("\nATENCIÓN: equipos sin valor de plantilla después de unir:")
        for equipo in faltantes:
            print(f"- {equipo}")
    else:
        print("\nTodos los equipos fueron unidos correctamente con Transfermarkt.")

    return df


def asignar_grupos_economicos(df):
    """
    Crea grupos económicos Alto, Medio y Bajo según terciles del valor de plantilla.

    Terciles:
    - Bajo: tercio inferior de valores.
    - Medio: tercio central.
    - Alto: tercio superior.
    """

    df = df.copy()

    df_validos = df.dropna(subset=["ValorPlantillaM"]).copy()

    df_validos["GrupoEconomico"] = pd.qcut(
        df_validos["ValorPlantillaM"],
        q=3,
        labels=["Bajo", "Medio", "Alto"]
    )

    df = df.merge(
        df_validos[["Equipo", "GrupoEconomico"]],
        on="Equipo",
        how="left"
    )

    return df


def correlaciones_plantilla(df):
    """
    Calcula correlaciones entre valor de plantilla y variables de localía.

    Pearson mide relación lineal.
    Spearman mide relación monotónica por rangos.
    """

    variables = [
        "Pts_PJ_Local",
        "Pts_PJ_Visitante",
        "Delta_Pts_PJ",
        "GF_PJ_Local",
        "Delta_GF_PJ",
        "Eficacia_Local_%",
    ]

    resultados = []

    for variable in variables:
        datos = df[["ValorPlantillaM", variable]].dropna()

        if len(datos) < 3:
            resultados.append({
                "Variable": variable,
                "Pearson_r": np.nan,
                "Pearson_p": np.nan,
                "Spearman_rho": np.nan,
                "Spearman_p": np.nan,
            })
            continue

        pearson = stats.pearsonr(datos["ValorPlantillaM"], datos[variable])
        spearman = stats.spearmanr(datos["ValorPlantillaM"], datos[variable])

        resultados.append({
            "Variable": variable,
            "Pearson_r": pearson.statistic,
            "Pearson_p": pearson.pvalue,
            "Spearman_rho": spearman.statistic,
            "Spearman_p": spearman.pvalue,
        })

    return pd.DataFrame(resultados)


def regresion_simple_plantilla(df, variable_objetivo="Delta_Pts_PJ"):
    """
    Regresión simple:

    variable_objetivo = b0 + b1 * ValorPlantillaM

    Por defecto analiza si el valor de plantilla explica la ventaja de localía.
    """

    datos = df[["ValorPlantillaM", variable_objetivo]].dropna()

    if len(datos) < 3:
        return {
            "VariableObjetivo": variable_objetivo,
            "Intercepto": np.nan,
            "Pendiente": np.nan,
            "R": np.nan,
            "R2": np.nan,
            "p_valor": np.nan,
            "ErrorEstandarPendiente": np.nan,
        }

    x = datos["ValorPlantillaM"]
    y = datos[variable_objetivo]

    modelo = stats.linregress(x, y)

    return {
        "VariableObjetivo": variable_objetivo,
        "Intercepto": modelo.intercept,
        "Pendiente": modelo.slope,
        "R": modelo.rvalue,
        "R2": modelo.rvalue ** 2,
        "p_valor": modelo.pvalue,
        "ErrorEstandarPendiente": modelo.stderr,
    }


def resumen_por_grupo_economico(df):
    """
    Resume el rendimiento de localía según grupo económico.
    """

    resumen = df.dropna(subset=["GrupoEconomico"]).groupby(
        "GrupoEconomico",
        observed=True
    ).agg(
        Equipos=("Equipo", "count"),
        ValorPromedioM=("ValorPlantillaM", "mean"),
        PtsLocalPromedio=("Pts_PJ_Local", "mean"),
        PtsVisitantePromedio=("Pts_PJ_Visitante", "mean"),
        DeltaPtsPromedio=("Delta_Pts_PJ", "mean"),
        GolesLocalPromedio=("GF_PJ_Local", "mean"),
        EficaciaLocalPromedio=("Eficacia_Local_%", "mean"),
    ).reset_index()

    return resumen


def prueba_anova_grupos(df):
    """
    Compara la ventaja de localía entre grupos económicos usando ANOVA.

    H0: las medias de Delta_Pts_PJ son iguales entre grupos.
    H1: al menos un grupo tiene media distinta.
    """

    grupos = []

    for _, grupo in df.dropna(subset=["GrupoEconomico"]).groupby(
        "GrupoEconomico",
        observed=True
    ):
        valores = grupo["Delta_Pts_PJ"].dropna()

        if len(valores) > 0:
            grupos.append(valores)

    if len(grupos) < 2:
        return {
            "prueba": "ANOVA Delta_Pts_PJ por GrupoEconomico",
            "F": np.nan,
            "p_valor": np.nan,
            "decision": "No se puede calcular",
        }

    f_stat, p_valor = stats.f_oneway(*grupos)

    return {
        "prueba": "ANOVA Delta_Pts_PJ por GrupoEconomico",
        "F": f_stat,
        "p_valor": p_valor,
        "decision": "Rechazar H0" if p_valor < 0.05 else "No rechazar H0",
    }


def prueba_kruskal_grupos(df):
    """
    Prueba no paramétrica de Kruskal-Wallis entre grupos económicos.

    H0: las distribuciones de Delta_Pts_PJ son iguales entre grupos.
    H1: al menos un grupo difiere.
    """

    grupos = []

    for _, grupo in df.dropna(subset=["GrupoEconomico"]).groupby(
        "GrupoEconomico",
        observed=True
    ):
        valores = grupo["Delta_Pts_PJ"].dropna()

        if len(valores) > 0:
            grupos.append(valores)

    if len(grupos) < 2:
        return {
            "prueba": "Kruskal-Wallis Delta_Pts_PJ por GrupoEconomico",
            "H": np.nan,
            "p_valor": np.nan,
            "decision": "No se puede calcular",
        }

    h_stat, p_valor = stats.kruskal(*grupos)

    return {
        "prueba": "Kruskal-Wallis Delta_Pts_PJ por GrupoEconomico",
        "H": h_stat,
        "p_valor": p_valor,
        "decision": "Rechazar H0" if p_valor < 0.05 else "No rechazar H0",
    }


def ejecutar_analisis_plantilla(df_localia):
    """
    Ejecuta todo el análisis económico.

    Devuelve:
    - df unido con valor de plantilla
    - tabla de correlaciones
    - resumen por grupos económicos
    - resultados de regresión y pruebas por grupos
    """

    df = unir_localia_con_plantilla(df_localia)
    df = asignar_grupos_economicos(df)

    correlaciones = correlaciones_plantilla(df)

    regresion_delta = regresion_simple_plantilla(df, "Delta_Pts_PJ")
    regresion_local = regresion_simple_plantilla(df, "Pts_PJ_Local")

    resumen_grupos = resumen_por_grupo_economico(df)

    anova = prueba_anova_grupos(df)
    kruskal = prueba_kruskal_grupos(df)

    resultados = {
        "regresion_delta": regresion_delta,
        "regresion_local": regresion_local,
        "anova_grupos": anova,
        "kruskal_grupos": kruskal,
    }

    return df, correlaciones, resumen_grupos, resultados