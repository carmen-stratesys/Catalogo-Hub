"""Carga las instrucciones del agente ficticio; no invoca modelos."""
from pathlib import Path


def cargar_instrucciones() -> str:
    return (Path(__file__).resolve().parents[1] / "instrucciones.md").read_text(encoding="utf-8")
