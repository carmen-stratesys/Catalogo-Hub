"""Descripción: Devuelve repositorios ficticios.
Entradas: proyecto (texto).
Salida: elementos ficticios con id y título.
Efecto: lectura.
"""

def leer_repositorios(proyecto: str) -> list[dict[str, str]]:
    if not proyecto.strip():
        raise ValueError("Indica un proyecto de ejemplo.")
    return [{"id": "demo-1", "titulo": "Repositorios de ejemplo"}]
