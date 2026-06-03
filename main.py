import pandas as pd

from src.cargar_datos import cargar_tablas_fbref, cargar_valores_plantilla
from src.preparar_datos import preparar_base_limpia
from src.estadistica_descriptiva import (
    resumen_local_vs_visitante,
    ranking_localia,
    resumen_global_resultados,
    tabla_percentiles_localia,
    resumen_empates,
    tabla_formulas_principales,
    glosario_estadistico,
)
from src.inferencia import ejecutar_inferencia
from src.graficos import generar_todos_los_graficos
from src.graficos_complementarios import generar_graficos_complementarios
from src.reporte import generar_reporte_markdown
from src.analisis_plantilla import ejecutar_analisis_plantilla
from src.config import TABLAS_DIR, GRAFICOS_DIR


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

    Evita guardar directamente DataFrames dentro del CSV principal,
    porque esos objetos se exportan mejor como tablas auxiliares separadas.
    """

    resultados_planos = []

    for nombre_bloque, bloque in resultados.items():
        for clave, valor in bloque.items():
            if isinstance(valor, pd.DataFrame):
                valor_exportado = "Tabla auxiliar exportada por separado"
            else:
                valor_exportado = valor

            resultados_planos.append(
                {
                    "bloque": nombre_bloque,
                    "medida": clave,
                    "valor": valor_exportado,
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
    print(f"n = {ic['n']}")
    print(f"Media diferencia: {ic['media_diferencia']:.4f}")
    print(f"Desvío diferencia: {ic['desvio_diferencia']:.4f}")
    print(f"Error estándar: {ic['error_estandar']:.4f}")
    print(f"IC 95%: [{ic['ic_inferior']:.4f} ; {ic['ic_superior']:.4f}]")

    t_puntos = resultados_inf["prueba_t_puntos"]
    print("\nPrueba t pareada - Puntos por partido:")
    print(f"H0: {t_puntos['hipotesis_nula']}")
    print(f"H1: {t_puntos['hipotesis_alternativa']}")
    print(f"t = {t_puntos['estadistico']:.4f}")
    print(f"p-valor = {t_puntos['p_valor']:.8f}")
    print(f"Decisión: {t_puntos['decision']}")

    t_goles = resultados_inf["prueba_t_goles"]
    print("\nPrueba t pareada - Goles por partido:")
    print(f"H0: {t_goles['hipotesis_nula']}")
    print(f"H1: {t_goles['hipotesis_alternativa']}")
    print(f"t = {t_goles['estadistico']:.4f}")
    print(f"p-valor = {t_goles['p_valor']:.8f}")
    print(f"Decisión: {t_goles['decision']}")

    wilcoxon = resultados_inf["wilcoxon_puntos"]
    print("\nPrueba Wilcoxon - Puntos por partido:")
    print(f"H0: {wilcoxon['hipotesis_nula']}")
    print(f"H1: {wilcoxon['hipotesis_alternativa']}")
    print(f"estadístico = {wilcoxon['estadistico']:.4f}")
    print(f"p-valor = {wilcoxon['p_valor']:.8f}")
    print(f"Decisión: {wilcoxon['decision']}")

    signo = resultados_inf["prueba_signo_puntos"]
    print("\nPrueba del signo - Puntos por partido:")
    print(f"Positivos: {signo['positivos']}")
    print(f"Negativos: {signo['negativos']}")
    print(f"Ceros excluidos: {signo['ceros_excluidos']}")
    print(f"n utilizado = {signo['n_utilizado']}")
    print(f"p-valor = {signo['p_valor']:.8f}")
    print(f"Decisión: {signo['decision']}")

    binomial = resultados_inf["prueba_binomial_victorias"]
    print("\nPrueba binomial - Victorias locales vs visitantes:")
    print(f"Victorias locales: {binomial['victorias_local']}")
    print(f"Victorias visitantes: {binomial['victorias_visitante']}")
    print(f"Empates excluidos en esta prueba: {binomial['empates_excluidos']}")
    print(f"Proporción victorias locales: {binomial['proporcion_victorias_local']:.4f}")
    print(f"p-valor = {binomial['p_valor']:.8f}")
    print(f"Decisión: {binomial['decision']}")

    chi = resultados_inf["chi_cuadrado_resultados"]
    print("\nChi-cuadrado - Distribución de resultados:")
    print(f"H0: {chi['hipotesis_nula']}")
    print(f"chi2 = {chi['chi2']:.4f}")
    print(f"gl = {chi['gl']}")
    print(f"p-valor = {chi['p_valor']:.8f}")
    print(f"Decisión: {chi['decision']}")

    bondad = resultados_inf["bondad_ajuste_resultados"]
    print("\nBondad de ajuste - Resultados globales:")
    print(f"H0: {bondad['hipotesis_nula']}")
    print(f"chi2 = {bondad['chi2']:.4f}")
    print(f"gl = {bondad['gl']}")
    print(f"p-valor = {bondad['p_valor']:.8f}")
    print(f"Decisión: {bondad['decision']}")

    varianza = resultados_inf["prueba_varianza_delta"]
    print("\nPrueba de hipótesis sobre una varianza:")
    print(f"Variable: {varianza['variable']}")
    print(f"Varianza muestral = {varianza['varianza_muestral']:.4f}")
    print(f"Varianza hipotética = {varianza['varianza_hipotetica']:.4f}")
    print(f"chi2 = {varianza['chi2']:.4f}")
    print(f"gl = {varianza['gl']}")
    print(f"p-valor = {varianza['p_valor']:.8f}")
    print(f"Decisión: {varianza['decision']}")

    ks = resultados_inf["kolmogorov_smirnov_delta"]
    print("\nKolmogorov-Smirnov - Normalidad de Delta_Pts_PJ:")
    print(f"Estadístico = {ks['estadistico']:.4f}")
    print(f"p-valor = {ks['p_valor']:.8f}")
    print(f"Decisión: {ks['decision']}")

    cheb = resultados_inf["chebyshev"]
    print("\nTeorema de Chebyshev sobre Delta_Pts_PJ:")
    print(f"k = {cheb['k']}")
    print(f"Media = {cheb['media']:.4f}")
    print(f"Desvío = {cheb['desvio']:.4f}")
    print(f"Intervalo = [{cheb['limite_inferior']:.4f} ; {cheb['limite_superior']:.4f}]")
    print(f"Proporción observada dentro del intervalo = {cheb['proporcion_observada']:.4f}")
    print(f"Cota mínima de Chebyshev = {cheb['cota_minima_chebyshev']:.4f}")

    percentiles = resultados_inf["percentiles_delta"]
    print("\nPercentiles de Delta_Pts_PJ:")
    print(f"P10 = {percentiles['P10']:.4f}")
    print(f"P25 = {percentiles['P25']:.4f}")
    print(f"P50 / Mediana = {percentiles['P50_mediana']:.4f}")
    print(f"P75 = {percentiles['P75']:.4f}")
    print(f"P90 = {percentiles['P90']:.4f}")

    empates = resultados_inf["resumen_empates"]
    print("\nResumen de empates:")
    print(f"Partidos totales: {empates['partidos_totales']}")
    print(f"Victorias locales: {empates['victorias_locales']}")
    print(f"Empates: {empates['empates']}")
    print(f"Victorias visitantes: {empates['victorias_visitantes']}")
    print(f"% Empates: {empates['porcentaje_empates']:.4f}")


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

    tabla_percentiles = tabla_percentiles_localia(df)
    tabla_empates = resumen_empates(df)
    tabla_formulas = tabla_formulas_principales()
    tabla_glosario = glosario_estadistico()

    tabla_resumen.to_csv(TABLAS_DIR / "resumen_descriptivo.csv")
    tabla_ranking.to_csv(TABLAS_DIR / "ranking_localia.csv", index=False)
    tabla_global.to_csv(TABLAS_DIR / "resumen_global_resultados.csv", index=False)

    tabla_percentiles.to_csv(TABLAS_DIR / "tabla_percentiles_localia.csv", index=False)
    tabla_empates.to_csv(TABLAS_DIR / "resumen_empates.csv", index=False)
    tabla_formulas.to_csv(TABLAS_DIR / "formulas_principales.csv", index=False)
    tabla_glosario.to_csv(TABLAS_DIR / "glosario_estadistico.csv", index=False)

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
            [
                "Equipo",
                "Pts_PJ_Local",
                "Pts_PJ_Visitante",
                "Delta_Pts_PJ",
                "Percentil_Localia",
                "Clasificacion_Localia",
            ]
        ].round(3)
    )

    print("\nPERCENTILES DE LOCALÍA")
    print("----------------------")
    print(tabla_percentiles.round(4))

    print("\nRESUMEN DE EMPATES")
    print("------------------")
    print(tabla_empates.round(4))

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

    # Tabla auxiliar de bondad de ajuste
    if "tabla" in resultados_inf["bondad_ajuste_resultados"]:
        resultados_inf["bondad_ajuste_resultados"]["tabla"].to_csv(
            TABLAS_DIR / "bondad_ajuste_observados_esperados.csv",
            index=False,
        )

    salida_inferencia = guardar_resultados_diccionario(
        resultados_inf,
        "resultados_inferencia.csv",
    )

    mostrar_resultados_inferencia(resultados_inf)

    print("\nZ-score y percentiles exportados en:")
    print(TABLAS_DIR / "zscore_percentiles_localia.csv")

    print("\nResultados inferenciales exportados en:")
    print(salida_inferencia)

    print("\nTabla de bondad de ajuste exportada en:")
    print(TABLAS_DIR / "bondad_ajuste_observados_esperados.csv")

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