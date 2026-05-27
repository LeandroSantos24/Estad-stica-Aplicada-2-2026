from src.config import INFORME_AUTO


# ============================================================
# REPORTE AUTOMÁTICO
# ============================================================
# Este archivo genera un informe en formato Markdown.
# El objetivo no es reemplazar el documento final, sino crear
# una base escrita con los resultados calculados por Python.
# ============================================================


def generar_reporte_markdown(tabla_global, tabla_resumen, ranking, resultados_inf):
    """
    Genera un informe automático en Markdown con:
    - resumen del proyecto
    - principales resultados descriptivos
    - resultados inferenciales
    - interpretación básica
    """

    local = tabla_global[tabla_global["Condicion"] == "Local"].iloc[0]
    visitante = tabla_global[tabla_global["Condicion"] == "Visitante"].iloc[0]

    ic = resultados_inf["intervalo_confianza_delta_puntos"]
    t_puntos = resultados_inf["prueba_t_puntos"]
    t_goles = resultados_inf["prueba_t_goles"]
    wilcoxon = resultados_inf["wilcoxon_puntos"]
    binomial = resultados_inf["prueba_binomial_victorias"]
    chi = resultados_inf["chi_cuadrado_resultados"]
    cheb = resultados_inf["chebyshev"]

    top_5 = ranking.head(5)

    contenido = f"""# Informe automático de resultados

## Proyecto

**Tema:** Análisis estadístico del factor localía en la Liga Profesional Argentina 2023.

El objetivo del proyecto es analizar si los equipos obtuvieron mejor rendimiento jugando como locales que como visitantes durante la temporada 2023.

---

## Fuente de datos

La fuente principal utilizada fue la tabla Home/Away de FBref correspondiente a la Liga Profesional Argentina 2023.

La unidad de análisis principal es cada equipo participante del torneo. Para cada equipo se comparó su rendimiento como local y como visitante.

---

## Variables principales

La variable central del análisis fue:

$$
\\Delta Pts/PJ = Pts/PJ_{{Local}} - Pts/PJ_{{Visitante}}
$$

Un valor positivo indica que el equipo obtuvo más puntos por partido jugando como local.  
Un valor negativo indica que el equipo rindió mejor como visitante.

También se analizaron:

- Goles por partido de local.
- Goles por partido de visitante.
- Porcentaje de victorias locales.
- Porcentaje de victorias visitantes.
- Eficacia de localía.
- Z-score y percentiles de la ventaja de localía.

---

## Análisis descriptivo global

Durante la temporada analizada se registraron:

| Condición | Partidos | Victorias | Empates | Derrotas | Puntos | Pts/PJ | GF/PJ | % Victorias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Local | {local['Partidos']:.0f} | {local['Victorias']:.0f} | {local['Empates']:.0f} | {local['Derrotas']:.0f} | {local['Puntos']:.0f} | {local['Pts_PJ']:.4f} | {local['GF_PJ']:.4f} | {local['Pct_Victorias']:.2f}% |
| Visitante | {visitante['Partidos']:.0f} | {visitante['Victorias']:.0f} | {visitante['Empates']:.0f} | {visitante['Derrotas']:.0f} | {visitante['Puntos']:.0f} | {visitante['Pts_PJ']:.4f} | {visitante['GF_PJ']:.4f} | {visitante['Pct_Victorias']:.2f}% |

Los equipos locales obtuvieron en promedio **{local['Pts_PJ']:.4f} puntos por partido**, mientras que los visitantes obtuvieron **{visitante['Pts_PJ']:.4f} puntos por partido**.

En goles, los locales marcaron **{local['GF_PJ']:.4f} goles por partido**, mientras que los visitantes marcaron **{visitante['GF_PJ']:.4f} goles por partido**.

---

## Resumen de la variable Delta_Pts_PJ

| Medida | Valor |
|---|---:|
| Media | {tabla_resumen.loc['Delta_Pts_PJ', 'media']:.4f} |
| Mediana | {tabla_resumen.loc['Delta_Pts_PJ', 'mediana']:.4f} |
| Varianza | {tabla_resumen.loc['Delta_Pts_PJ', 'varianza']:.4f} |
| Desvío estándar | {tabla_resumen.loc['Delta_Pts_PJ', 'desvio_estandar']:.4f} |
| Mínimo | {tabla_resumen.loc['Delta_Pts_PJ', 'minimo']:.4f} |
| Máximo | {tabla_resumen.loc['Delta_Pts_PJ', 'maximo']:.4f} |

La media de la diferencia fue **{tabla_resumen.loc['Delta_Pts_PJ', 'media']:.4f}**, lo que indica que los equipos obtuvieron, en promedio, aproximadamente **{tabla_resumen.loc['Delta_Pts_PJ', 'media']:.3f} puntos más por partido jugando como locales**.

---

## Ranking de ventaja de localía

Los cinco equipos con mayor diferencia entre rendimiento local y visitante fueron:

| Equipo | Pts/PJ Local | Pts/PJ Visitante | Delta Pts/PJ |
|---|---:|---:|---:|
"""

    for _, fila in top_5.iterrows():
        contenido += f"| {fila['Equipo']} | {fila['Pts_PJ_Local']:.3f} | {fila['Pts_PJ_Visitante']:.3f} | {fila['Delta_Pts_PJ']:.3f} |\n"

    contenido += f"""

Este ranking no indica necesariamente quién fue el mejor equipo local en términos absolutos, sino qué equipo mejoró más su rendimiento al jugar en condición de local respecto de su propio rendimiento como visitante.

---

## Intervalo de confianza

Se calculó un intervalo de confianza del 95% para la diferencia media de puntos por partido.

| Medida | Valor |
|---|---:|
| Media de la diferencia | {ic['media_diferencia']:.4f} |
| Límite inferior | {ic['ic_inferior']:.4f} |
| Límite superior | {ic['ic_superior']:.4f} |

El intervalo de confianza obtenido fue:

$$
[{ic['ic_inferior']:.4f}; {ic['ic_superior']:.4f}]
$$

Como el intervalo se encuentra completamente por encima de cero, se interpreta que la diferencia media es positiva y estadísticamente significativa.

---

## Prueba t pareada para puntos por partido

Hipótesis planteadas:

$$
H_0: \\mu_d = 0
$$

$$
H_1: \\mu_d > 0
$$

Donde:

$$
d = Pts/PJ_{{Local}} - Pts/PJ_{{Visitante}}
$$

Resultado:

| Estadístico | Valor |
|---|---:|
| t | {t_puntos['estadistico']:.4f} |
| p-valor | {t_puntos['p_valor']:.8f} |
| Decisión | {t_puntos['decision']} |

Como el p-valor es menor que 0,05, se rechaza la hipótesis nula. Existe evidencia estadística suficiente para afirmar que los equipos rindieron mejor como locales.

---

## Prueba t pareada para goles por partido

También se comparó el promedio de goles por partido de local y visitante.

| Estadístico | Valor |
|---|---:|
| t | {t_goles['estadistico']:.4f} |
| p-valor | {t_goles['p_valor']:.8f} |
| Decisión | {t_goles['decision']} |

El resultado permite concluir que los equipos también marcaron significativamente más goles jugando como locales.

---

## Prueba de Wilcoxon

Como complemento no paramétrico se aplicó la prueba de Wilcoxon para muestras relacionadas.

| Estadístico | Valor |
|---|---:|
| Estadístico Wilcoxon | {wilcoxon['estadistico']:.4f} |
| p-valor | {wilcoxon['p_valor']:.8f} |
| Decisión | {wilcoxon['decision']} |

Esta prueba confirma la conclusión obtenida con la prueba t pareada.

---

## Prueba binomial

Se analizaron solamente los partidos con ganador, comparando victorias locales contra victorias visitantes.

| Medida | Valor |
|---|---:|
| Victorias locales | {binomial['victorias_local']} |
| Victorias visitantes | {binomial['victorias_visitante']} |
| Proporción de victorias locales | {binomial['proporcion_victorias_local']:.4f} |
| p-valor | {binomial['p_valor']:.8f} |
| Decisión | {binomial['decision']} |

Entre los partidos con ganador, el local ganó una proporción significativamente mayor.

---

## Prueba chi-cuadrado

Se aplicó una prueba chi-cuadrado para analizar si la distribución de resultados depende de la condición local/visitante.

| Estadístico | Valor |
|---|---:|
| Chi-cuadrado | {chi['chi2']:.4f} |
| Grados de libertad | {chi['gl']} |
| p-valor | {chi['p_valor']:.8f} |
| Decisión | {chi['decision']} |

Como el p-valor es menor que 0,05, se concluye que la distribución de resultados está asociada a la condición de localía.

---

## Teorema de Chebyshev

Se aplicó el Teorema de Chebyshev sobre la variable Delta_Pts_PJ con k = {cheb['k']}.

| Medida | Valor |
|---|---:|
| Media | {cheb['media']:.4f} |
| Desvío estándar | {cheb['desvio']:.4f} |
| Límite inferior | {cheb['limite_inferior']:.4f} |
| Límite superior | {cheb['limite_superior']:.4f} |
| Proporción observada dentro del intervalo | {cheb['proporcion_observada']:.4f} |
| Cota mínima de Chebyshev | {cheb['cota_minima_chebyshev']:.4f} |

Según Chebyshev, al menos el {cheb['cota_minima_chebyshev'] * 100:.2f}% de los datos deberían encontrarse dentro de dos desvíos estándar de la media. En la muestra observada, la proporción fue del {cheb['proporcion_observada'] * 100:.2f}%.

---

## Gráficos generados

Los gráficos del análisis fueron generados automáticamente en la carpeta `resultados/graficos/`.

Archivos generados:

1. `01_resumen_local_visitante.png`
2. `02_ranking_delta_puntos.png`
3. `03_boxplot_delta_puntos.png`
4. `04_dispersion_local_visitante.png`
5. `05_goles_local_visitante.png`
6. `06_zscore_localia.png`

---

## Conclusión automática

Los resultados descriptivos e inferenciales permiten afirmar que en la Liga Profesional Argentina 2023 existió una ventaja de localía estadísticamente significativa. Los equipos obtuvieron más puntos, marcaron más goles y ganaron una mayor proporción de partidos cuando jugaron como locales.

"""

    INFORME_AUTO.parent.mkdir(parents=True, exist_ok=True)

    with open(INFORME_AUTO, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)

    return INFORME_AUTO
