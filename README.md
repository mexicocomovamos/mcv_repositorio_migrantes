# Repositorio de visualizaciones: integración laboral de población migrante

Sitio público: https://mexicocomovamos.github.io/mcv_repositorio_migrantes/

Reúne las fichas territoriales de las 39 ciudades autorrepresentadas de la
ENOE y las gráficas del estudio *Oportunidades de integración laboral de
población migrante en México* de México ¿Cómo Vamos?.

## Estructura

- `index.html`: portada con el índice de ciudades y de gráficas.
- `ciudades/<ciudad>.html`: ficha territorial de cada ciudad, con navegación
  entre ciudades y sección de descargas.
- `ciudades/<ciudad>/*.png`: las siete gráficas de cada ficha.
- `graficas/informe/*.png`: figuras del informe.
- `assets/`: estilo, logo, favicon e imagen de vista previa.
- `catalogo_visualizaciones.csv`: lista de todos los archivos con su URL.
- `herramientas/verificar_enlaces.py`: comprobación de enlaces que corre
  GitHub Actions en cada subida.

## Cómo se actualiza

El contenido se genera con `scripts/37_sitio_github.py` del proyecto de
análisis (no está en este repositorio) a partir de las salidas del pipeline en
R. No conviene editar los HTML a mano: se sobrescriben en la siguiente
generación. Para publicar cambios basta hacer *commit* y *push* a `main`;
GitHub Pages sirve la rama tal cual (`.nojekyll`).

## Fuentes

INEGI (ENOE, DENUE, Censos Económicos 2024, Encuesta Intercensal 2025) e
IMSS (datos abiertos de puestos asegurados). Elaboración propia.
