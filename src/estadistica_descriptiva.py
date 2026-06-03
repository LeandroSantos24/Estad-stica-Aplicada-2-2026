import numpy as np
import pandas as pd


# ============================================================
# ESTADÍSTICA DESCRIPTIVA
# ============================================================
# Este archivo contiene los cálculos descriptivos del proyecto.
#
# La estadística descriptiva permite resumir los datos antes de
# aplicar inferencia. Acá calculamos medidas como:
#
# - media
# - mediana
# - varianza
# - desvío estándar
# - mínimo y máximo
# - cuartiles
# - percentiles
# - rango
# - rango intercuartílico
# - coeficiente de variación
#
# También se calculan rankings y resúmenes globales para comparar
# el rendimiento local y visitante.
# ============================================================


def resumen_variable(serie):
    """
    Calcula un resumen descriptivo completo para una variable numérica.

    Fórmulas principales:

    Media:
        x_barra = suma(x_i) / n

    Varianza muestral:
        s² = suma((x_i - x_barra)²) / (n - 1)

    Desvío estándar:
        s = raíz(s²)

    Rango:
        máximo - mínimo

    Rango intercuartílico:
        RIC = Q3 - Q1

    Coeficiente de variación:
        CV = s / media

    Percentiles:
        P10, P25, P50, P75, P90
    """

    serie = pd.Series(serie).dropna()

    n = len(serie)

    if n == 0:
        return {
            "n": 0,
            "media": np.nan,
            "mediana": np.nan,
            "varianza": np.nan,
            "desvio_estandar": np.nan,
            "minimo": np.nan,
            "p10": np.nan,
            "q1_p25": np.nan,
            "p50_mediana": np.nan,
            "q3_p75": np.nan,
            "p90": np.nan,
            "maximo": np.nan,
            "rango": np.nan,
            "rango_intercuartilico": np.nan,
            "coeficiente_variacion": np.nan,
        }

    media = serie.mean()
    mediana = serie.median()
    varianza = serie.var(ddof=1)
    desvio = serie.std(ddof=1)

    minimo = serie.min()
    maximo = serie.max()

    p10 = np.percentile(serie, 10)
    q1 = np.percentile(serie, 25)
    p50 = np.percentile(serie, 50)
    q3 = np.percentile(serie, 75)
    p90 = np.percentile(serie, 90)

    rango = maximo - minimo
    rango_intercuartilico = q3 - q1

    if media != 0:
        coeficiente_variacion = desvio / abs(media)
    else:
        coeficiente_variacion = np.nan

    return {
        "n": n,
        "media": media,
        "mediana": mediana,
        "varianza": varianza,
        "desvio_estandar": desvio,
        "minimo": minimo,
        "p10": p10,
        "q1_p25": q1,
        "p50_mediana": p50,
        "q3_p75": q3,
        "p90": p90,
        "maximo": maximo,
        "rango": rango,
        "rango_intercuartilico": rango_intercuartilico,
        "coeficiente_variacion": coeficiente_variacion,
    }


def resumen_local_vs_visitante(df):
    """
    Calcula resumen descriptivo de las principales variables del proyecto.

    Variables incluidas:

    Pts_PJ_Local:
        puntos por partido jugando como local.

    Pts_PJ_Visitante:
        puntos por partido jugando como visitante.

    GF_PJ_Local:
        goles a favor por partido jugando como local.

    GF_PJ_Visitante:
        goles a favor por partido jugando como visitante.

    Eficacia_Local_%:
        porcentaje de puntos obtenidos como local sobre el máximo posible.

    Eficacia_Visitante_%:
        porcentaje de puntos obtenidos como visitante sobre el máximo posible.

    Delta_Pts_PJ:
        ventaja de localía medida en puntos por partido.

    Delta_GF_PJ:
        diferencia de goles a favor por partido entre local y visitante.
    """

    variables = [
        "Pts_PJ_Local",
        "Pts_PJ_Visitante",
        "GF_PJ_Local",
        "GF_PJ_Visitante",
        "Eficacia_Local_%",
        "Eficacia_Visitante_%",
        "Delta_Pts_PJ",
        "Delta_GF_PJ",
    ]

    resumen = {}

    for variable in variables:
        resumen[variable] = resumen_variable(df[variable])

    tabla = pd.DataFrame(resumen).T

    return tabla


def tabla_percentiles_localia(df):
    """
    Crea una tabla específica de percentiles para Delta_Pts_PJ.

    Esta tabla sirve para explicar la distribución de la ventaja de localía.

    Interpretación:
    - P10: el 10% de los equipos tiene una ventaja igual o menor a ese valor.
    - P25: primer cuartil.
    - P50: mediana.
    - P75: tercer cuartil.
    - P90: el 90% de los equipos tiene una ventaja igual o menor a ese valor.
    """

    datos = df["Delta_Pts_PJ"].dropna()

    tabla = pd.DataFrame(
        [
            {
                "Percentil": "P10",
                "Valor_Delta_Pts_PJ": np.percentile(datos, 10),
                "Interpretacion": "El 10% de los equipos tiene una ventaja de localía igual o menor a este valor.",
            },
            {
                "Percentil": "P25",
                "Valor_Delta_Pts_PJ": np.percentile(datos, 25),
                "Interpretacion": "El 25% de los equipos está por debajo o igual a este valor.",
            },
            {
                "Percentil": "P50 / Mediana",
                "Valor_Delta_Pts_PJ": np.percentile(datos, 50),
                "Interpretacion": "La mitad de los equipos está por debajo y la otra mitad por encima.",
            },
            {
                "Percentil": "P75",
                "Valor_Delta_Pts_PJ": np.percentile(datos, 75),
                "Interpretacion": "El 75% de los equipos está por debajo o igual a este valor.",
            },
            {
                "Percentil": "P90",
                "Valor_Delta_Pts_PJ": np.percentile(datos, 90),
                "Interpretacion": "El 90% de los equipos tiene una ventaja de localía igual o menor a este valor.",
            },
        ]
    )

    return tabla


def ranking_localia(df):
    """
    Ordena los equipos según su ventaja de localía.

    Fórmula principal:

        Delta_Pts_PJ = Pts_PJ_Local - Pts_PJ_Visitante

    Si Delta_Pts_PJ es alto:
        el equipo rindió mucho mejor como local que como visitante.

    Si Delta_Pts_PJ es cercano a cero:
        el equipo rindió parecido de local y visitante.

    Si Delta_Pts_PJ es negativo:
        el equipo rindió mejor como visitante.
    """

    ranking = df.copy()

    ranking["Percentil_Localia"] = ranking["Delta_Pts_PJ"].rank(pct=True) * 100

    def clasificar_delta(valor):
        if valor >= 1:
            return "Ventaja local muy alta"
        if valor >= 0.5:
            return "Ventaja local alta"
        if valor >= 0.2:
            return "Ventaja local moderada"
        if valor >= 0:
            return "Ventaja local baja"
        return "Mejor rendimiento visitante"

    ranking["Clasificacion_Localia"] = ranking["Delta_Pts_PJ"].apply(clasificar_delta)

    columnas = [
        "Equipo",
        "Pts_PJ_Local",
        "Pts_PJ_Visitante",
        "Delta_Pts_PJ",
        "GF_PJ_Local",
        "GF_PJ_Visitante",
        "Delta_GF_PJ",
        "Eficacia_Local_%",
        "Eficacia_Visitante_%",
        "Percentil_Localia",
        "Clasificacion_Localia",
    ]

    columnas_existentes = [col for col in columnas if col in ranking.columns]

    ranking = ranking[columnas_existentes].sort_values(
        by="Delta_Pts_PJ",
        ascending=False,
    )

    return ranking


def resumen_global_resultados(df):
    """
    Calcula un resumen global de resultados local vs visitante.

    Se suman los resultados de todos los equipos.

    Para Local:
        Victorias = suma de Home_W
        Empates   = suma de Home_D
        Derrotas  = suma de Home_L

    Para Visitante:
        Victorias = suma de Away_W
        Empates   = suma de Away_D
        Derrotas  = suma de Away_L

    Importante:
    En un partido empatado, el empate aparece tanto para el local como para el visitante
    porque ambos equipos empataron ese mismo partido.

    Por eso:
        Empates Local = Empates Visitante

    Los empates se cuentan así porque estamos comparando rendimiento desde la
    perspectiva de cada condición.
    """

    partidos_local = int(df["Home_MP"].sum())
    partidos_visitante = int(df["Away_MP"].sum())

    victorias_local = int(df["Home_W"].sum())
    empates_local = int(df["Home_D"].sum())
    derrotas_local = int(df["Home_L"].sum())

    victorias_visitante = int(df["Away_W"].sum())
    empates_visitante = int(df["Away_D"].sum())
    derrotas_visitante = int(df["Away_L"].sum())

    goles_local = int(df["Home_GF"].sum())
    goles_contra_local = int(df["Home_GA"].sum())

    goles_visitante = int(df["Away_GF"].sum())
    goles_contra_visitante = int(df["Away_GA"].sum())

    puntos_local = int(df["Home_Pts"].sum())
    puntos_visitante = int(df["Away_Pts"].sum())

    tabla = pd.DataFrame(
        [
            {
                "Condicion": "Local",
                "Partidos": partidos_local,
                "Victorias": victorias_local,
                "Empates": empates_local,
                "Derrotas": derrotas_local,
                "Goles_Favor": goles_local,
                "Goles_Contra": goles_contra_local,
                "Puntos": puntos_local,
                "Pts_PJ": puntos_local / partidos_local,
                "GF_PJ": goles_local / partidos_local,
                "Pct_Victorias": victorias_local / partidos_local * 100,
                "Pct_Empates": empates_local / partidos_local * 100,
                "Pct_Derrotas": derrotas_local / partidos_local * 100,
            },
            {
                "Condicion": "Visitante",
                "Partidos": partidos_visitante,
                "Victorias": victorias_visitante,
                "Empates": empates_visitante,
                "Derrotas": derrotas_visitante,
                "Goles_Favor": goles_visitante,
                "Goles_Contra": goles_contra_visitante,
                "Puntos": puntos_visitante,
                "Pts_PJ": puntos_visitante / partidos_visitante,
                "GF_PJ": goles_visitante / partidos_visitante,
                "Pct_Victorias": victorias_visitante / partidos_visitante * 100,
                "Pct_Empates": empates_visitante / partidos_visitante * 100,
                "Pct_Derrotas": derrotas_visitante / partidos_visitante * 100,
            },
        ]
    )

    return tabla


def resumen_empates(df):
    """
    Resume el papel de los empates en el torneo.

    Esto es importante porque:
    - En la prueba binomial de victorias se excluyen los empates.
    - En la prueba chi-cuadrado sí se incluyen los empates.
    - En el cálculo de puntos, el empate suma 1 punto a cada equipo.

    Fórmula de porcentaje de empates:

        Pct_Empates = Empates / Partidos * 100
    """

    partidos = int(df["Home_MP"].sum())

    victorias_locales = int(df["Home_W"].sum())
    empates = int(df["Home_D"].sum())
    victorias_visitantes = int(df["Away_W"].sum())

    tabla = pd.DataFrame(
        [
            {
                "Categoria": "Victoria local",
                "Cantidad": victorias_locales,
                "Porcentaje": victorias_locales / partidos * 100,
                "Interpretacion": "Partidos ganados por el equipo local.",
            },
            {
                "Categoria": "Empate",
                "Cantidad": empates,
                "Porcentaje": empates / partidos * 100,
                "Interpretacion": "Partidos sin ganador. Suman 1 punto para cada equipo.",
            },
            {
                "Categoria": "Victoria visitante",
                "Cantidad": victorias_visitantes,
                "Porcentaje": victorias_visitantes / partidos * 100,
                "Interpretacion": "Partidos ganados por el equipo visitante.",
            },
        ]
    )

    return tabla


def tabla_formulas_principales():
    """
    Devuelve una tabla con las fórmulas principales usadas en el proyecto.

    Esta tabla es útil para el informe Word, porque permite explicar cómo
    se calculó cada indicador.
    """

    formulas = pd.DataFrame(
        [
            {
                "Indicador": "Puntos por partido local",
                "Formula": "Pts_PJ_Local = Puntos_Local / Partidos_Local",
                "Interpretacion": "Mide cuántos puntos obtiene un equipo por partido jugando como local.",
            },
            {
                "Indicador": "Puntos por partido visitante",
                "Formula": "Pts_PJ_Visitante = Puntos_Visitante / Partidos_Visitante",
                "Interpretacion": "Mide cuántos puntos obtiene un equipo por partido jugando como visitante.",
            },
            {
                "Indicador": "Ventaja de localía",
                "Formula": "Delta_Pts_PJ = Pts_PJ_Local - Pts_PJ_Visitante",
                "Interpretacion": "Mide cuánto mejora o empeora el rendimiento al jugar como local.",
            },
            {
                "Indicador": "Goles por partido local",
                "Formula": "GF_PJ_Local = Goles_Local / Partidos_Local",
                "Interpretacion": "Mide la producción ofensiva como local.",
            },
            {
                "Indicador": "Goles por partido visitante",
                "Formula": "GF_PJ_Visitante = Goles_Visitante / Partidos_Visitante",
                "Interpretacion": "Mide la producción ofensiva como visitante.",
            },
            {
                "Indicador": "Diferencia de goles por partido",
                "Formula": "Delta_GF_PJ = GF_PJ_Local - GF_PJ_Visitante",
                "Interpretacion": "Mide la diferencia ofensiva entre jugar de local y visitante.",
            },
            {
                "Indicador": "Eficacia local",
                "Formula": "Eficacia_Local_% = Puntos_Local / (3 * Partidos_Local) * 100",
                "Interpretacion": "Porcentaje de puntos obtenidos sobre el máximo posible como local.",
            },
            {
                "Indicador": "Porcentaje de victorias",
                "Formula": "Pct_Victorias = Victorias / Partidos * 100",
                "Interpretacion": "Proporción de partidos ganados en una condición determinada.",
            },
        ]
    )

    return formulas


def glosario_estadistico():
    """
    Devuelve un glosario básico para el informe.
    """

    glosario = pd.DataFrame(
        [
            {
                "Concepto": "Media",
                "Definicion": "Promedio aritmético de un conjunto de datos.",
            },
            {
                "Concepto": "Mediana",
                "Definicion": "Valor central de los datos ordenados.",
            },
            {
                "Concepto": "Varianza",
                "Definicion": "Medida de dispersión que indica cuánto se alejan los datos de la media.",
            },
            {
                "Concepto": "Desvío estándar",
                "Definicion": "Raíz cuadrada de la varianza. Mide dispersión en las mismas unidades que la variable.",
            },
            {
                "Concepto": "Percentil",
                "Definicion": "Valor por debajo del cual se encuentra un determinado porcentaje de observaciones.",
            },
            {
                "Concepto": "Cuartil",
                "Definicion": "Percentiles 25, 50 y 75. Dividen los datos en cuatro partes.",
            },
            {
                "Concepto": "Rango intercuartílico",
                "Definicion": "Diferencia entre el tercer y el primer cuartil. Mide la dispersión central.",
            },
            {
                "Concepto": "Z-score",
                "Definicion": "Indica cuántos desvíos estándar se encuentra un valor por encima o por debajo de la media.",
            },
            {
                "Concepto": "p-valor",
                "Definicion": "Probabilidad de obtener un resultado tan extremo como el observado si la hipótesis nula fuera verdadera.",
            },
            {
                "Concepto": "Hipótesis nula",
                "Definicion": "Supuesto inicial que se pone a prueba estadísticamente.",
            },
            {
                "Concepto": "Intervalo de confianza",
                "Definicion": "Rango de valores plausibles para un parámetro poblacional.",
            },
            {
                "Concepto": "Correlación",
                "Definicion": "Medida de asociación entre dos variables.",
            },
            {
                "Concepto": "Regresión",
                "Definicion": "Modelo que permite estudiar cómo una variable explica o predice a otra.",
            },
            {
                "Concepto": "ANOVA",
                "Definicion": "Prueba que compara medias entre tres o más grupos.",
            },
        ]
    )

    return glosario