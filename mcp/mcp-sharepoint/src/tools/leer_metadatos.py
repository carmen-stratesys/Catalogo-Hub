"""Descripción: Devuelve metadatos ficticios de un documento.
Entradas: proyecto (texto).
Salida: elementos ficticios con id y título.
Efecto: lectura.
"""

def leer_metadatos(proyecto: str) -> list[dict[str, str]]:
    if not proyecto.strip():
        raise ValueError("Indica un proyecto de ejemplo.")
    return [{"id": "demo-1", "titulo": "Metadatos de ejemplo"}]
