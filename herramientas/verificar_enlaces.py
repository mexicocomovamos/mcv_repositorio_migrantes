"""Comprueba que todos los enlaces e imágenes locales de las páginas HTML
apunten a archivos existentes. Devuelve código 1 si falta alguno."""
import re
import sys
from pathlib import Path

raiz = Path(__file__).resolve().parent.parent
faltan = []
for pagina in list(raiz.glob('*.html')) + list(raiz.glob('ciudades/*.html')):
    texto = pagina.read_text(encoding='utf-8')
    for ref in set(re.findall(r'(?:href|src)="([^"#][^"]*)"', texto)):
        if ref.startswith(('http://', 'https://', 'mailto:')):
            continue
        if not (pagina.parent / ref.split('#')[0]).exists():
            faltan.append(f'{pagina.relative_to(raiz)} -> {ref}')
if faltan:
    print('Enlaces rotos:')
    print('\n'.join(faltan))
    sys.exit(1)
print('Todos los enlaces locales resuelven.')
