# Informe automático de resultados

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
\Delta Pts/PJ = Pts/PJ_{Local} - Pts/PJ_{Visitante}
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
| Local | 378 | 169 | 121 | 88 | 628 | 1.6614 | 1.2037 | 44.71% |
| Visitante | 378 | 88 | 121 | 169 | 385 | 1.0185 | 0.8545 | 23.28% |

Los equipos locales obtuvieron en promedio **1.6614 puntos por partido**, mientras que los visitantes obtuvieron **1.0185 puntos por partido**.

En goles, los locales marcaron **1.2037 goles por partido**, mientras que los visitantes marcaron **0.8545 goles por partido**.

---

## Resumen de la variable Delta_Pts_PJ

| Medida | Valor |
|---|---:|
| Media | 0.6413 |
| Mediana | 0.6319 |
| Varianza | 0.1095 |
| Desvío estándar | 0.3309 |
| Mínimo | -0.1374 |
| Máximo | 1.5165 |

La media de la diferencia fue **0.6413**, lo que indica que los equipos obtuvieron, en promedio, aproximadamente **0.641 puntos más por partido jugando como locales**.

---

## Ranking de ventaja de localía

Los cinco equipos con mayor diferencia entre rendimiento local y visitante fueron:

| Equipo | Pts/PJ Local | Pts/PJ Visitante | Delta Pts/PJ |
|---|---:|---:|---:|
| Rosario Central | 2.286 | 0.769 | 1.516 |
| Godoy Cruz | 2.154 | 0.929 | 1.225 |
| Lanús | 2.231 | 1.143 | 1.088 |
| Newell's Old Boys | 1.846 | 0.786 | 1.060 |
| River Plate | 2.769 | 1.786 | 0.984 |


Este ranking no indica necesariamente quién fue el mejor equipo local en términos absolutos, sino qué equipo mejoró más su rendimiento al jugar en condición de local respecto de su propio rendimiento como visitante.

---

## Intervalo de confianza

Se calculó un intervalo de confianza del 95% para la diferencia media de puntos por partido.

| Medida | Valor |
|---|---:|
| Media de la diferencia | 0.6413 |
| Límite inferior | 0.5130 |
| Límite superior | 0.7696 |

El intervalo de confianza obtenido fue:

$$
[0.5130; 0.7696]
$$

Como el intervalo se encuentra completamente por encima de cero, se interpreta que la diferencia media es positiva y estadísticamente significativa.

---

## Prueba t pareada para puntos por partido

Hipótesis planteadas:

$$
H_0: \mu_d = 0
$$

$$
H_1: \mu_d > 0
$$

Donde:

$$
d = Pts/PJ_{Local} - Pts/PJ_{Visitante}
$$

Resultado:

| Estadístico | Valor |
|---|---:|
| t | 10.2539 |
| p-valor | 0.00000000 |
| Decisión | Rechazar H0 |

Como el p-valor es menor que 0,05, se rechaza la hipótesis nula. Existe evidencia estadística suficiente para afirmar que los equipos rindieron mejor como locales.

---

## Prueba t pareada para goles por partido

También se comparó el promedio de goles por partido de local y visitante.

| Estadístico | Valor |
|---|---:|
| t | 4.0416 |
| p-valor | 0.00019822 |
| Decisión | Rechazar H0 |

El resultado permite concluir que los equipos también marcaron significativamente más goles jugando como locales.

---

## Prueba de Wilcoxon

Como complemento no paramétrico se aplicó la prueba de Wilcoxon para muestras relacionadas.

| Estadístico | Valor |
|---|---:|
| Estadístico Wilcoxon | 405.0000 |
| p-valor | 0.00000211 |
| Decisión | Rechazar H0 |

Esta prueba confirma la conclusión obtenida con la prueba t pareada.

---

## Prueba binomial

Se analizaron solamente los partidos con ganador, comparando victorias locales contra victorias visitantes.

| Medida | Valor |
|---|---:|
| Victorias locales | 169 |
| Victorias visitantes | 88 |
| Proporción de victorias locales | 0.6576 |
| p-valor | 0.00000024 |
| Decisión | Rechazar H0 |

Entre los partidos con ganador, el local ganó una proporción significativamente mayor.

---

## Prueba chi-cuadrado

Se aplicó una prueba chi-cuadrado para analizar si la distribución de resultados depende de la condición local/visitante.

| Estadístico | Valor |
|---|---:|
| Chi-cuadrado | 51.0584 |
| Grados de libertad | 2 |
| p-valor | 0.00000000 |
| Decisión | Rechazar H0 |

Como el p-valor es menor que 0,05, se concluye que la distribución de resultados está asociada a la condición de localía.

---

## Teorema de Chebyshev

Se aplicó el Teorema de Chebyshev sobre la variable Delta_Pts_PJ con k = 2.

| Medida | Valor |
|---|---:|
| Media | 0.6413 |
| Desvío estándar | 0.3309 |
| Límite inferior | -0.0206 |
| Límite superior | 1.3032 |
| Proporción observada dentro del intervalo | 0.9286 |
| Cota mínima de Chebyshev | 0.7500 |

Según Chebyshev, al menos el 75.00% de los datos deberían encontrarse dentro de dos desvíos estándar de la media. En la muestra observada, la proporción fue del 92.86%.

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

