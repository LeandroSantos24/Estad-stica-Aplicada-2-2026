from pathlib import Path

# ============================================================
# CONFIGURACIÓN GENERAL DEL PROYECTO
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATOS_DIR = BASE_DIR / "datos"
RESULTADOS_DIR = BASE_DIR / "resultados"
TABLAS_DIR = RESULTADOS_DIR / "tablas"
GRAFICOS_DIR = RESULTADOS_DIR / "graficos"

HTML_FBREF = DATOS_DIR / "fbref_lpf_2023.html"
HTML_TRANSFERMARKT = DATOS_DIR / "transfermarkt_lpf_2023.html"
VALORES_PLANTILLA = DATOS_DIR / "valores_plantilla_2023.csv"

INFORME_AUTO = RESULTADOS_DIR / "informe_auto.md"

ALPHA = 0.05
