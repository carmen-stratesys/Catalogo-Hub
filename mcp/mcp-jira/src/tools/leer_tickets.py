"""Descripción: Lee tickets ficticios de un proyecto.
Entradas: proyecto (texto).
Salida: elementos ficticios con id y título.
Efecto: lectura.
"""

def leer_tickets(proyecto: str) -> list[dict[str, str]]:
    if not proyecto.strip():
        raise ValueError("Indica un proyecto de ejemplo.")
    return [{"id": "demo-1", "titulo": "Tickets de ejemplo"}]
