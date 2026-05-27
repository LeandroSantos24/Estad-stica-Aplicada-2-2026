import pandas as pd


# ============================================================
# ESTADÍSTICA DESCRIPTIVA
# ============================================================
# En este archivo calculamos medidas resumen:
# - media
# - mediana
# - varianza
# - desvío estándar
# - mínimo
# - máximo
# - cuartiles
#
# Estas medidas nos permiten describir cómo se comportan los equipos
# como locales y como visitantes antes de hacer inferencia estadística.
# ============================================================


def resumen_variable(serie):
    """
    Calcula medidas descriptivas básicas para una variable numérica.
    """

    return {
        "n": serie.count(),
        "media": serie.mean(),
        "mediana": serie.median(),
        "varianza": serie.var(ddof=1),
        "desvio_estandar": serie.std(ddof=1),
        "minimo": serie.min(),
        "q1": serie.quantile(0.25),
        "q3": serie.quantile(0.75),
        "maximo": serie.max(),
    }


def resumen_local_vs_visitante(df):
    """
    Compara descriptivamente el rendimiento local y visitante.

    Se analizan:
    - puntos por partido
    - goles por partido
    - eficacia porcentual
    """

    resumen = {
        "Pts_PJ_Local": resumen_variable(df["Pts_PJ_Local"]),
        "Pts_PJ_Visitante": resumen_variable(df["Pts_PJ_Visitante"]),
        "GF_PJ_Local": resumen_variable(df["GF_PJ_Local"]),
        "GF_PJ_Visitante": resumen_variable(df["GF_PJ_Visitante"]),
        "Eficacia_Local_%": resumen_variable(df["Eficacia_Local_%"]),
        "Eficacia_Visitante_%": resumen_variable(df["Eficacia_Visitante_%"]),
        "Delta_Pts_PJ": resumen_variable(df["Delta_Pts_PJ"]),
        "Delta_GF_PJ": resumen_variable(df["Delta_GF_PJ"]),
    }

    tabla_resumen = pd.DataFrame(resumen).T
    return tabla_resumen


def ranking_localia(df):
    """
    Ordena los equipos según la diferencia de puntos por partido
    entre local y visitante.

    Esta diferencia es la variable principal del proyecto:
    Delta_Pts_PJ = Pts_PJ_Local - Pts_PJ_Visitante
    """

    columnas = [
        "Equipo",
        "Pts_PJ_Local",
        "Pts_PJ_Visitante",
        "Delta_Pts_PJ",
        "GF_PJ_Local",
        "GF_PJ_Visitante",
        "Delta_GF_PJ",
        "Eficacia_Local_%",
        "Pct_Victorias_Local",
        "Pct_Victorias_Visitante",
    ]

    ranking = df[columnas].sort_values(by="Delta_Pts_PJ", ascending=False)
    return ranking


def resumen_global_resultados(df):
    """
    Calcula resultados globales de toda la liga.

    Suma todos los partidos, victorias, empates, derrotas, goles y puntos
    para comparar local vs visitante a nivel general.
    """

    total_home_mp = df["Home_MP"].sum()
    total_away_mp = df["Away_MP"].sum()

    resumen = pd.DataFrame({
        "Condicion": ["Local", "Visitante"],
        "Partidos": [total_home_mp, total_away_mp],
        "Victorias": [df["Home_W"].sum(), df["Away_W"].sum()],
        "Empates": [df["Home_D"].sum(), df["Away_D"].sum()],
        "Derrotas": [df["Home_L"].sum(), df["Away_L"].sum()],
        "Goles_Favor": [df["Home_GF"].sum(), df["Away_GF"].sum()],
        "Goles_Contra": [df["Home_GA"].sum(), df["Away_GA"].sum()],
        "Puntos": [df["Home_Pts"].sum(), df["Away_Pts"].sum()],
    })

    resumen["Pts_PJ"] = resumen["Puntos"] / resumen["Partidos"]
    resumen["GF_PJ"] = resumen["Goles_Favor"] / resumen["Partidos"]
    resumen["Pct_Victorias"] = resumen["Victorias"] / resumen["Partidos"] * 100
    resumen["Pct_Empates"] = resumen["Empates"] / resumen["Partidos"] * 100
    resumen["Pct_Derrotas"] = resumen["Derrotas"] / resumen["Partidos"] * 100

    return resumen
