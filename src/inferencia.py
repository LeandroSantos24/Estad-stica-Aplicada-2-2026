import numpy as np
import pandas as pd
from scipy import stats

from src.config import ALPHA


# ============================================================
# INFERENCIA ESTADÍSTICA
# ============================================================
# Este archivo contiene las pruebas estadísticas principales
# del proyecto "Factor localía - Liga Profesional Argentina 2023".
#
# Variables centrales:
#
# Pts_PJ_Local:
#   puntos por partido jugando como local.
#
# Pts_PJ_Visitante:
#   puntos por partido jugando como visitante.
#
# Delta_Pts_PJ:
#   diferencia entre rendimiento local y visitante.
#
#   Delta_Pts_PJ = Pts_PJ_Local - Pts_PJ_Visitante
#
# Si Delta_Pts_PJ > 0:
#   el equipo rindió mejor como local.
#
# Si Delta_Pts_PJ = 0:
#   el equipo rindió igual como local y visitante.
#
# Si Delta_Pts_PJ < 0:
#   el equipo rindió mejor como visitante.
# ============================================================


def intervalo_confianza_media_pareada(diferencias, alpha=ALPHA):
    """
    Calcula un intervalo de confianza para la media de diferencias.

    Aplicación en el proyecto:
    Queremos estimar la ventaja promedio de localía:

        Delta_Pts_PJ = Pts_PJ_Local - Pts_PJ_Visitante

    Fórmula:

        IC = media ± t_critico * (s / sqrt(n))

    donde:
    - media es el promedio de las diferencias.
    - s es el desvío estándar muestral de las diferencias.
    - n es la cantidad de equipos.
    - t_critico viene de la distribución t de Student.
    """

    diferencias = pd.Series(diferencias).dropna()

    n = len(diferencias)
    media = diferencias.mean()
    desvio = diferencias.std(ddof=1)
    error_estandar = desvio / np.sqrt(n)

    t_critico = stats.t.ppf(1 - alpha / 2, df=n - 1)

    ic_inferior = media - t_critico * error_estandar
    ic_superior = media + t_critico * error_estandar

    return {
        "n": n,
        "media_diferencia": media,
        "desvio_diferencia": desvio,
        "error_estandar": error_estandar,
        "t_critico": t_critico,
        "ic_inferior": ic_inferior,
        "ic_superior": ic_superior,
        "confianza": 1 - alpha,
        "formula": "IC = media ± t_critico * (s / sqrt(n))",
        "interpretacion": (
            "Intervalo estimado para la ventaja promedio de localía "
            "medida como diferencia de puntos por partido."
        ),
    }


def prueba_t_pareada(local, visitante, alpha=ALPHA):
    """
    Prueba t pareada para comparar medias relacionadas.

    Aplicación:
    Compara el rendimiento del mismo equipo en dos condiciones:
    - local
    - visitante

    Hipótesis:

        H0: mu_d = 0
        H1: mu_d > 0

    donde:

        d = local - visitante

    Si se rechaza H0, hay evidencia de que el rendimiento local
    promedio es mayor que el visitante.
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
        "alpha": alpha,
        "decision": "Rechazar H0" if resultado.pvalue < alpha else "No rechazar H0",
        "interpretacion": (
            "Compara medias relacionadas. En este caso, compara el rendimiento "
            "del mismo equipo como local y como visitante."
        ),
    }


def prueba_wilcoxon_pareada(local, visitante, alpha=ALPHA):
    """
    Prueba no paramétrica de Wilcoxon para muestras relacionadas.

    Aplicación:
    Es una alternativa no paramétrica a la prueba t pareada.

    Hipótesis:

        H0: la mediana de las diferencias es 0
        H1: la mediana de las diferencias es mayor que 0

    Se usa como complemento porque no exige normalidad estricta.
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
        "alpha": alpha,
        "decision": "Rechazar H0" if resultado.pvalue < alpha else "No rechazar H0",
        "interpretacion": (
            "Prueba no paramétrica para muestras relacionadas. Refuerza la conclusión "
            "sin depender del supuesto de normalidad."
        ),
    }


def prueba_del_signo(local, visitante, alpha=ALPHA):
    """
    Prueba del signo.

    Esta prueba analiza solamente el signo de las diferencias, no su magnitud.

    Para cada equipo:

        d = Pts_PJ_Local - Pts_PJ_Visitante

    Si d > 0:
        el equipo rindió mejor como local.

    Si d < 0:
        el equipo rindió mejor como visitante.

    Si d = 0:
        empate exacto entre rendimiento local y visitante.
        Se excluye de la prueba del signo.

    Hipótesis:

        H0: p = 0.5
        H1: p > 0.5

    donde p es la probabilidad de que un equipo rinda mejor como local.
    """

    local = pd.Series(local).reset_index(drop=True)
    visitante = pd.Series(visitante).reset_index(drop=True)

    diferencias = local - visitante

    positivos = int((diferencias > 0).sum())
    negativos = int((diferencias < 0).sum())
    ceros = int((diferencias == 0).sum())

    n = positivos + negativos

    if n == 0:
        return {
            "prueba": "Prueba del signo",
            "positivos": positivos,
            "negativos": negativos,
            "ceros_excluidos": ceros,
            "n_utilizado": n,
            "hipotesis_nula": "p = 0.5",
            "hipotesis_alternativa": "p > 0.5",
            "p_valor": np.nan,
            "alpha": alpha,
            "decision": "No se puede calcular",
            "interpretacion": "No hay diferencias positivas ni negativas para evaluar.",
        }

    resultado = stats.binomtest(
        k=positivos,
        n=n,
        p=0.5,
        alternative="greater",
    )

    return {
        "prueba": "Prueba del signo",
        "positivos": positivos,
        "negativos": negativos,
        "ceros_excluidos": ceros,
        "n_utilizado": n,
        "hipotesis_nula": "p = 0.5",
        "hipotesis_alternativa": "p > 0.5",
        "p_valor": resultado.pvalue,
        "alpha": alpha,
        "decision": "Rechazar H0" if resultado.pvalue < alpha else "No rechazar H0",
        "interpretacion": (
            "Evalúa si la cantidad de equipos que rindieron mejor como locales "
            "es significativamente mayor a la cantidad esperada por azar."
        ),
    }


def prueba_binomial_victorias(df, alpha=ALPHA):
    """
    Prueba binomial para comparar victorias locales contra victorias visitantes.

    Esta prueba usa solamente partidos con ganador:

        victorias_locales vs victorias_visitantes

    Los empates se excluyen porque la prueba binomial compara dos categorías.
    En este caso las dos categorías son:

        1. ganó el local
        2. ganó el visitante

    Los empates NO se pierden: se analizan después con chi-cuadrado,
    donde sí se consideran tres categorías:

        victoria local, empate, victoria visitante.

    Hipótesis:

        H0: p = 0.5
        H1: p > 0.5

    donde p es la proporción de victorias locales entre partidos con ganador.
    """

    victorias_local = int(df["Home_W"].sum())
    victorias_visitante = int(df["Away_W"].sum())

    partidos_con_ganador = victorias_local + victorias_visitante

    resultado = stats.binomtest(
        k=victorias_local,
        n=partidos_con_ganador,
        p=0.5,
        alternative="greater",
    )

    proporcion = victorias_local / partidos_con_ganador

    return {
        "prueba": "Binomial victorias local vs visitante",
        "victorias_local": victorias_local,
        "victorias_visitante": victorias_visitante,
        "partidos_con_ganador": partidos_con_ganador,
        "empates_excluidos": int(df["Home_D"].sum()),
        "proporcion_victorias_local": proporcion,
        "hipotesis_nula": "p = 0.5",
        "hipotesis_alternativa": "p > 0.5",
        "p_valor": resultado.pvalue,
        "alpha": alpha,
        "decision": "Rechazar H0" if resultado.pvalue < alpha else "No rechazar H0",
        "interpretacion": (
            "Compara si, entre los partidos con ganador, la proporción de victorias "
            "locales es mayor que la proporción de victorias visitantes."
        ),
    }


def prueba_chi_cuadrado_resultados(df, alpha=ALPHA):
    """
    Prueba chi-cuadrado de independencia.

    Se arma una tabla 2 x 3:

                    Victoria   Empate   Derrota
        Local
        Visitante

    Para la fila Local:
    - Victoria = Home_W
    - Empate   = Home_D
    - Derrota  = Home_L

    Para la fila Visitante:
    - Victoria = Away_W
    - Empate   = Away_D
    - Derrota  = Away_L

    Hipótesis:

        H0: el resultado es independiente de la condición local/visitante.
        H1: el resultado está asociado a la condición local/visitante.

    Esta prueba incluye empates.
    """

    tabla_observada = pd.DataFrame(
        {
            "Victoria": [int(df["Home_W"].sum()), int(df["Away_W"].sum())],
            "Empate": [int(df["Home_D"].sum()), int(df["Away_D"].sum())],
            "Derrota": [int(df["Home_L"].sum()), int(df["Away_L"].sum())],
        },
        index=["Local", "Visitante"],
    )

    chi2, p_valor, gl, esperadas = stats.chi2_contingency(tabla_observada)

    tabla_esperada = pd.DataFrame(
        esperadas,
        index=tabla_observada.index,
        columns=tabla_observada.columns,
    )

    return {
        "resultado": {
            "prueba": "Chi-cuadrado distribución de resultados",
            "chi2": chi2,
            "gl": gl,
            "p_valor": p_valor,
            "alpha": alpha,
            "decision": "Rechazar H0" if p_valor < alpha else "No rechazar H0",
            "hipotesis_nula": "resultado independiente de localía",
            "hipotesis_alternativa": "resultado asociado a localía",
            "interpretacion": (
                "Evalúa si la distribución de victorias, empates y derrotas "
                "depende de la condición local o visitante."
            ),
        },
        "observadas": tabla_observada,
        "esperadas": tabla_esperada,
    }


def prueba_bondad_ajuste_resultados(df, alpha=ALPHA):
    """
    Prueba chi-cuadrado de bondad de ajuste.

    Se analizan los resultados globales del torneo:

        victorias locales, empates, victorias visitantes

    Observados:

        O = [victorias locales, empates, victorias visitantes]

    Como modelo simple de referencia, se prueba contra una distribución uniforme:

        H0: P(victoria local) = P(empate) = P(victoria visitante) = 1/3

    Esto no significa que la distribución uniforme sea la "verdadera",
    sino que funciona como referencia teórica para ver si los resultados
    están equilibrados o no.

    Hipótesis:

        H0: las tres categorías son igualmente probables.
        H1: al menos una categoría tiene una proporción diferente.
    """

    victorias_locales = int(df["Home_W"].sum())
    empates = int(df["Home_D"].sum())
    victorias_visitantes = int(df["Away_W"].sum())

    observados = np.array([victorias_locales, empates, victorias_visitantes])
    total = observados.sum()
    esperados = np.array([total / 3, total / 3, total / 3])

    chi2, p_valor = stats.chisquare(f_obs=observados, f_exp=esperados)

    tabla = pd.DataFrame(
        {
            "Categoria": ["Victoria local", "Empate", "Victoria visitante"],
            "Observado": observados,
            "Esperado_uniforme": esperados,
        }
    )

    return {
        "prueba": "Bondad de ajuste resultados globales",
        "chi2": chi2,
        "gl": len(observados) - 1,
        "p_valor": p_valor,
        "alpha": alpha,
        "decision": "Rechazar H0" if p_valor < alpha else "No rechazar H0",
        "hipotesis_nula": "las tres categorías son igualmente probables",
        "hipotesis_alternativa": "al menos una categoría difiere",
        "victorias_locales": victorias_locales,
        "empates": empates,
        "victorias_visitantes": victorias_visitantes,
        "interpretacion": (
            "Evalúa si las proporciones globales de victoria local, empate "
            "y victoria visitante se alejan de una distribución uniforme."
        ),
        "tabla": tabla,
    }


def prueba_varianza_delta(diferencias, varianza_hipotetica=0.10, alpha=ALPHA):
    """
    Prueba de hipótesis sobre una varianza.

    Variable analizada:

        Delta_Pts_PJ

    Hipótesis:

        H0: sigma² = varianza_hipotetica
        H1: sigma² != varianza_hipotetica

    Estadístico:

        chi² = (n - 1) * s² / sigma0²

    donde:
    - n es la cantidad de equipos.
    - s² es la varianza muestral de Delta_Pts_PJ.
    - sigma0² es la varianza hipotética.

    Nota:
    Este análisis se incluye como complemento para cubrir el tema de
    hipótesis sobre una varianza. Su interpretación no es tan central
    como la prueba t o Wilcoxon.
    """

    diferencias = pd.Series(diferencias).dropna()

    n = len(diferencias)
    varianza_muestral = diferencias.var(ddof=1)

    chi2 = (n - 1) * varianza_muestral / varianza_hipotetica

    gl = n - 1

    p_izquierda = stats.chi2.cdf(chi2, gl)
    p_derecha = 1 - stats.chi2.cdf(chi2, gl)

    p_valor = 2 * min(p_izquierda, p_derecha)
    p_valor = min(p_valor, 1)

    return {
        "prueba": "Hipótesis sobre una varianza",
        "variable": "Delta_Pts_PJ",
        "n": n,
        "varianza_muestral": varianza_muestral,
        "varianza_hipotetica": varianza_hipotetica,
        "chi2": chi2,
        "gl": gl,
        "p_valor": p_valor,
        "alpha": alpha,
        "hipotesis_nula": f"sigma² = {varianza_hipotetica}",
        "hipotesis_alternativa": f"sigma² != {varianza_hipotetica}",
        "decision": "Rechazar H0" if p_valor < alpha else "No rechazar H0",
        "interpretacion": (
            "Contrasta si la varianza observada de la ventaja de localía "
            "difiere de una varianza de referencia."
        ),
    }


def prueba_kolmogorov_smirnov_normalidad(diferencias, alpha=ALPHA):
    """
    Prueba de Kolmogorov-Smirnov para normalidad.

    Se estandariza la variable Delta_Pts_PJ:

        z = (x - media) / desvio

    Luego se compara contra una normal estándar N(0,1).

    Hipótesis:

        H0: los datos provienen de una distribución normal.
        H1: los datos no provienen de una distribución normal.

    Nota:
    Con muestras chicas, esta prueba puede tener poca potencia.
    Se usa junto con el Q-Q plot como análisis complementario.
    """

    diferencias = pd.Series(diferencias).dropna()

    media = diferencias.mean()
    desvio = diferencias.std(ddof=1)

    z = (diferencias - media) / desvio

    resultado = stats.kstest(z, "norm")

    return {
        "prueba": "Kolmogorov-Smirnov normalidad",
        "variable": "Delta_Pts_PJ estandarizada",
        "estadistico": resultado.statistic,
        "p_valor": resultado.pvalue,
        "alpha": alpha,
        "hipotesis_nula": "la variable sigue una distribución normal",
        "hipotesis_alternativa": "la variable no sigue una distribución normal",
        "decision": "Rechazar H0" if resultado.pvalue < alpha else "No rechazar H0",
        "media": media,
        "desvio": desvio,
        "interpretacion": (
            "Evalúa si la distribución de la ventaja de localía es compatible "
            "con una distribución normal."
        ),
    }


def zscore_percentiles_localia(df):
    """
    Calcula Z-score y percentiles para Delta_Pts_PJ.

    Z-score:

        z = (x - media) / desvio

    Interpretación:
    - z > 0: el equipo está por encima del promedio de ventaja de localía.
    - z < 0: el equipo está por debajo del promedio.
    - z >= 2: caso atípico positivo aproximado.
    - z <= -2: caso atípico negativo aproximado.

    Percentil:
    Indica qué porcentaje de equipos tiene una ventaja de localía menor o igual.
    """

    df_z = df[["Equipo", "Delta_Pts_PJ"]].copy()

    media = df_z["Delta_Pts_PJ"].mean()
    desvio = df_z["Delta_Pts_PJ"].std(ddof=1)

    df_z["Z_Delta_Pts_PJ"] = (df_z["Delta_Pts_PJ"] - media) / desvio

    df_z["Percentil_Localia"] = df_z["Delta_Pts_PJ"].rank(pct=True) * 100

    def clasificar(z):
        if z >= 2:
            return "Atípico positivo"
        if z >= 1:
            return "Localía alta"
        if z <= -2:
            return "Atípico negativo"
        if z <= -1:
            return "Localía baja"
        return "Localía media"

    df_z["Clasificacion"] = df_z["Z_Delta_Pts_PJ"].apply(clasificar)

    df_z = df_z.sort_values(by="Delta_Pts_PJ", ascending=False)

    return df_z


def tabla_percentiles_delta(df):
    """
    Calcula percentiles principales de Delta_Pts_PJ.

    Sirve para describir la distribución de la ventaja de localía.

    Percentiles incluidos:
    - P10
    - P25
    - P50
    - P75
    - P90
    """

    datos = df["Delta_Pts_PJ"].dropna()

    percentiles = {
        "P10": np.percentile(datos, 10),
        "P25": np.percentile(datos, 25),
        "P50_mediana": np.percentile(datos, 50),
        "P75": np.percentile(datos, 75),
        "P90": np.percentile(datos, 90),
    }

    tabla = pd.DataFrame(
        [{"Percentil": clave, "Valor_Delta_Pts_PJ": valor} for clave, valor in percentiles.items()]
    )

    return tabla


def analisis_chebyshev(diferencias, k=2):
    """
    Aplica el Teorema de Chebyshev.

    El Teorema de Chebyshev dice que, para cualquier distribución,
    al menos:

        1 - 1/k²

    de los datos se encuentra dentro del intervalo:

        media ± k * desvio

    Para k = 2:

        1 - 1/2² = 1 - 1/4 = 0.75

    Es decir, al menos el 75% de los datos debería estar dentro
    de dos desvíos estándar de la media.
    """

    diferencias = pd.Series(diferencias).dropna()

    media = diferencias.mean()
    desvio = diferencias.std(ddof=1)

    limite_inferior = media - k * desvio
    limite_superior = media + k * desvio

    dentro = diferencias[
        (diferencias >= limite_inferior) &
        (diferencias <= limite_superior)
    ]

    proporcion_observada = len(dentro) / len(diferencias)
    cota_minima = 1 - 1 / (k ** 2)

    return {
        "k": k,
        "media": media,
        "desvio": desvio,
        "limite_inferior": limite_inferior,
        "limite_superior": limite_superior,
        "proporcion_observada": proporcion_observada,
        "cota_minima_chebyshev": cota_minima,
        "interpretacion": (
            "Compara la proporción observada dentro de media ± k desvíos "
            "contra la cota mínima garantizada por Chebyshev."
        ),
    }


def resumen_empates(df):
    """
    Resume qué pasa con los empates.

    En fútbol, el empate es importante porque:
    - suma 1 punto para cada equipo.
    - no entra en la prueba binomial de victorias.
    - sí entra en chi-cuadrado y bondad de ajuste.

    Esta función deja explícito cómo se trataron los empates.
    """

    partidos = int(df["Home_MP"].sum())

    empates = int(df["Home_D"].sum())
    victorias_locales = int(df["Home_W"].sum())
    victorias_visitantes = int(df["Away_W"].sum())

    porcentaje_empates = empates / partidos * 100
    porcentaje_victorias_locales = victorias_locales / partidos * 100
    porcentaje_victorias_visitantes = victorias_visitantes / partidos * 100

    return {
        "partidos_totales": partidos,
        "victorias_locales": victorias_locales,
        "empates": empates,
        "victorias_visitantes": victorias_visitantes,
        "porcentaje_victorias_locales": porcentaje_victorias_locales,
        "porcentaje_empates": porcentaje_empates,
        "porcentaje_victorias_visitantes": porcentaje_victorias_visitantes,
        "tratamiento_en_binomial": (
            "Los empates se excluyen porque la binomial compara solo dos categorías: "
            "victoria local vs victoria visitante."
        ),
        "tratamiento_en_chi_cuadrado": (
            "Los empates se incluyen porque chi-cuadrado trabaja con la tabla completa "
            "victoria, empate y derrota."
        ),
    }


def ejecutar_inferencia(df):
    """
    Ejecuta todo el bloque inferencial del proyecto.

    Devuelve:
    - resultados: diccionario con pruebas estadísticas.
    - tabla_chi_obs: tabla observada para chi-cuadrado.
    - tabla_chi_esp: tabla esperada para chi-cuadrado.
    - zscores: tabla de z-score y percentiles por equipo.
    """

    diferencias_puntos = df["Delta_Pts_PJ"]
    diferencias_goles = df["Delta_GF_PJ"]

    # ========================================================
    # Intervalos y pruebas sobre medias
    # ========================================================
    ic_delta = intervalo_confianza_media_pareada(diferencias_puntos)

    t_puntos = prueba_t_pareada(
        df["Pts_PJ_Local"],
        df["Pts_PJ_Visitante"],
    )

    t_goles = prueba_t_pareada(
        df["GF_PJ_Local"],
        df["GF_PJ_Visitante"],
    )

    # ========================================================
    # No paramétricas
    # ========================================================
    wilcoxon_puntos = prueba_wilcoxon_pareada(
        df["Pts_PJ_Local"],
        df["Pts_PJ_Visitante"],
    )

    signo_puntos = prueba_del_signo(
        df["Pts_PJ_Local"],
        df["Pts_PJ_Visitante"],
    )

    # ========================================================
    # Proporciones y tablas
    # ========================================================
    binomial_victorias = prueba_binomial_victorias(df)

    chi = prueba_chi_cuadrado_resultados(df)
    chi_resultado = chi["resultado"]
    tabla_chi_obs = chi["observadas"]
    tabla_chi_esp = chi["esperadas"]

    bondad_ajuste = prueba_bondad_ajuste_resultados(df)

    # ========================================================
    # Varianza y normalidad
    # ========================================================
    varianza_delta = prueba_varianza_delta(diferencias_puntos)

    ks_normalidad = prueba_kolmogorov_smirnov_normalidad(diferencias_puntos)

    # ========================================================
    # Z-score, percentiles, Chebyshev y empates
    # ========================================================
    zscores = zscore_percentiles_localia(df)

    percentiles_delta = tabla_percentiles_delta(df)

    chebyshev = analisis_chebyshev(diferencias_puntos, k=2)

    empates = resumen_empates(df)

    resultados = {
        "intervalo_confianza_delta_puntos": ic_delta,
        "prueba_t_puntos": t_puntos,
        "prueba_t_goles": t_goles,
        "wilcoxon_puntos": wilcoxon_puntos,
        "prueba_signo_puntos": signo_puntos,
        "prueba_binomial_victorias": binomial_victorias,
        "chi_cuadrado_resultados": chi_resultado,
        "bondad_ajuste_resultados": bondad_ajuste,
        "prueba_varianza_delta": varianza_delta,
        "kolmogorov_smirnov_delta": ks_normalidad,
        "chebyshev": chebyshev,
        "resumen_empates": empates,
    }

    # Guardamos tablas auxiliares dentro del diccionario para que puedan usarse
    # más adelante si se desea generar reportes más completos.
    resultados["percentiles_delta"] = {
        "tabla": "Se exporta por separado desde main.py si se desea",
        "P10": float(percentiles_delta.loc[percentiles_delta["Percentil"] == "P10", "Valor_Delta_Pts_PJ"].iloc[0]),
        "P25": float(percentiles_delta.loc[percentiles_delta["Percentil"] == "P25", "Valor_Delta_Pts_PJ"].iloc[0]),
        "P50_mediana": float(percentiles_delta.loc[percentiles_delta["Percentil"] == "P50_mediana", "Valor_Delta_Pts_PJ"].iloc[0]),
        "P75": float(percentiles_delta.loc[percentiles_delta["Percentil"] == "P75", "Valor_Delta_Pts_PJ"].iloc[0]),
        "P90": float(percentiles_delta.loc[percentiles_delta["Percentil"] == "P90", "Valor_Delta_Pts_PJ"].iloc[0]),
    }

    return resultados, tabla_chi_obs, tabla_chi_esp, zscores