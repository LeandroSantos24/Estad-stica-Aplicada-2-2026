import matplotlib
matplotlib.use("Agg")  # Para guardar imágenes sin abrir ventanas

import matplotlib.pyplot as plt
import numpy as np

from src.config import GRAFICOS_DIR


# ============================================================
# GRÁFICOS DEL PROYECTO
# ============================================================
# Este archivo genera las imágenes del trabajo:
#
# 1. Resumen local vs visitante.
# 2. Ranking de localía.
# 3. Boxplot de puntos por partido.
# 4. Dispersión local vs visitante.
# 5. Comparación de goles por partido.
# 6. Z-score de localía.
# ============================================================


def grafico_resumen_local_visitante(tabla_global):
    """
    Genera un gráfico resumen comparando local vs visitante
    en tres medidas:
    - puntos por partido
    - goles por partido
    - porcentaje de victorias
    """

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    condiciones = tabla_global["Condicion"]

    # 1. Puntos por partido
    axes[0].bar(condiciones, tabla_global["Pts_PJ"])
    axes[0].set_title("Puntos por partido")
    axes[0].set_ylabel("Pts/PJ")

    for i, v in enumerate(tabla_global["Pts_PJ"]):
        axes[0].text(i, v + 0.02, f"{v:.3f}", ha="center")

    # 2. Goles por partido
    axes[1].bar(condiciones, tabla_global["GF_PJ"])
    axes[1].set_title("Goles por partido")
    axes[1].set_ylabel("GF/PJ")

    for i, v in enumerate(tabla_global["GF_PJ"]):
        axes[1].text(i, v + 0.02, f"{v:.3f}", ha="center")

    # 3. Porcentaje de victorias
    axes[2].bar(condiciones, tabla_global["Pct_Victorias"])
    axes[2].set_title("% de victorias")
    axes[2].set_ylabel("Porcentaje")

    for i, v in enumerate(tabla_global["Pct_Victorias"]):
        axes[2].text(i, v + 0.5, f"{v:.2f}%", ha="center")

    fig.suptitle("Resumen global: Local vs Visitante", fontsize=14)
    plt.tight_layout()

    salida = GRAFICOS_DIR / "01_resumen_local_visitante.png"
    plt.savefig(salida, dpi=300, bbox_inches="tight")
    plt.close()


def grafico_ranking_localia(df):
    """
    Genera un ranking horizontal de la ventaja de localía
    según Delta_Pts_PJ.
    """

    ranking = df.sort_values("Delta_Pts_PJ", ascending=True)

    plt.figure(figsize=(10, 10))
    plt.barh(ranking["Equipo"], ranking["Delta_Pts_PJ"])
    plt.axvline(0, linestyle="--")
    plt.title("Ranking de localía según ΔPts/PJ")
    plt.xlabel("ΔPts/PJ = Pts/PJ Local - Pts/PJ Visitante")
    plt.ylabel("Equipo")
    plt.tight_layout()

    salida = GRAFICOS_DIR / "02_ranking_delta_puntos.png"
    plt.savefig(salida, dpi=300, bbox_inches="tight")
    plt.close()


def grafico_boxplot_puntos(df):
    """
    Genera boxplots para comparar:
    - puntos por partido de local
    - puntos por partido de visitante
    - diferencia entre ambos
    """

    datos = [
        df["Pts_PJ_Local"],
        df["Pts_PJ_Visitante"],
        df["Delta_Pts_PJ"],
    ]

    etiquetas = [
        "Pts/PJ Local",
        "Pts/PJ Visitante",
        "ΔPts/PJ",
    ]

    plt.figure(figsize=(8, 6))
    plt.boxplot(datos, tick_labels=etiquetas)
    plt.title("Distribución de puntos por partido y diferencia")
    plt.ylabel("Valor")
    plt.tight_layout()

    salida = GRAFICOS_DIR / "03_boxplot_delta_puntos.png"
    plt.savefig(salida, dpi=300, bbox_inches="tight")
    plt.close()


def grafico_dispersion_local_visitante(df):
    """
    Genera un gráfico de dispersión comparando
    puntos por partido de visitante vs local.
    """

    x = df["Pts_PJ_Visitante"]
    y = df["Pts_PJ_Local"]

    plt.figure(figsize=(8, 8))
    plt.scatter(x, y)

    # Línea de igualdad y = x
    minimo = min(x.min(), y.min()) - 0.1
    maximo = max(x.max(), y.max()) + 0.1
    plt.plot([minimo, maximo], [minimo, maximo], linestyle="--")

    for _, fila in df.iterrows():
        plt.text(fila["Pts_PJ_Visitante"] + 0.01, fila["Pts_PJ_Local"] + 0.01, fila["Equipo"], fontsize=7)

    plt.title("Dispersión: Pts/PJ Visitante vs Pts/PJ Local")
    plt.xlabel("Pts/PJ Visitante")
    plt.ylabel("Pts/PJ Local")
    plt.xlim(minimo, maximo)
    plt.ylim(minimo, maximo)
    plt.tight_layout()

    salida = GRAFICOS_DIR / "04_dispersion_local_visitante.png"
    plt.savefig(salida, dpi=300, bbox_inches="tight")
    plt.close()


def grafico_goles_local_visitante(df):
    """
    Genera un gráfico comparando goles por partido
    de local y visitante por equipo.
    """

    ordenado = df.sort_values("GF_PJ_Local", ascending=False)

    x = np.arange(len(ordenado))
    ancho = 0.4

    plt.figure(figsize=(14, 6))
    plt.bar(x - ancho/2, ordenado["GF_PJ_Local"], width=ancho, label="Local")
    plt.bar(x + ancho/2, ordenado["GF_PJ_Visitante"], width=ancho, label="Visitante")

    plt.xticks(x, ordenado["Equipo"], rotation=90)
    plt.title("Goles por partido: Local vs Visitante")
    plt.xlabel("Equipo")
    plt.ylabel("Goles por partido")
    plt.legend()
    plt.tight_layout()

    salida = GRAFICOS_DIR / "05_goles_local_visitante.png"
    plt.savefig(salida, dpi=300, bbox_inches="tight")
    plt.close()


def grafico_zscore_localia(zscores):
    """
    Genera un gráfico horizontal con Z-score de la ventaja de localía.
    """

    z = zscores.sort_values("Z_Delta_Pts_PJ", ascending=True)

    plt.figure(figsize=(10, 10))
    plt.barh(z["Equipo"], z["Z_Delta_Pts_PJ"])
    plt.axvline(0, linestyle="--")
    plt.axvline(1, linestyle=":")
    plt.axvline(2, linestyle=":")
    plt.axvline(-1, linestyle=":")
    plt.axvline(-2, linestyle=":")
    plt.title("Z-score de la ventaja de localía")
    plt.xlabel("Z-score")
    plt.ylabel("Equipo")
    plt.tight_layout()

    salida = GRAFICOS_DIR / "06_zscore_localia.png"
    plt.savefig(salida, dpi=300, bbox_inches="tight")
    plt.close()


def generar_todos_los_graficos(df, tabla_global, zscores):
    """
    Ejecuta todos los gráficos del proyecto.
    """

    GRAFICOS_DIR.mkdir(parents=True, exist_ok=True)

    grafico_resumen_local_visitante(tabla_global)
    grafico_ranking_localia(df)
    grafico_boxplot_puntos(df)
    grafico_dispersion_local_visitante(df)
    grafico_goles_local_visitante(df)
    grafico_zscore_localia(zscores)
