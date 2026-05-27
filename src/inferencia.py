import numpy as np
import pandas as pd
from scipy import stats

from src.config import ALPHA


# ============================================================
# INFERENCIA ESTADÍSTICA
# ============================================================
# En este archivo aplicamos herramientas de Estadística Aplicada II:
#
# 1. Intervalo de confianza para la diferencia media de puntos.
# 2. Prueba t pareada para comparar rendimiento local vs visitante.
# 3. Prueba no paramétrica de Wilcoxon.
# 4. Prueba binomial para victorias locales vs visitantes.
# 5. Prueba chi-cuadrado para comparar distribución de resultados.
# 6. Z-score y percentiles para detectar equipos destacados.
# 7. Teorema de Chebyshev aplicado a la variable Delta_Pts_PJ.
# ============================================================


def intervalo_confianza_media_pareada(diferencias, alpha=ALPHA):
    """
    Calcula un intervalo de confianza para la media de una muestra de diferencias.

    En este caso, la diferencia es:
    Delta_Pts_PJ = Pts_PJ_Local - Pts_PJ_Visitante

    Como comparamos al mismo equipo en dos condiciones,
    trabajamos con diferencias apareadas.
    """

    diferencias = pd.Series(diferencias).dropna()

    n = diferencias.count()
    media = diferencias.mean()
    desvio = diferencias.std(ddof=1)

    error_estandar = desvio / np.sqrt(n)

    t_critico = stats.t.ppf(1 - alpha / 2, df=n - 1)

    limite_inferior = media - t_critico * error_estandar
    limite_superior = media + t_critico * error_estandar

    return {
        "n": n,
        "media_diferencia": media,
        "desvio_diferencia": desvio,
        "error_estandar": error_estandar,
        "t_critico": t_critico,
        "ic_inferior": limite_inferior,
        "ic_superior": limite_superior,
        "confianza": 1 - alpha,
    }


def prueba_t_pareada(local, visitante):
    """
    Realiza una prueba t pareada.

    Hipótesis:
    H0: mu_d = 0
    H1: mu_d > 0

    Donde:
    mu_d = media de las diferencias entre rendimiento local y visitante.

    Si el p-valor es menor a alpha, se rechaza H0 y se concluye
    que el rendimiento como local es significativamente mayor.
    """

    local = pd.Series(local).dropna()
    visitante = pd.Series(visitante).dropna()

    resultado = stats.ttest_rel(local, visitante, alternative="greater")

    return {
        "prueba": "t pareada",
        "hipotesis_nula": "mu_d = 0",
        "hipotesis_alternativa": "mu_d > 0",
        "estadistico": resultado.statistic,
        "p_valor": resultado.pvalue,
        "decision": "Rechazar H0" if resultado.pvalue < ALPHA else "No rechazar H0",
    }


def prueba_wilcoxon_pareada(local, visitante):
    """
    Realiza la prueba no paramétrica de Wilcoxon para muestras pareadas.

    Se utiliza como complemento de la prueba t pareada.
    Es útil cuando no queremos depender fuertemente del supuesto
    de normalidad de las diferencias.
    """

    local = pd.Series(local).dropna()
    visitante = pd.Series(visitante).dropna()

    resultado = stats.wilcoxon(local, visitante, alternative="greater")

    return {
        "prueba": "Wilcoxon pareada",
        "hipotesis_nula": "la mediana de las diferencias es 0",
        "hipotesis_alternativa": "la mediana de las diferencias es mayor que 0",
        "estadistico": resultado.statistic,
        "p_valor": resultado.pvalue,
        "decision": "Rechazar H0" if resultado.pvalue < ALPHA else "No rechazar H0",
    }


def prueba_binomial_victorias(df):
    """
    Compara cantidad de victorias locales contra victorias visitantes.

    Se excluyen los empates y se analiza si, entre los partidos con ganador,
    la proporción de victorias locales es mayor que 0.5.

    Hipótesis:
    H0: p = 0.5
    H1: p > 0.5
    """

    victorias_local = int(df["Home_W"].sum())
    victorias_visitante = int(df["Away_W"].sum())

    partidos_con_ganador = victorias_local + victorias_visitante

    resultado = stats.binomtest(
        k=victorias_local,
        n=partidos_con_ganador,
        p=0.5,
        alternative="greater"
    )

    return {
        "prueba": "Binomial victorias local vs visitante",
        "victorias_local": victorias_local,
        "victorias_visitante": victorias_visitante,
        "partidos_con_ganador": partidos_con_ganador,
        "proporcion_victorias_local": victorias_local / partidos_con_ganador,
        "hipotesis_nula": "p = 0.5",
        "hipotesis_alternativa": "p > 0.5",
        "p_valor": resultado.pvalue,
        "decision": "Rechazar H0" if resultado.pvalue < ALPHA else "No rechazar H0",
    }


def prueba_chi_cuadrado_resultados(df):
    """
    Aplica una prueba chi-cuadrado sobre la distribución de resultados.

    Compara la distribución:
    - victorias
    - empates
    - derrotas

    para local y visitante.

    Tabla:
                  Victoria  Empate  Derrota
    Local
    Visitante
    """

    tabla = np.array([
        [df["Home_W"].sum(), df["Home_D"].sum(), df["Home_L"].sum()],
        [df["Away_W"].sum(), df["Away_D"].sum(), df["Away_L"].sum()],
    ])

    chi2, p_valor, gl, esperadas = stats.chi2_contingency(tabla)

    tabla_observada = pd.DataFrame(
        tabla,
        index=["Local", "Visitante"],
        columns=["Victorias", "Empates", "Derrotas"]
    )

    tabla_esperada = pd.DataFrame(
        esperadas,
        index=["Local", "Visitante"],
        columns=["Victorias", "Empates", "Derrotas"]
    )

    resultado = {
        "prueba": "Chi-cuadrado distribución de resultados",
        "chi2": chi2,
        "gl": gl,
        "p_valor": p_valor,
        "decision": "Rechazar H0" if p_valor < ALPHA else "No rechazar H0",
    }

    return resultado, tabla_observada, tabla_esperada


def zscore_percentiles_localia(df):
    """
    Calcula Z-score y percentiles para la variable Delta_Pts_PJ.

    Z-score:
    Indica cuántos desvíos estándar se aleja un equipo del promedio.

    Percentil:
    Indica qué porcentaje de equipos queda por debajo de ese valor.
    """

    df_z = df.copy()

    media = df_z["Delta_Pts_PJ"].mean()
    desvio = df_z["Delta_Pts_PJ"].std(ddof=1)

    df_z["Z_Delta_Pts_PJ"] = (df_z["Delta_Pts_PJ"] - media) / desvio

    df_z["Percentil_Delta_Pts_PJ"] = df_z["Delta_Pts_PJ"].apply(
        lambda x: stats.percentileofscore(df_z["Delta_Pts_PJ"], x, kind="rank")
    )

    def clasificar(z):
        if z >= 2:
            return "Atípico positivo"
        elif z >= 1:
            return "Localía alta"
        elif z <= -2:
            return "Atípico negativo"
        elif z <= -1:
            return "Localía baja"
        else:
            return "Localía media"

    df_z["Clasificacion_Z"] = df_z["Z_Delta_Pts_PJ"].apply(clasificar)

    columnas = [
        "Equipo",
        "Pts_PJ_Local",
        "Pts_PJ_Visitante",
        "Delta_Pts_PJ",
        "Z_Delta_Pts_PJ",
        "Percentil_Delta_Pts_PJ",
        "Clasificacion_Z",
    ]

    return df_z[columnas].sort_values(by="Delta_Pts_PJ", ascending=False)


def analisis_chebyshev(diferencias, k=2):
    """
    Aplica el Teorema de Chebyshev a Delta_Pts_PJ.

    Chebyshev dice que, para cualquier distribución,
    al menos 1 - 1/k^2 de los datos se encuentran a menos de k
    desvíos estándar de la media.

    Para k = 2:
    al menos 75% de los datos deberían caer dentro de ese rango.
    """

    diferencias = pd.Series(diferencias).dropna()

    media = diferencias.mean()
    desvio = diferencias.std(ddof=1)

    limite_inferior = media - k * desvio
    limite_superior = media + k * desvio

    dentro = diferencias.between(limite_inferior, limite_superior).sum()
    n = diferencias.count()

    proporcion_observada = dentro / n
    cota_chebyshev = 1 - (1 / k**2)

    return {
        "variable": "Delta_Pts_PJ",
        "k": k,
        "media": media,
        "desvio": desvio,
        "limite_inferior": limite_inferior,
        "limite_superior": limite_superior,
        "cantidad_dentro": dentro,
        "n": n,
        "proporcion_observada": proporcion_observada,
        "cota_minima_chebyshev": cota_chebyshev,
    }


def ejecutar_inferencia(df):
    """
    Ejecuta todas las pruebas inferenciales del proyecto.
    """

    ic_delta = intervalo_confianza_media_pareada(df["Delta_Pts_PJ"])

    t_puntos = prueba_t_pareada(
        df["Pts_PJ_Local"],
        df["Pts_PJ_Visitante"]
    )

    t_goles = prueba_t_pareada(
        df["GF_PJ_Local"],
        df["GF_PJ_Visitante"]
    )

    wilcoxon_puntos = prueba_wilcoxon_pareada(
        df["Pts_PJ_Local"],
        df["Pts_PJ_Visitante"]
    )

    binomial = prueba_binomial_victorias(df)

    chi_resultado, tabla_chi_obs, tabla_chi_esp = prueba_chi_cuadrado_resultados(df)

    zscores = zscore_percentiles_localia(df)

    chebyshev = analisis_chebyshev(df["Delta_Pts_PJ"], k=2)

    resultados = {
        "intervalo_confianza_delta_puntos": ic_delta,
        "prueba_t_puntos": t_puntos,
        "prueba_t_goles": t_goles,
        "wilcoxon_puntos": wilcoxon_puntos,
        "prueba_binomial_victorias": binomial,
        "chi_cuadrado_resultados": chi_resultado,
        "chebyshev": chebyshev,
    }

    return resultados, tabla_chi_obs, tabla_chi_esp, zscores

