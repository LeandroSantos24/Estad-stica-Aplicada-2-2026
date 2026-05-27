#Instalación y ejecución
1. Crear entorno virtual
python3 -m venv venv
2. Activar entorno virtual en Linux/Kali
source venv/bin/activate

Cuando el entorno esté activado, la terminal debería mostrar algo parecido a:

(venv) usuario@equipo:~/est_II$
3. Instalar dependencias
pip install -r requirements.txt
4. Ejecutar el análisis
python main.py

Estructura del proyecto
est_II/
│
├── datos/
│   ├── fbref_lpf_2023.html
│   ├── fbref_lpf_2023_files/
│   └── valores_plantilla_2023.csv
│
├── resultados/
│   ├── graficos/
│   ├── tablas/
│   └── informe_auto.md
│
├── src/
│   ├── config.py
│   ├── cargar_datos.py
│   ├── preparar_datos.py
│   ├── estadistica_descriptiva.py
│   ├── inferencia.py
│   ├── graficos.py
│   └── reporte.py
│
├── main.py
├── requirements.txt
└── README.md
Librerías utilizadas
pandas
numpy
scipy
matplotlib
tabulate
lxml
html5lib
beautifulsoup4

Qué genera el programa

El programa genera automáticamente tablas, gráficos e informe.

Tablas generadas
resultados/tablas/base_localia_lpf_2023.csv
resultados/tablas/resumen_global_resultados.csv
resultados/tablas/resumen_descriptivo.csv
resultados/tablas/ranking_localia.csv
resultados/tablas/resultados_inferencia.csv
resultados/tablas/chi_cuadrado_observadas.csv
resultados/tablas/chi_cuadrado_esperadas.csv
resultados/tablas/zscore_percentiles_localia.csv
Gráficos generados
resultados/graficos/01_resumen_local_visitante.png
resultados/graficos/02_ranking_delta_puntos.png
resultados/graficos/03_boxplot_delta_puntos.png
resultados/graficos/04_dispersion_local_visitante.png
resultados/graficos/05_goles_local_visitante.png
resultados/graficos/06_zscore_localia.png
Informe automático
resultados/informe_auto.md
Variables principales

La variable central del análisis es:

Delta_Pts_PJ = Pts_PJ_Local - Pts_PJ_Visitante

Esta variable mide la ventaja de localía de cada equipo.

Si Delta_Pts_PJ es positivo, el equipo obtuvo más puntos por partido jugando como local.

Si Delta_Pts_PJ es negativo, el equipo obtuvo mejor rendimiento como visitante.

Otras variables calculadas:

Pts_PJ_Local
Pts_PJ_Visitante
GF_PJ_Local
GF_PJ_Visitante
Delta_GF_PJ
Eficacia_Local_%
Eficacia_Visitante_%
Pct_Victorias_Local
Pct_Victorias_Visitante
Herramientas estadísticas aplicadas
Estadística descriptiva.
Media.
Mediana.
Varianza.
Desvío estándar.
Cuartiles.
Intervalo de confianza para la diferencia media.
Prueba t pareada.
Prueba no paramétrica de Wilcoxon.
Prueba binomial.
Prueba chi-cuadrado.
Z-score.
Percentiles.
Teorema de Chebyshev.
Resultado descriptivo principal

En la temporada 2023 se analizaron 378 partidos.

Los equipos locales obtuvieron:

1.661 puntos por partido
1.204 goles por partido
44.71% de victorias

Los equipos visitantes obtuvieron:

1.019 puntos por partido
0.854 goles por partido
23.28% de victorias

La diferencia media de puntos por partido fue:

Delta_Pts_PJ = 0.6413

Esto significa que, en promedio, los equipos obtuvieron aproximadamente 0.64 puntos más por partido jugando como locales.

Resultado inferencial principal

Se aplicó una prueba t pareada para comparar el rendimiento del mismo equipo como local y como visitante.

Hipótesis:

H0: μd = 0
H1: μd > 0

Donde:

d = Pts/PJ Local - Pts/PJ Visitante

Resultado:

t = 10.2539
p-valor < 0.0001
Decisión: Rechazar H0

Por lo tanto, existe evidencia estadística suficiente para afirmar que los equipos rindieron mejor jugando como locales.

Conclusión general

Los resultados descriptivos e inferenciales permiten afirmar que en la Liga Profesional Argentina 2023 existió una ventaja de localía estadísticamente significativa.

Los equipos locales obtuvieron más puntos, marcaron más goles y ganaron una mayor proporción de partidos que los equipos visitantes.

Cómo defender el proyecto

El flujo del programa es el siguiente:

1. cargar_datos.py
   Lee el HTML de FBref.

2. preparar_datos.py
   Selecciona la tabla Home/Away y calcula variables derivadas.

3. estadistica_descriptiva.py
   Calcula medias, varianzas, desvíos, ranking y resumen global.

4. inferencia.py
   Aplica intervalos de confianza, pruebas de hipótesis, Wilcoxon, binomial, chi-cuadrado, Z-score, percentiles y Chebyshev.

5. graficos.py
   Genera las imágenes listas para el informe.

6. reporte.py
   Genera un informe automático en Markdown.

7. main.py
   Ejecuta todo el proceso completo.
Observación

El archivo valores_plantilla_2023.csv queda preparado para incorporar luego el valor económico de los planteles y analizar si existe relación entre el valor de mercado del equipo y la ventaja de localía.


Guardá con:

```text
CTRL + O
ENTER
CTRL + X

Después abrilo en VS Code y ya debería verse completo.