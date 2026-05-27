import pandas as pd

from src.cargar_datos import cargar_tablas_fbref, cargar_valores_plantilla
from src.preparar_datos import preparar_base_limpia
from src.estadistica_descriptiva import (
    resumen_local_vs_visitante,
    ranking_localia,
    resumen_global_resultados,
)
from src.inferencia import ejecutar_inferencia
from src.graficos import generar_todos_los_graficos
from src.reporte import generar_reporte_markdown
from src.analisis_plantilla import ejecutar_analisis_plantilla
from src.config import TABLAS_DIR, GRAFICOS_DIR
from src.graficos_complementarios import generar_graficos_complementarios


# ============================================================
# ARCHIVO PRINCIPAL DEL PROYECTO
# ============================================================
# Este archivo ejecuta todo el flujo del proyecto:
#
# 1. Carga datos reales desde FBref.
# 2. Prepara la base limpia de localía.
# 3. Calcula estadística descriptiva.
# 4. Ejecuta análisis económico con valor de plantilla.
# 5. Ejecuta inferencia estadística.
# 6. Genera gráficos.
# 7. Genera informe automático.
# ============================================================


def guardar_resultados_diccionario(resultados, nombre_archivo):
    """
    Convierte un diccionario de resultados en una tabla CSV.
    Sirve para guardar resultados de inferencia o de análisis económico.
    """

    resultados_planos = []

    for nombre_bloque, bloque in resultados.items():
        for clave, valor in bloque.items():
            resultados_planos.append(
                {
                    "bloque": nombre_bloque,
                    "medida": clave,
                    "valor": valor,
                }
            )

    df_resultados = pd.DataFrame(resultados_planos)
    salida = TABLAS_DIR / nombre_archivo
    df_resultados.to_csv(salida, index=False)

    return salida


def mostrar_resultados_inferencia(resultados_inf):
    """
    Muestra en pantalla los resultados principales de inferencia estadística.
    """

    print("\nINFERENCIA ESTADÍSTICA")
    print("----------------------")

    ic = resultados_inf["intervalo_confianza_delta_puntos"]
    print("\nIntervalo de confianza para Delta_Pts_PJ:")
    print(f"Media diferencia: {ic['media_diferencia']:.4f}")
    print(f"IC 95%: [{ic['ic_inferior']:.4f} ; {ic['ic_superior']:.4f}]")

    t_puntos = resultados_inf["prueba_t_puntos"]
    print("\nPrueba t pareada - Puntos por partido:")
    print(f"t = {t_puntos['estadistico']:.4f}")
    print(f"p-valor = {t_puntos['p_valor']:.8f}")
    print(f"Decisión: {t_puntos['decision']}")

    t_goles = resultados_inf["prueba_t_goles"]
    print("\nPrueba t pareada - Goles por partido:")
    print(f"t = {t_goles['estadistico']:.4f}")
    print(f"p-valor = {t_goles['p_valor']:.8f}")
    print(f"Decisión: {t_goles['decision']}")

    wilcoxon = resultados_inf["wilcoxon_puntos"]
    print("\nPrueba Wilcoxon - Puntos por partido:")
    print(f"estadístico = {wilcoxon['estadistico']:.4f}")
    print(f"p-valor = {wilcoxon['p_valor']:.8f}")
    print(f"Decisión: {wilcoxon['decision']}")

    binomial = resultados_inf["prueba_binomial_victorias"]
    print("\nPrueba binomial - Victorias locales vs visitantes:")
    print(f"Victorias locales: {binomial['victorias_local']}")
    print(f"Victorias visitantes: {binomial['victorias_visitante']}")
    print(f"Proporción victorias locales: {binomial['proporcion_victorias_local']:.4f}")
    print(f"p-valor = {binomial['p_valor']:.8f}")
    print(f"Decisión: {binomial['decision']}")

    chi = resultados_inf["chi_cuadrado_resultados"]
    print("\nChi-cuadrado - Distribución de resultados:")
    print(f"chi2 = {chi['chi2']:.4f}")
    print(f"gl = {chi['gl']}")
    print(f"p-valor = {chi['p_valor']:.8f}")
    print(f"Decisión: {chi['decision']}")

    cheb = resultados_inf["chebyshev"]
    print("\nTeorema de Chebyshev sobre Delta_Pts_PJ:")
    print(f"k = {cheb['k']}")
    print(f"Media = {cheb['media']:.4f}")
    print(f"Desvío = {cheb['desvio']:.4f}")
    print(f"Intervalo = [{cheb['limite_inferior']:.4f} ; {cheb['limite_superior']:.4f}]")
    print(f"Proporción observada dentro del intervalo = {cheb['proporcion_observada']:.4f}")
    print(f"Cota mínima de Chebyshev = {cheb['cota_minima_chebyshev']:.4f}")


def mostrar_resultados_plantilla(correlaciones_plant, resumen_grupos, resultados_plant):
    """
    Muestra en pantalla el análisis económico del proyecto.
    """

    print("\nANÁLISIS DE VALOR DE PLANTILLA")
    print("------------------------------")

    print("\nCorrelaciones entre valor de plantilla y variables deportivas:")
    print(correlaciones_plant.round(4))

    print("\nResumen por grupo económico:")
    print(resumen_grupos.round(4))

    print("\nRegresión simple: ValorPlantillaM -> Delta_Pts_PJ")
    regresion_delta = resultados_plant["regresion_delta"]
    print(f"Intercepto = {regresion_delta['Intercepto']:.4f}")
    print(f"Pendiente = {regresion_delta['Pendiente']:.6f}")
    print(f"R = {regresion_delta['R']:.4f}")
    print(f"R2 = {regresion_delta['R2']:.4f}")
    print(f"p-valor = {regresion_delta['p_valor']:.8f}")

    print("\nRegresión simple: ValorPlantillaM -> Pts_PJ_Local")
    regresion_local = resultados_plant["regresion_local"]
    print(f"Intercepto = {regresion_local['Intercepto']:.4f}")
    print(f"Pendiente = {regresion_local['Pendiente']:.6f}")
    print(f"R = {regresion_local['R']:.4f}")
    print(f"R2 = {regresion_local['R2']:.4f}")
    print(f"p-valor = {regresion_local['p_valor']:.8f}")

    print("\nANOVA por grupos económicos:")
    anova = resultados_plant["anova_grupos"]
    print(f"F = {anova['F']:.4f}")
    print(f"p-valor = {anova['p_valor']:.8f}")
    print(f"Decisión = {anova['decision']}")

    print("\nKruskal-Wallis por grupos económicos:")
    kruskal = resultados_plant["kruskal_grupos"]
    print(f"H = {kruskal['H']:.4f}")
    print(f"p-valor = {kruskal['p_valor']:.8f}")
    print(f"Decisión = {kruskal['decision']}")


def main():
    print("\n==============================================")
    print("PROYECTO FINAL - ESTADÍSTICA APLICADA II")
    print("Factor localía - Liga Profesional Argentina 2023")
    print("==============================================")

    # Crear carpetas de salida
    TABLAS_DIR.mkdir(parents=True, exist_ok=True)
    GRAFICOS_DIR.mkdir(parents=True, exist_ok=True)

    # ========================================================
    # 1. CARGA DE DATOS
    # ========================================================
    tablas = cargar_tablas_fbref()
    cargar_valores_plantilla()

    # ========================================================
    # 2. PREPARACIÓN DE BASE LIMPIA
    # ========================================================
    df = preparar_base_limpia(tablas)

    salida_base = TABLAS_DIR / "base_localia_lpf_2023.csv"
    df.to_csv(salida_base, index=False)

    print("\nBase limpia exportada correctamente en:")
    print(salida_base)

    # ========================================================
    # 3. ESTADÍSTICA DESCRIPTIVA
    # ========================================================
    tabla_resumen = resumen_local_vs_visitante(df)
    tabla_ranking = ranking_localia(df)
    tabla_global = resumen_global_resultados(df)

    tabla_resumen.to_csv(TABLAS_DIR / "resumen_descriptivo.csv")
    tabla_ranking.to_csv(TABLAS_DIR / "ranking_localia.csv", index=False)
    tabla_global.to_csv(TABLAS_DIR / "resumen_global_resultados.csv", index=False)

    print("\nRESUMEN GLOBAL LOCAL VS VISITANTE")
    print("--------------------------------")
    print(tabla_global.round(4))

    print("\nRESUMEN DESCRIPTIVO")
    print("-------------------")
    print(tabla_resumen.round(4))

    print("\nRANKING DE LOCALÍA")
    print("------------------")
    print(
        tabla_ranking[
            ["Equipo", "Pts_PJ_Local", "Pts_PJ_Visitante", "Delta_Pts_PJ"]
        ].round(3)
    )

    print("\nTablas descriptivas exportadas correctamente en:")
    print(TABLAS_DIR)

    # ========================================================
    # 4. ANÁLISIS DE VALOR DE PLANTILLA
    # ========================================================
    df_plantilla, correlaciones_plant, resumen_grupos, resultados_plant = (
        ejecutar_analisis_plantilla(df)
    )

    df_plantilla.to_csv(
        TABLAS_DIR / "base_localia_plantilla_2023.csv",
        index=False,
    )

    correlaciones_plant.to_csv(
        TABLAS_DIR / "correlaciones_plantilla.csv",
        index=False,
    )

    resumen_grupos.to_csv(
        TABLAS_DIR / "resumen_grupos_economicos.csv",
        index=False,
    )

    salida_resultados_plantilla = guardar_resultados_diccionario(
        resultados_plant,
        "resultados_analisis_plantilla.csv",
    )

    mostrar_resultados_plantilla(
        correlaciones_plant=correlaciones_plant,
        resumen_grupos=resumen_grupos,
        resultados_plant=resultados_plant,
    )

    print("\nResultados de análisis de plantilla exportados en:")
    print(salida_resultados_plantilla)

    # ========================================================
    # 5. INFERENCIA ESTADÍSTICA
    # ========================================================
    resultados_inf, tabla_chi_obs, tabla_chi_esp, zscores = ejecutar_inferencia(df)

    tabla_chi_obs.to_csv(TABLAS_DIR / "chi_cuadrado_observadas.csv")
    tabla_chi_esp.to_csv(TABLAS_DIR / "chi_cuadrado_esperadas.csv")
    zscores.to_csv(TABLAS_DIR / "zscore_percentiles_localia.csv", index=False)

    salida_inferencia = guardar_resultados_diccionario(
        resultados_inf,
        "resultados_inferencia.csv",
    )

    mostrar_resultados_inferencia(resultados_inf)

    print("\nZ-score y percentiles exportados en:")
    print(TABLAS_DIR / "zscore_percentiles_localia.csv")

    print("\nResultados inferenciales exportados en:")
    print(salida_inferencia)

    # ========================================================
    # 6. GRÁFICOS
    # ========================================================
    generar_todos_los_graficos(df, tabla_global, zscores)

    rutas_complementarias = generar_graficos_complementarios(
        df=df,
        df_plantilla=df_plantilla,
        tabla_global=tabla_global,
        tabla_chi_obs=tabla_chi_obs,
        resultados_inf=resultados_inf,
    )

    print("\nGRÁFICOS GENERADOS")
    print("------------------")
    print(GRAFICOS_DIR / "01_resumen_local_visitante.png")
    print(GRAFICOS_DIR / "02_ranking_delta_puntos.png")
    print(GRAFICOS_DIR / "03_boxplot_delta_puntos.png")
    print(GRAFICOS_DIR / "04_dispersion_local_visitante.png")
    print(GRAFICOS_DIR / "05_goles_local_visitante.png")
    print(GRAFICOS_DIR / "06_zscore_localia.png")

    print("\nGRÁFICOS COMPLEMENTARIOS GENERADOS")
    print("----------------------------------")
    for ruta in rutas_complementarias:
        print(ruta)
        
    # ========================================================
    # 7. REPORTE AUTOMÁTICO
    # ========================================================
    informe = generar_reporte_markdown(
        tabla_global=tabla_global,
        tabla_resumen=tabla_resumen,
        ranking=tabla_ranking,
        resultados_inf=resultados_inf,
    )

    print("\nREPORTE AUTOMÁTICO GENERADO")
    print("--------------------------")
    print(informe)

    print("\n==============================================")
    print("PROCESO FINALIZADO CORRECTAMENTE")
    print("Ya tenemos tablas, gráficos e informe automático.")
    print("==============================================")


if __name__ == "__main__":
    main()