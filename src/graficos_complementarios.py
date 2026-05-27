import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

from src.config import GRAFICOS_DIR


# ============================================================
# GRÁFICOS COMPLEMENTARIOS DEL PROYECTO
# ============================================================
# Estos gráficos ayudan a cubrir más temas de Estadística Aplicada II:
#
# - Distribución muestral / descriptiva
# - Intervalos de confianza
# - Teorema de Chebyshev
# - Proporciones
# - Tablas r x c
# - Pruebas no paramétricas
# - Regresión simple
# - Ajuste curvilíneo
# - ANOVA por grupos
# ============================================================


def guardar_grafico(nombre_archivo):
    """
    Guarda el gráfico actual en la carpeta resultados/graficos.
    """

    ruta = GRAFICOS_DIR / nombre_archivo
    plt.tight_layout()
    plt.savefig(ruta, dpi=300, bbox_inches="tight")
    plt.close()
    return ruta


def grafico_valor_vs_puntos_local(df_plantilla):
    """
    Capítulo 5 - Regresión simple.
    Relación entre valor de plantilla y puntos por partido como local.
    """

    datos = df_plantilla[["ValorPlantillaM", "Pts_PJ_Local", "Equipo"]].dropna()

    x = datos["ValorPlantillaM"]
    y = datos["Pts_PJ_Local"]

    modelo = stats.linregress(x, y)

    x_linea = np.linspace(x.min(), x.max(), 100)
    y_linea = modelo.intercept + modelo.slope * x_linea

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y)
    plt.plot(x_linea, y_linea)

    for _, fila in datos.iterrows():
        if fila["ValorPlantillaM"] >= 50 or fila["Pts_PJ_Local"] >= 2.1:
            plt.text(
                fila["ValorPlantillaM"],
                fila["Pts_PJ_Local"],
                fila["Equipo"],
                fontsize=8
            )

    plt.title("Valor de plantilla vs puntos por partido como local")
    plt.xlabel("Valor de plantilla en millones de euros")
    plt.ylabel("Puntos por partido como local")
    plt.grid(True, alpha=0.3)

    texto = (
        f"R = {modelo.rvalue:.3f}\n"
        f"R² = {modelo.rvalue ** 2:.3f}\n"
        f"p = {modelo.pvalue:.4f}"
    )

    plt.text(
        0.02,
        0.95,
        texto,
        transform=plt.gca().transAxes,
        verticalalignment="top",
        bbox=dict(boxstyle="round", alpha=0.15)
    )

    return guardar_grafico("07_valor_vs_puntos_local_regresion.png")


def grafico_valor_vs_delta_localia(df_plantilla):
    """
    Capítulo 5 - Regresión simple.
    Relación entre valor de plantilla y ventaja de localía.
    """

    datos = df_plantilla[["ValorPlantillaM", "Delta_Pts_PJ", "Equipo"]].dropna()

    x = datos["ValorPlantillaM"]
    y = datos["Delta_Pts_PJ"]

    modelo = stats.linregress(x, y)

    x_linea = np.linspace(x.min(), x.max(), 100)
    y_linea = modelo.intercept + modelo.slope * x_linea

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y)
    plt.plot(x_linea, y_linea)
    plt.axhline(0, linestyle="--", linewidth=1)

    for _, fila in datos.iterrows():
        if fila["Delta_Pts_PJ"] >= 1.0 or fila["ValorPlantillaM"] >= 80:
            plt.text(
                fila["ValorPlantillaM"],
                fila["Delta_Pts_PJ"],
                fila["Equipo"],
                fontsize=8
            )

    plt.title("Valor de plantilla vs ventaja de localía")
    plt.xlabel("Valor de plantilla en millones de euros")
    plt.ylabel("Delta puntos por partido: local - visitante")
    plt.grid(True, alpha=0.3)

    texto = (
        f"R = {modelo.rvalue:.3f}\n"
        f"R² = {modelo.rvalue ** 2:.3f}\n"
        f"p = {modelo.pvalue:.4f}"
    )

    plt.text(
        0.02,
        0.95,
        texto,
        transform=plt.gca().transAxes,
        verticalalignment="top",
        bbox=dict(boxstyle="round", alpha=0.15)
    )

    return guardar_grafico("08_valor_vs_delta_localia_regresion.png")


def grafico_delta_por_grupo_economico(df_plantilla):
    """
    Capítulo 6 - ANOVA.
    Comparación de Delta_Pts_PJ entre grupos económicos.
    """

    datos = df_plantilla[["GrupoEconomico", "Delta_Pts_PJ"]].dropna()

    orden = ["Bajo", "Medio", "Alto"]
    grupos = [
        datos[datos["GrupoEconomico"].astype(str) == grupo]["Delta_Pts_PJ"]
        for grupo in orden
    ]

    plt.figure(figsize=(9, 6))
    plt.boxplot(grupos, labels=orden, showmeans=True)

    medias = [g.mean() for g in grupos]

    for i, media in enumerate(medias, start=1):
        plt.text(i, media, f"{media:.3f}", ha="center", va="bottom")

    plt.title("Ventaja de localía según grupo económico")
    plt.xlabel("Grupo económico según valor de plantilla")
    plt.ylabel("Delta puntos por partido")
    plt.grid(True, axis="y", alpha=0.3)

    return guardar_grafico("09_boxplot_delta_grupo_economico.png")


def grafico_intervalo_confianza_delta(resultados_inf):
    """
    Capítulo 1 y 2 - Intervalo de confianza.
    Muestra la media de Delta_Pts_PJ con su IC 95%.
    """

    ic = resultados_inf["intervalo_confianza_delta_puntos"]

    media = ic["media_diferencia"]
    inferior = ic["ic_inferior"]
    superior = ic["ic_superior"]

    error_inferior = media - inferior
    error_superior = superior - media

    plt.figure(figsize=(8, 5))
    plt.errorbar(
        x=[1],
        y=[media],
        yerr=[[error_inferior], [error_superior]],
        fmt="o",
        capsize=10
    )

    plt.axhline(0, linestyle="--", linewidth=1)
    plt.xlim(0.5, 1.5)
    plt.xticks([1], ["Delta_Pts_PJ"])
    plt.ylabel("Diferencia media de puntos por partido")
    plt.title("Intervalo de confianza del 95% para la ventaja de localía")
    plt.grid(True, axis="y", alpha=0.3)

    plt.text(
        1.05,
        media,
        f"Media = {media:.3f}\nIC 95% [{inferior:.3f}; {superior:.3f}]",
        va="center"
    )

    return guardar_grafico("10_intervalo_confianza_delta.png")


def grafico_chebyshev_delta(df, resultados_inf):
    """
    Capítulo 1 - Teorema de Chebyshev.
    Muestra media ± 2 desvíos sobre la distribución de Delta_Pts_PJ.
    """

    datos = df["Delta_Pts_PJ"].dropna()

    cheb = resultados_inf["chebyshev"]

    media = cheb["media"]
    inferior = cheb["limite_inferior"]
    superior = cheb["limite_superior"]

    plt.figure(figsize=(10, 6))
    plt.hist(datos, bins=8, edgecolor="black", alpha=0.7)

    plt.axvline(media, linestyle="-", linewidth=2, label=f"Media = {media:.3f}")
    plt.axvline(inferior, linestyle="--", linewidth=2, label=f"Media - 2s = {inferior:.3f}")
    plt.axvline(superior, linestyle="--", linewidth=2, label=f"Media + 2s = {superior:.3f}")

    plt.title("Distribución de la ventaja de localía y Teorema de Chebyshev")
    plt.xlabel("Delta puntos por partido")
    plt.ylabel("Cantidad de equipos")
    plt.legend()
    plt.grid(True, axis="y", alpha=0.3)

    return guardar_grafico("11_chebyshev_delta_localia.png")


def grafico_qqplot_delta(df):
    """
    Capítulo 1 y 4 - Normalidad / Kolmogorov-Smirnov como idea complementaria.
    Q-Q plot para observar si Delta_Pts_PJ se parece a una distribución normal.
    """

    datos = df["Delta_Pts_PJ"].dropna()

    plt.figure(figsize=(7, 7))
    stats.probplot(datos, dist="norm", plot=plt)

    plt.title("Q-Q plot de Delta_Pts_PJ")
    plt.grid(True, alpha=0.3)

    return guardar_grafico("12_qqplot_delta_localia.png")


def grafico_proporciones_resultados(tabla_global):
    """
    Capítulo 3 - Proporciones.
    Compara proporciones de victorias, empates y derrotas como local y visitante.
    """

    datos = tabla_global.copy()

    categorias = ["Pct_Victorias", "Pct_Empates", "Pct_Derrotas"]

    local = datos[datos["Condicion"] == "Local"][categorias].iloc[0].values
    visitante = datos[datos["Condicion"] == "Visitante"][categorias].iloc[0].values

    x = np.arange(len(categorias))
    ancho = 0.35

    plt.figure(figsize=(10, 6))
    plt.bar(x - ancho / 2, local, width=ancho, label="Local")
    plt.bar(x + ancho / 2, visitante, width=ancho, label="Visitante")

    plt.xticks(x, ["Victorias", "Empates", "Derrotas"])
    plt.ylabel("Porcentaje")
    plt.title("Proporciones de resultados: local vs visitante")
    plt.legend()
    plt.grid(True, axis="y", alpha=0.3)

    return guardar_grafico("13_proporciones_resultados_local_visitante.png")


def grafico_chi_cuadrado_observadas(tabla_chi_obs):
    """
    Capítulo 3 - Tabla r x c.
    Muestra la tabla observada usada en Chi-cuadrado.
    """

    tabla = tabla_chi_obs.copy()

    plt.figure(figsize=(8, 5))
    plt.imshow(tabla.values, aspect="auto")

    plt.xticks(np.arange(len(tabla.columns)), tabla.columns)
    plt.yticks(np.arange(len(tabla.index)), tabla.index)

    for i in range(tabla.shape[0]):
        for j in range(tabla.shape[1]):
            plt.text(j, i, int(tabla.values[i, j]), ha="center", va="center")

    plt.title("Tabla observada para prueba Chi-cuadrado")
    plt.xlabel("Resultado")
    plt.ylabel("Condición")

    return guardar_grafico("14_tabla_chi_cuadrado_observada.png")


def grafico_residuos_regresion(df_plantilla):
    """
    Capítulo 5 - Inferencias basadas en mínimos cuadrados.
    Gráfico de residuos para la regresión:
    ValorPlantillaM -> Pts_PJ_Local.
    """

    datos = df_plantilla[["ValorPlantillaM", "Pts_PJ_Local"]].dropna()

    x = datos["ValorPlantillaM"]
    y = datos["Pts_PJ_Local"]

    modelo = stats.linregress(x, y)
    y_estimado = modelo.intercept + modelo.slope * x
    residuos = y - y_estimado

    plt.figure(figsize=(10, 6))
    plt.scatter(y_estimado, residuos)
    plt.axhline(0, linestyle="--", linewidth=1)

    plt.title("Residuos de la regresión: valor de plantilla vs puntos como local")
    plt.xlabel("Valores estimados")
    plt.ylabel("Residuos")
    plt.grid(True, alpha=0.3)

    return guardar_grafico("15_residuos_regresion_valor_pts_local.png")


def grafico_ajuste_polinomico(df_plantilla):
    """
    Capítulo 5 - Regresión curvilínea / ajuste de polinomio.
    Ajuste cuadrático entre valor de plantilla y puntos por partido como local.
    """

    datos = df_plantilla[["ValorPlantillaM", "Pts_PJ_Local", "Equipo"]].dropna()

    x = datos["ValorPlantillaM"].values
    y = datos["Pts_PJ_Local"].values

    coef = np.polyfit(x, y, deg=2)
    polinomio = np.poly1d(coef)

    x_linea = np.linspace(x.min(), x.max(), 100)
    y_linea = polinomio(x_linea)

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y)
    plt.plot(x_linea, y_linea)

    plt.title("Ajuste curvilíneo: valor de plantilla vs puntos como local")
    plt.xlabel("Valor de plantilla en millones de euros")
    plt.ylabel("Puntos por partido como local")
    plt.grid(True, alpha=0.3)

    return guardar_grafico("16_ajuste_polinomico_valor_pts_local.png")


def grafico_media_delta_por_grupo(df_plantilla):
    """
    Capítulo 6 - ANOVA con tamaños muestrales distintos.
    Muestra la media de Delta_Pts_PJ para cada grupo económico.
    """

    datos = df_plantilla[["GrupoEconomico", "Delta_Pts_PJ"]].dropna()

    orden = ["Bajo", "Medio", "Alto"]

    medias = []
    errores = []

    for grupo in orden:
        valores = datos[datos["GrupoEconomico"].astype(str) == grupo]["Delta_Pts_PJ"]
        medias.append(valores.mean())

        if len(valores) > 1:
            error = stats.sem(valores)
        else:
            error = 0

        errores.append(error)

    plt.figure(figsize=(9, 6))
    plt.bar(orden, medias, yerr=errores, capsize=8)

    plt.title("Media de ventaja de localía por grupo económico")
    plt.xlabel("Grupo económico")
    plt.ylabel("Media de Delta_Pts_PJ")
    plt.grid(True, axis="y", alpha=0.3)

    for i, media in enumerate(medias):
        plt.text(i, media, f"{media:.3f}", ha="center", va="bottom")

    return guardar_grafico("17_media_delta_por_grupo_economico.png")


def generar_graficos_complementarios(
    df,
    df_plantilla,
    tabla_global,
    tabla_chi_obs,
    resultados_inf
):
    """
    Genera todos los gráficos complementarios.
    """

    GRAFICOS_DIR.mkdir(parents=True, exist_ok=True)

    rutas = []

    rutas.append(grafico_valor_vs_puntos_local(df_plantilla))
    rutas.append(grafico_valor_vs_delta_localia(df_plantilla))
    rutas.append(grafico_delta_por_grupo_economico(df_plantilla))
    rutas.append(grafico_intervalo_confianza_delta(resultados_inf))
    rutas.append(grafico_chebyshev_delta(df, resultados_inf))
    rutas.append(grafico_qqplot_delta(df))
    rutas.append(grafico_proporciones_resultados(tabla_global))
    rutas.append(grafico_chi_cuadrado_observadas(tabla_chi_obs))
    rutas.append(grafico_residuos_regresion(df_plantilla))
    rutas.append(grafico_ajuste_polinomico(df_plantilla))
    rutas.append(grafico_media_delta_por_grupo(df_plantilla))

    return rutas
